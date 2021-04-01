# level09

## Simple substitution cipher based on character index

Similar pair of files.
```bash
level09@SnowCrash:~$ ls
level09  token
level09@SnowCrash:~$ cat token
f4kmm6p|=�p�n��DB�Du{��
level09@SnowCrash:~$ xxd token
0000000: 6634 6b6d 6d36 707c 3d82 7f70 826e 8382  f4kmm6p|=..p.n..
0000010: 4442 8344 757b 7f8c 890a                 DB.Du{....
```
Hark, an epiphany hath led my journey toward the Python interpreter.
```bash
level09@SnowCrash:~$ python -c 'print "".join([chr(ord(c) - i) for i,c in enumerate(open("token").read()[:-1])])'
f3iji1ju5yuevaus41q1afiuq
level09@SnowCrash:~$ su flag09
Password: f3iji1ju5yuevaus41q1afiuq
Don't forget to launch getflag !
flag09@SnowCrash:~$ getflag
Check flag.Here is your token : s5cAJpM8ev6XHw998pRWG728z
flag09@SnowCrash:~$ su level10
Password: s5cAJpM8ev6XHw998pRWG728z
level10@SnowCrash:~$
```
