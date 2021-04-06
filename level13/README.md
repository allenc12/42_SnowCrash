# level13

## GDB is neat

Our hint here is a solitary binary file, with some rather helpful output.
```bash
level13@SnowCrash:~$ ls -l
total 8
-rwsr-sr-x 1 flag13 level13 7303 Aug 30  2015 level13
level13@SnowCrash:~$ ./level13
UID 2013 started us but we we expect 4242
```
Disassembling main reveals the program performing a simple comparison against `getuid` and then passing a pointer to `ft_des`
```bash
level13@SnowCrash:~$ gdb -batch -ex 'file level13' -ex 'disas main'
Dump of assembler code for function main:
   0x0804858c <+0>:     push   %ebp
   0x0804858d <+1>:     mov    %esp,%ebp
   0x0804858f <+3>:     and    $0xfffffff0,%esp
   0x08048592 <+6>:     sub    $0x10,%esp
   0x08048595 <+9>:     call   0x8048380 <getuid@plt>
   0x0804859a <+14>:    cmp    $0x1092,%eax
   0x0804859f <+19>:    je     0x80485cb <main+63>
   0x080485a1 <+21>:    call   0x8048380 <getuid@plt>
   0x080485a6 <+26>:    mov    $0x80486c8,%edx
   0x080485ab <+31>:    movl   $0x1092,0x8(%esp)
   0x080485b3 <+39>:    mov    %eax,0x4(%esp)
   0x080485b7 <+43>:    mov    %edx,(%esp)
   0x080485ba <+46>:    call   0x8048360 <printf@plt>
   0x080485bf <+51>:    movl   $0x1,(%esp)
   0x080485c6 <+58>:    call   0x80483a0 <exit@plt>
   0x080485cb <+63>:    movl   $0x80486ef,(%esp)
   0x080485d2 <+70>:    call   0x8048474 <ft_des>
   0x080485d7 <+75>:    mov    $0x8048709,%edx
   0x080485dc <+80>:    mov    %eax,0x4(%esp)
   0x080485e0 <+84>:    mov    %edx,(%esp)
   0x080485e3 <+87>:    call   0x8048360 <printf@plt>
   0x080485e8 <+92>:    leave
   0x080485e9 <+93>:    ret
End of assembler dump.
```

At this point we have two ways of solving this level:
### Changing registers at runtime in a debugger to bypass the uid check
```bash
level13@SnowCrash:~$ gdb -batch -ex 'file level13' -ex 'b *main+14' -ex 'r' -ex 'set $eax=4242' -ex 'c'
Breakpoint 1 at 0x804859a

Breakpoint 1, 0x0804859a in main ()
your token is 2A31L79asukciNyi8uppkEuSx
[Inferior 1 (process 21968) exited with code 050]
level13@SnowCrash:~$ su level14
Password: 2A31L79asukciNyi8uppkEuSx
level14@SnowCrash:~$
```

### Reverse engineering `ft_des`

This method is significantly more time consuming and difficult.

