# level00

Launch provided Live-CD ISO and log in
```bash
login: level00
password: level00
level00:~ $
```

Search for suspicious files using `find` on a whim with no hints whatsoever
```bash
level00:~ $ find / -type -f -user flag00 2>/dev/null
/usr/sbin/john
level00:~ $ cat /usr/sbin/john
cdiiddwpgswtgt
level00:~ $
```

Simple monoalphabetic cipher, [this website](https://rot13.com/) is very useful for basic rotN variations.
```bash
level00:~ $ cat /usr/sbin/john | tr '[A-Za-z]' '[L-ZA-Kl-za-k]'
nottoohardhere
level00:~ $ 
```

Claim flag00
```bash
level00:~ $ su flag00
Password: nottoohardhere
flag00:~ $ getflag
Check flag.Here is your token : x24ti5gi3x0ol2eh4esiuxias
flag00:~ $ 
```
