# level00

Launch provided Live-CD ISO and log in
```bash
login: level00
password: level00
level00:~ $
```

Search for suspicious files using `find`
```bash
level00:~ $ find / -type -f -user flag00 2>/dev/null
/etc/john # TODO get actual file path
level00:~ $ cat /etc/john
# TODO get contents of file
level00:~ $
```

Simple monoalphabetic cipher
```python
import sys

def rot_alpha(n):
    from string import ascii_lowercase as lc, ascii_uppercase as uc, maketrans
    lookup = maketrans(lc + uc, lc[n:] + lc[:n] + uc[n:] + uc[:n])
    return lambda s: s.translate(lookup)


print(rot_alpha(11)(sys.argv[1]))
```

Claim flag00
```bash
level00:~ $ su flag00
# TODO get password
flag00:~ $ getflag
#TODO getflag output
```
