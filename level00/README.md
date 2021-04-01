# level00

Launch provided Live-CD ISO and log in
```bash
root@kali:~# ssh -p 4242 level00@SnowCrash
           _____                      _____               _
          / ____|                    / ____|             | |
         | (___  _ __   _____      _| |     _ __ __ _ ___| |__
          \___ \| '_ \ / _ \ \ /\ / / |    | '__/ _` / __| '_ \
          ____) | | | | (_) \ V  V /| |____| | | (_| \__ \ | | |
         |_____/|_| |_|\___/ \_/\_/  \_____|_|  \__,_|___/_| |_|

  Good luck & Have fun

          192.168.56.101
level00@SnowCrash's password: level00
level00@SnowCrash:~$
```

Search for suspicious files using `find` on a whim with no hints whatsoever
```bash
level00@SnowCrash:~$ find / -type -f -user flag00 2>/dev/null
/usr/sbin/john
level00@SnowCrash:~$ cat /usr/sbin/john
cdiiddwpgswtgt
level00@SnowCrash:~$
```

Simple monoalphabetic cipher, [this website](https://rot13.com/) is very useful for basic rotN variations.
```bash
level00@SnowCrash:~$ cat /usr/sbin/john | tr '[A-Za-z]' '[L-ZA-Kl-za-k]'
nottoohardhere
level00@SnowCrash:~$
```

Claim flag00
```bash
level00@SnowCrash:~$ su flag00
Password: nottoohardhere
flag00@SnowCrash:~$ getflag
Check flag.Here is your token : x24ti5gi3x0ol2eh4esiuxias
flag00@SnowCrash:~$ su level01
Password: x24ti5gi3x0ol2eh4esiuxias
level01@SnowCrash:~$
```
