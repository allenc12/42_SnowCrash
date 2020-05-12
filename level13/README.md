# level13

Patching bytes in a binary file
```bash
level13@SnowCrash:~ $ xxd level13 > /tmp/level13; printf '90c\n\
        0000590: e4f0 83ec 10e8 e6fd ffff 3ddd 0700 0074  ..........=....t\n\
        .\n\
        w\n\
        q\n' | ed /tmp/level13;\
        xxd -r /tmp/level13 > /tmp/goat;\
        chmod +x /tmp/goat;\
        /tmp/goat
#OUTPUT
level13@SnowCrash:~ $ su flag13
Password
flag13@SnowCrash:~ $ getflag; su level14
#OUTPUT
Password:
level14@SnowCrash:~ $
```