Starting with the disassembly of `ft_des`, here I have renamed offsets relative to ebp into more helpful names. TODO finish
```bash
level13@SnowCrash:~$ gdb -batch -ex 'file level13' -ex 'set disassembly-flavor intel' -ex 'disas ft_des'
Dump of assembler code for function ft_des:
var_2C= DWORD PTR -0x2c
ii= DWORD PTR -0x1c
jj= DWORD PTR -0x18
var_14= DWORD PTR -0x14
var_10= DWORD PTR -0x10
res= DWORD PTR -0xC
s= DWORD PTR  8
   0x08048474 <+0>:     push   ebp
   0x08048475 <+1>:     mov    ebp,esp
   0x08048477 <+3>:     push   edi
   0x08048478 <+4>:     sub    esp,0x44
   0x0804847b <+7>:     mov    eax,DWORD PTR [ebp+s]
   0x0804847e <+10>:    mov    DWORD PTR [esp],eax
   0x08048481 <+13>:    call   0x8048370 <strdup@plt>
   0x08048486 <+18>:    mov    DWORD PTR [ebp+res],eax          ; res=strdup(s)
   0x08048489 <+21>:    mov    DWORD PTR [ebp+jj],0x0           ; ii=0
   0x08048490 <+28>:    mov    DWORD PTR [ebp+ii],0x0           ; jj=0
   0x08048497 <+35>:    jmp    0x804855b <ft_des+231>           ; yump
   0x0804849c <+40>:    cmp    DWORD PTR [ebp+jj],0x6
   0x080484a0 <+44>:    jne    0x80484a9 <ft_des+53>
   0x080484a2 <+46>:    mov    DWORD PTR [ebp+jj],0x0
   0x080484a9 <+53>:    mov    eax,DWORD PTR [ebp+ii]
   0x080484ac <+56>:    and    eax,0x1
   0x080484af <+59>:    test   al,al
   0x080484b1 <+61>:    je     0x80484ff <ft_des+139>
   0x080484b3 <+63>:    mov    DWORD PTR [ebp+var_14],0x0
   0x080484ba <+70>:    jmp    0x80484ea <ft_des+118>
   0x080484bc <+72>:    mov    eax,DWORD PTR [ebp+ii]
   0x080484bf <+75>:    mov    edx,DWORD PTR [ebp+res]
   0x080484c2 <+78>:    add    eax,edx
   0x080484c4 <+80>:    movzx  edx,BYTE PTR [eax]
   0x080484c7 <+83>:    add    edx,0x1
   0x080484ca <+86>:    mov    BYTE PTR [eax],dl
   0x080484cc <+88>:    mov    eax,DWORD PTR [ebp+ii]
   0x080484cf <+91>:    mov    edx,DWORD PTR [ebp+res]
   0x080484d2 <+94>:    add    eax,edx
   0x080484d4 <+96>:    movzx  eax,BYTE PTR [eax]
   0x080484d7 <+99>:    cmp    al,0x7f
   0x080484d9 <+101>:   jne    0x80484e6 <ft_des+114>
   0x080484db <+103>:   mov    eax,DWORD PTR [ebp+ii]
   0x080484de <+106>:   mov    edx,DWORD PTR [ebp+res]
   0x080484e1 <+109>:   add    eax,edx
   0x080484e3 <+111>:   mov    BYTE PTR [eax],0x20
   0x080484e6 <+114>:   add    DWORD PTR [ebp+var_14],0x1
   0x080484ea <+118>:   mov    eax,DWORD PTR [ebp+jj]
   0x080484ed <+121>:   add    eax,0x80486c0
   0x080484f2 <+126>:   movzx  eax,BYTE PTR [eax]
   0x080484f5 <+129>:   movsx  eax,al
   0x080484f8 <+132>:   cmp    eax,DWORD PTR [ebp+var_14]
   0x080484fb <+135>:   jg     0x80484bc <ft_des+72>
   0x080484fd <+137>:   jmp    0x8048553 <ft_des+223>
   0x080484ff <+139>:   mov    eax,DWORD PTR [ebp+ii]
   0x08048502 <+142>:   and    eax,0x1
   0x08048505 <+145>:   test   eax,eax
   0x08048507 <+147>:   jne    0x8048553 <ft_des+223>
   0x08048509 <+149>:   mov    DWORD PTR [ebp+var_10],0x0
   0x08048510 <+156>:   jmp    0x8048540 <ft_des+204>
   0x08048512 <+158>:   mov    eax,DWORD PTR [ebp+ii]
   0x08048515 <+161>:   mov    edx,DWORD PTR [ebp+res]
   0x08048518 <+164>:   add    eax,edx
   0x0804851a <+166>:   movzx  edx,BYTE PTR [eax]
   0x0804851d <+169>:   sub    edx,0x1
   0x08048520 <+172>:   mov    BYTE PTR [eax],dl
   0x08048522 <+174>:   mov    eax,DWORD PTR [ebp+ii]
   0x08048525 <+177>:   mov    edx,DWORD PTR [ebp+res]
   0x08048528 <+180>:   add    eax,edx
   0x0804852a <+182>:   movzx  eax,BYTE PTR [eax]
   0x0804852d <+185>:   cmp    al,0x1f
   0x0804852f <+187>:   jne    0x804853c <ft_des+200>
   0x08048531 <+189>:   mov    eax,DWORD PTR [ebp+ii]
   0x08048534 <+192>:   mov    edx,DWORD PTR [ebp+res]
   0x08048537 <+195>:   add    eax,edx
   0x08048539 <+197>:   mov    BYTE PTR [eax],0x7e
   0x0804853c <+200>:   add    DWORD PTR [ebp+var_10],0x1
   0x08048540 <+204>:   mov    eax,DWORD PTR [ebp+jj]
   0x08048543 <+207>:   add    eax,0x80486c0
   0x08048548 <+212>:   movzx  eax,BYTE PTR [eax]
   0x0804854b <+215>:   movsx  eax,al
   0x0804854e <+218>:   cmp    eax,DWORD PTR [ebp+var_10]
   0x08048551 <+221>:   jg     0x8048512 <ft_des+158>
   0x08048553 <+223>:   add    DWORD PTR [ebp+ii],0x1
   0x08048557 <+227>:   add    DWORD PTR [ebp+jj],0x1
   0x0804855b <+231>:   mov    eax,DWORD PTR [ebp+res]
   0x0804855e <+234>:   mov    DWORD PTR [ebp+var_2C],0xffffffff
   0x08048565 <+241>:   mov    edx,eax
   0x08048567 <+243>:   mov    eax,0x0
   0x0804856c <+248>:   mov    ecx,DWORD PTR [ebp+var_2C]
   0x0804856f <+251>:   mov    edi,edx
   0x08048571 <+253>:   repnz scas al,BYTE PTR es:[edi]
   0x08048573 <+255>:   mov    eax,ecx
   0x08048575 <+257>:   not    eax
   0x08048577 <+259>:   sub    eax,0x1
   0x0804857a <+262>:   cmp    eax,DWORD PTR [ebp+ii]
   0x0804857d <+265>:   ja     0x804849c <ft_des+40>
   0x08048583 <+271>:   mov    eax,DWORD PTR [ebp+res]
   0x08048586 <+274>:   add    esp,0x44
   0x08048589 <+277>:   pop    edi
   0x0804858a <+278>:   pop    ebp
   0x0804858b <+279>:   ret
End of assembler dump.
```

