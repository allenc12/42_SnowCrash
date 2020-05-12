# level09

Simple substitution cipher based on character index
```bash
level09@SnowCrash:~ $ cat token
#OUTPUT
level09@SnowCrash:~ $ python -c 'print("".join([chr(ord(c) - i) for i,c in enumerate("#TOKENHERE")])'
#OUTPUT
level09@SnowCrash:~ $ su flag09
#OUTPUT
level09@SnowCrash:~ $ getflag
#OUTPUT
level09@SnowCrash:~ $ su level10
#OUTPUT
level10@SnowCrash:~ $ 