Wack string offset skullduggery
```bash
level13@SnowCrash:~$ gdb -batch -ex 'file level13' -ex 'x/2i *ft_des+118' -ex 'x/s 0x80486c0'
   0x80484ea <ft_des+118>:      mov    -0x18(%ebp),%eax
   0x80484ed <ft_des+121>:      add    $0x80486c0,%eax
0x80486c0:       "0123456"
```

Lets also extract the encrypted token passed to ft_des
```bash
level13@SnowCrash:~$ gdb -batch -ex 'file level13' -ex 'x/2i *main+63' -ex 'x/s 0x80486ef'
   0x80485cb <main+63>: movl   $0x80486ef,(%esp)
   0x80485d2 <main+70>: call   0x8048474 <ft_des>
0x80486ef:       "boe]!ai0FB@.:|L6l@A?>qJ}I"
```

(lmao just use a decompiler)
```c
static const char *alph = "0123456";
char *ft_des(char *str)
{
    unsigned int ii;
    int jj, i, j;
    char *res;
    
    res = strdup(str);
    for (ii=jj=0; strlen(res) > ii; ++ii,++jj) {
        if (jj == 6)
            jj = 0
        if (ii & 1) {
            for (i=0; alph[jj] > i; ++i)
                if (++res[ii] == 127)
                    res[ii] = ' ';
        } else {
            for (j=0; alph[jj] > j; ++j)
                if (--res[ii] == 31)
                    res[ii] = 126;
        }
    }
    return res;
}
```
