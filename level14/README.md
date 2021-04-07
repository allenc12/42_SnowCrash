# level14

## Binary Reverse Engineering

This level has no hint, so on an absolute whim, let's take a look at the getflag binary.
```bash
level14@SnowCrash:~$ ls -l
total 0
level14@SnowCrash:~$ nm -n /bin/getflag | egrep '08048[6-9]..'
08048604 T ft_des
0804871c T syscall_open
0804874c T syscall_gets
080487be T afterSubstr
08048843 T isLib
08048946 T main
level14@SnowCrash:~$ gdb -batch -ex 'file /bin/getflag' -ex 'set disassembly-flavor intel' -ex 'disas ft_des' -ex 'disas
syscall_open' -ex 'disas syscall_gets' -ex 'disas afterSubstr' -ex 'disas isLib' -ex 'disas main'
```
```asm
Dump of assembler code for function ft_des:
   0x08048604 <+0>:     push   ebp
   0x08048605 <+1>:     mov    ebp,esp
   0x08048607 <+3>:     push   edi
   0x08048608 <+4>:     sub    esp,0x44
   0x0804860b <+7>:     mov    eax,DWORD PTR [ebp+0x8]
   0x0804860e <+10>:    mov    DWORD PTR [esp],eax
   0x08048611 <+13>:    call   0x8048490 <strdup@plt>
   0x08048616 <+18>:    mov    DWORD PTR [ebp-0xc],eax
   0x08048619 <+21>:    mov    DWORD PTR [ebp-0x18],0x0
   0x08048620 <+28>:    mov    DWORD PTR [ebp-0x1c],0x0
   0x08048627 <+35>:    jmp    0x80486eb <ft_des+231>
   0x0804862c <+40>:    cmp    DWORD PTR [ebp-0x18],0x6
   0x08048630 <+44>:    jne    0x8048639 <ft_des+53>
   0x08048632 <+46>:    mov    DWORD PTR [ebp-0x18],0x0
   0x08048639 <+53>:    mov    eax,DWORD PTR [ebp-0x1c]
   0x0804863c <+56>:    and    eax,0x1
   0x0804863f <+59>:    test   al,al
   0x08048641 <+61>:    je     0x804868f <ft_des+139>
   0x08048643 <+63>:    mov    DWORD PTR [ebp-0x14],0x0
   0x0804864a <+70>:    jmp    0x804867a <ft_des+118>
   0x0804864c <+72>:    mov    eax,DWORD PTR [ebp-0x1c]
   0x0804864f <+75>:    mov    edx,DWORD PTR [ebp-0xc]
   0x08048652 <+78>:    add    eax,edx
   0x08048654 <+80>:    movzx  edx,BYTE PTR [eax]
   0x08048657 <+83>:    add    edx,0x1
   0x0804865a <+86>:    mov    BYTE PTR [eax],dl
   0x0804865c <+88>:    mov    eax,DWORD PTR [ebp-0x1c]
   0x0804865f <+91>:    mov    edx,DWORD PTR [ebp-0xc]
   0x08048662 <+94>:    add    eax,edx
   0x08048664 <+96>:    movzx  eax,BYTE PTR [eax]
   0x08048667 <+99>:    cmp    al,0x7f
   0x08048669 <+101>:   jne    0x8048676 <ft_des+114>
   0x0804866b <+103>:   mov    eax,DWORD PTR [ebp-0x1c]
   0x0804866e <+106>:   mov    edx,DWORD PTR [ebp-0xc]
   0x08048671 <+109>:   add    eax,edx
   0x08048673 <+111>:   mov    BYTE PTR [eax],0x20
   0x08048676 <+114>:   add    DWORD PTR [ebp-0x14],0x1
   0x0804867a <+118>:   mov    eax,DWORD PTR [ebp-0x18]
   0x0804867d <+121>:   add    eax,0x8048fa0
   0x08048682 <+126>:   movzx  eax,BYTE PTR [eax]
   0x08048685 <+129>:   movsx  eax,al
   0x08048688 <+132>:   cmp    eax,DWORD PTR [ebp-0x14]
   0x0804868b <+135>:   jg     0x804864c <ft_des+72>
   0x0804868d <+137>:   jmp    0x80486e3 <ft_des+223>
   0x0804868f <+139>:   mov    eax,DWORD PTR [ebp-0x1c]
   0x08048692 <+142>:   and    eax,0x1
   0x08048695 <+145>:   test   eax,eax
   0x08048697 <+147>:   jne    0x80486e3 <ft_des+223>
   0x08048699 <+149>:   mov    DWORD PTR [ebp-0x10],0x0
   0x080486a0 <+156>:   jmp    0x80486d0 <ft_des+204>
   0x080486a2 <+158>:   mov    eax,DWORD PTR [ebp-0x1c]
   0x080486a5 <+161>:   mov    edx,DWORD PTR [ebp-0xc]
   0x080486a8 <+164>:   add    eax,edx
   0x080486aa <+166>:   movzx  edx,BYTE PTR [eax]
   0x080486ad <+169>:   sub    edx,0x1
   0x080486b0 <+172>:   mov    BYTE PTR [eax],dl
   0x080486b2 <+174>:   mov    eax,DWORD PTR [ebp-0x1c]
   0x080486b5 <+177>:   mov    edx,DWORD PTR [ebp-0xc]
   0x080486b8 <+180>:   add    eax,edx
   0x080486ba <+182>:   movzx  eax,BYTE PTR [eax]
   0x080486bd <+185>:   cmp    al,0x1f
   0x080486bf <+187>:   jne    0x80486cc <ft_des+200>
   0x080486c1 <+189>:   mov    eax,DWORD PTR [ebp-0x1c]
   0x080486c4 <+192>:   mov    edx,DWORD PTR [ebp-0xc]
   0x080486c7 <+195>:   add    eax,edx
   0x080486c9 <+197>:   mov    BYTE PTR [eax],0x7e
   0x080486cc <+200>:   add    DWORD PTR [ebp-0x10],0x1
   0x080486d0 <+204>:   mov    eax,DWORD PTR [ebp-0x18]
   0x080486d3 <+207>:   add    eax,0x8048fa0
   0x080486d8 <+212>:   movzx  eax,BYTE PTR [eax]
   0x080486db <+215>:   movsx  eax,al
   0x080486de <+218>:   cmp    eax,DWORD PTR [ebp-0x10]
   0x080486e1 <+221>:   jg     0x80486a2 <ft_des+158>
   0x080486e3 <+223>:   add    DWORD PTR [ebp-0x1c],0x1
   0x080486e7 <+227>:   add    DWORD PTR [ebp-0x18],0x1
   0x080486eb <+231>:   mov    eax,DWORD PTR [ebp-0xc]
   0x080486ee <+234>:   mov    DWORD PTR [ebp-0x2c],0xffffffff
   0x080486f5 <+241>:   mov    edx,eax
   0x080486f7 <+243>:   mov    eax,0x0
   0x080486fc <+248>:   mov    ecx,DWORD PTR [ebp-0x2c]
   0x080486ff <+251>:   mov    edi,edx
   0x08048701 <+253>:   repnz scas al,BYTE PTR es:[edi]
   0x08048703 <+255>:   mov    eax,ecx
   0x08048705 <+257>:   not    eax
   0x08048707 <+259>:   sub    eax,0x1
   0x0804870a <+262>:   cmp    eax,DWORD PTR [ebp-0x1c]
   0x0804870d <+265>:   ja     0x804862c <ft_des+40>
   0x08048713 <+271>:   mov    eax,DWORD PTR [ebp-0xc]
   0x08048716 <+274>:   add    esp,0x44
   0x08048719 <+277>:   pop    edi
   0x0804871a <+278>:   pop    ebp
   0x0804871b <+279>:   ret
End of assembler dump.
Dump of assembler code for function syscall_open:
   0x0804871c <+0>:     push   ebp
   0x0804871d <+1>:     mov    ebp,esp
   0x0804871f <+3>:     push   esi
   0x08048720 <+4>:     push   ebx
   0x08048721 <+5>:     sub    esp,0x10
   0x08048724 <+8>:     mov    DWORD PTR [ebp-0xc],0xffffffff
   0x0804872b <+15>:    mov    eax,0x5
   0x08048730 <+20>:    mov    ebx,DWORD PTR [ebp+0x8]
   0x08048733 <+23>:    mov    ecx,DWORD PTR [ebp+0xc]
   0x08048736 <+26>:    mov    edx,0x0
   0x0804873b <+31>:    int    0x80
   0x0804873d <+33>:    mov    esi,eax
   0x0804873f <+35>:    mov    DWORD PTR [ebp-0xc],esi
   0x08048742 <+38>:    mov    eax,DWORD PTR [ebp-0xc]
   0x08048745 <+41>:    add    esp,0x10
   0x08048748 <+44>:    pop    ebx
   0x08048749 <+45>:    pop    esi
   0x0804874a <+46>:    pop    ebp
   0x0804874b <+47>:    ret
End of assembler dump.
Dump of assembler code for function syscall_gets:
   0x0804874c <+0>:     push   ebp
   0x0804874d <+1>:     mov    ebp,esp
   0x0804874f <+3>:     push   esi
   0x08048750 <+4>:     push   ebx
   0x08048751 <+5>:     sub    esp,0x10
   0x08048754 <+8>:     mov    DWORD PTR [ebp-0x10],0x0
   0x0804875b <+15>:    jmp    0x804879b <syscall_gets+79>
   0x0804875d <+17>:    mov    eax,DWORD PTR [ebp-0x10]
   0x08048760 <+20>:    mov    edx,DWORD PTR [ebp+0x8]
   0x08048763 <+23>:    lea    esi,[edx+eax*1]
   0x08048766 <+26>:    mov    eax,0x3
   0x0804876b <+31>:    mov    ebx,DWORD PTR [ebp+0x10]
   0x0804876e <+34>:    mov    ecx,esi
   0x08048770 <+36>:    mov    edx,0x1
   0x08048775 <+41>:    int    0x80
   0x08048777 <+43>:    mov    esi,eax
   0x08048779 <+45>:    mov    DWORD PTR [ebp-0xc],esi
   0x0804877c <+48>:    cmp    DWORD PTR [ebp-0xc],0x1
   0x08048780 <+52>:    jne    0x80487a8 <syscall_gets+92>
   0x08048782 <+54>:    mov    eax,DWORD PTR [ebp-0x10]
   0x08048785 <+57>:    mov    edx,DWORD PTR [ebp+0x8]
   0x08048788 <+60>:    add    eax,edx
   0x0804878a <+62>:    movzx  eax,BYTE PTR [eax]
   0x0804878d <+65>:    cmp    al,0xa
   0x0804878f <+67>:    jne    0x8048797 <syscall_gets+75>
   0x08048791 <+69>:    add    DWORD PTR [ebp-0x10],0x1
   0x08048795 <+73>:    jmp    0x80487a9 <syscall_gets+93>
   0x08048797 <+75>:    add    DWORD PTR [ebp-0x10],0x1
   0x0804879b <+79>:    mov    eax,DWORD PTR [ebp+0xc]
   0x0804879e <+82>:    sub    eax,0x1
   0x080487a1 <+85>:    cmp    eax,DWORD PTR [ebp-0x10]
   0x080487a4 <+88>:    ja     0x804875d <syscall_gets+17>
   0x080487a6 <+90>:    jmp    0x80487a9 <syscall_gets+93>
   0x080487a8 <+92>:    nop
   0x080487a9 <+93>:    mov    eax,DWORD PTR [ebp-0x10]
   0x080487ac <+96>:    mov    edx,DWORD PTR [ebp+0x8]
   0x080487af <+99>:    add    eax,edx
   0x080487b1 <+101>:   mov    BYTE PTR [eax],0x0
   0x080487b4 <+104>:   mov    eax,DWORD PTR [ebp-0x10]
   0x080487b7 <+107>:   add    esp,0x10
   0x080487ba <+110>:   pop    ebx
   0x080487bb <+111>:   pop    esi
   0x080487bc <+112>:   pop    ebp
   0x080487bd <+113>:   ret
End of assembler dump.
Dump of assembler code for function afterSubstr:
   0x080487be <+0>:     push   ebp
   0x080487bf <+1>:     mov    ebp,esp
   0x080487c1 <+3>:     sub    esp,0x10
   0x080487c4 <+6>:     mov    DWORD PTR [ebp-0x8],0x0
   0x080487cb <+13>:    mov    eax,DWORD PTR [ebp+0x8]
   0x080487ce <+16>:    mov    DWORD PTR [ebp-0x4],eax
   0x080487d1 <+19>:    jmp    0x8048821 <afterSubstr+99>
   0x080487d3 <+21>:    mov    DWORD PTR [ebp-0x8],0x1
   0x080487da <+28>:    mov    DWORD PTR [ebp-0xc],0x0
   0x080487e1 <+35>:    jmp    0x8048804 <afterSubstr+70>
   0x080487e3 <+37>:    mov    eax,DWORD PTR [ebp-0xc]
   0x080487e6 <+40>:    add    eax,DWORD PTR [ebp+0xc]
   0x080487e9 <+43>:    movzx  edx,BYTE PTR [eax]
   0x080487ec <+46>:    mov    eax,DWORD PTR [ebp-0xc]
   0x080487ef <+49>:    add    eax,DWORD PTR [ebp-0x4]
   0x080487f2 <+52>:    movzx  eax,BYTE PTR [eax]
   0x080487f5 <+55>:    cmp    dl,al
   0x080487f7 <+57>:    je     0x8048800 <afterSubstr+66>
   0x080487f9 <+59>:    mov    DWORD PTR [ebp-0x8],0x0
   0x08048800 <+66>:    add    DWORD PTR [ebp-0xc],0x1
   0x08048804 <+70>:    cmp    DWORD PTR [ebp-0x8],0x1
   0x08048808 <+74>:    jne    0x8048817 <afterSubstr+89>
   0x0804880a <+76>:    mov    eax,DWORD PTR [ebp-0xc]
   0x0804880d <+79>:    add    eax,DWORD PTR [ebp+0xc]
   0x08048810 <+82>:    movzx  eax,BYTE PTR [eax]
   0x08048813 <+85>:    test   al,al
   0x08048815 <+87>:    jne    0x80487e3 <afterSubstr+37>
   0x08048817 <+89>:    cmp    DWORD PTR [ebp-0x8],0x1
   0x0804881b <+93>:    je     0x804882d <afterSubstr+111>
   0x0804881d <+95>:    add    DWORD PTR [ebp-0x4],0x1
   0x08048821 <+99>:    mov    eax,DWORD PTR [ebp-0x4]
   0x08048824 <+102>:   movzx  eax,BYTE PTR [eax]
   0x08048827 <+105>:   test   al,al
   0x08048829 <+107>:   jne    0x80487d3 <afterSubstr+21>
   0x0804882b <+109>:   jmp    0x804882e <afterSubstr+112>
   0x0804882d <+111>:   nop
   0x0804882e <+112>:   cmp    DWORD PTR [ebp-0x8],0x0
   0x08048832 <+116>:   jne    0x804883b <afterSubstr+125>
   0x08048834 <+118>:   mov    eax,0x0
   0x08048839 <+123>:   jmp    0x8048841 <afterSubstr+131>
   0x0804883b <+125>:   mov    eax,DWORD PTR [ebp-0xc]
   0x0804883e <+128>:   add    eax,DWORD PTR [ebp-0x4]
   0x08048841 <+131>:   leave
   0x08048842 <+132>:   ret
End of assembler dump.
Dump of assembler code for function isLib:
   0x08048843 <+0>:     push   ebp
   0x08048844 <+1>:     mov    ebp,esp
   0x08048846 <+3>:     sub    esp,0x18
   0x08048849 <+6>:     mov    eax,DWORD PTR [ebp+0xc]
   0x0804884c <+9>:     mov    DWORD PTR [esp+0x4],eax
   0x08048850 <+13>:    mov    eax,DWORD PTR [ebp+0x8]
   0x08048853 <+16>:    mov    DWORD PTR [esp],eax
   0x08048856 <+19>:    call   0x80487be <afterSubstr>
   0x0804885b <+24>:    mov    DWORD PTR [ebp-0x4],eax
   0x0804885e <+27>:    cmp    DWORD PTR [ebp-0x4],0x0
   0x08048862 <+31>:    jne    0x804886e <isLib+43>
   0x08048864 <+33>:    mov    eax,0x0
   0x08048869 <+38>:    jmp    0x8048944 <isLib+257>
   0x0804886e <+43>:    mov    eax,DWORD PTR [ebp-0x4]
   0x08048871 <+46>:    movzx  eax,BYTE PTR [eax]
   0x08048874 <+49>:    cmp    al,0x2d
   0x08048876 <+51>:    je     0x8048882 <isLib+63>
   0x08048878 <+53>:    mov    eax,0x0
   0x0804887d <+58>:    jmp    0x8048944 <isLib+257>
   0x08048882 <+63>:    mov    DWORD PTR [ebp-0x8],0x0
   0x08048889 <+70>:    add    DWORD PTR [ebp-0x4],0x1
   0x0804888d <+74>:    jmp    0x804889a <isLib+87>
   0x0804888f <+76>:    mov    DWORD PTR [ebp-0x8],0x1
   0x08048896 <+83>:    add    DWORD PTR [ebp-0x4],0x1
   0x0804889a <+87>:    mov    eax,DWORD PTR [ebp-0x4]
   0x0804889d <+90>:    movzx  eax,BYTE PTR [eax]
   0x080488a0 <+93>:    cmp    al,0x2f
   0x080488a2 <+95>:    jle    0x80488ae <isLib+107>
   0x080488a4 <+97>:    mov    eax,DWORD PTR [ebp-0x4]
   0x080488a7 <+100>:   movzx  eax,BYTE PTR [eax]
   0x080488aa <+103>:   cmp    al,0x39
   0x080488ac <+105>:   jle    0x804888f <isLib+76>
   0x080488ae <+107>:   cmp    DWORD PTR [ebp-0x8],0x0
   0x080488b2 <+111>:   je     0x80488be <isLib+123>
   0x080488b4 <+113>:   mov    eax,DWORD PTR [ebp-0x4]
   0x080488b7 <+116>:   movzx  eax,BYTE PTR [eax]
   0x080488ba <+119>:   cmp    al,0x2e
   0x080488bc <+121>:   je     0x80488c5 <isLib+130>
   0x080488be <+123>:   mov    eax,0x0
   0x080488c3 <+128>:   jmp    0x8048944 <isLib+257>
   0x080488c5 <+130>:   mov    DWORD PTR [ebp-0x8],0x0
   0x080488cc <+137>:   add    DWORD PTR [ebp-0x4],0x1
   0x080488d0 <+141>:   jmp    0x80488dd <isLib+154>
   0x080488d2 <+143>:   mov    DWORD PTR [ebp-0x8],0x1
   0x080488d9 <+150>:   add    DWORD PTR [ebp-0x4],0x1
   0x080488dd <+154>:   mov    eax,DWORD PTR [ebp-0x4]
   0x080488e0 <+157>:   movzx  eax,BYTE PTR [eax]
   0x080488e3 <+160>:   cmp    al,0x2f
   0x080488e5 <+162>:   jle    0x80488f1 <isLib+174>
   0x080488e7 <+164>:   mov    eax,DWORD PTR [ebp-0x4]
   0x080488ea <+167>:   movzx  eax,BYTE PTR [eax]
   0x080488ed <+170>:   cmp    al,0x39
   0x080488ef <+172>:   jle    0x80488d2 <isLib+143>
   0x080488f1 <+174>:   cmp    DWORD PTR [ebp-0x8],0x0
   0x080488f5 <+178>:   jne    0x80488fe <isLib+187>
   0x080488f7 <+180>:   mov    eax,0x0
   0x080488fc <+185>:   jmp    0x8048944 <isLib+257>
   0x080488fe <+187>:   mov    DWORD PTR [ebp-0xc],0x0
   0x08048905 <+194>:   jmp    0x804892d <isLib+234>
   0x08048907 <+196>:   mov    edx,DWORD PTR ds:0x804b038
   0x0804890d <+202>:   mov    eax,DWORD PTR [ebp-0xc]
   0x08048910 <+205>:   add    eax,edx
   0x08048912 <+207>:   movzx  edx,BYTE PTR [eax]
   0x08048915 <+210>:   mov    eax,DWORD PTR [ebp-0xc]
   0x08048918 <+213>:   add    eax,DWORD PTR [ebp-0x4]
   0x0804891b <+216>:   movzx  eax,BYTE PTR [eax]
   0x0804891e <+219>:   cmp    dl,al
   0x08048920 <+221>:   je     0x8048929 <isLib+230>
   0x08048922 <+223>:   mov    eax,0x0
   0x08048927 <+228>:   jmp    0x8048944 <isLib+257>
   0x08048929 <+230>:   add    DWORD PTR [ebp-0xc],0x1
   0x0804892d <+234>:   mov    edx,DWORD PTR ds:0x804b038
   0x08048933 <+240>:   mov    eax,DWORD PTR [ebp-0xc]
   0x08048936 <+243>:   add    eax,edx
   0x08048938 <+245>:   movzx  eax,BYTE PTR [eax]
   0x0804893b <+248>:   test   al,al
   0x0804893d <+250>:   jne    0x8048907 <isLib+196>
   0x0804893f <+252>:   mov    eax,0x1
   0x08048944 <+257>:   leave
   0x08048945 <+258>:   ret
End of assembler dump.
Dump of assembler code for function main:
   0x08048946 <+0>:     push   ebp
   0x08048947 <+1>:     mov    ebp,esp
   0x08048949 <+3>:     push   ebx
   0x0804894a <+4>:     and    esp,0xfffffff0
   0x0804894d <+7>:     sub    esp,0x120
   0x08048953 <+13>:    mov    eax,gs:0x14
   0x08048959 <+19>:    mov    DWORD PTR [esp+0x11c],eax
   0x08048960 <+26>:    xor    eax,eax
   0x08048962 <+28>:    mov    DWORD PTR [esp+0x10],0x0
   0x0804896a <+36>:    mov    DWORD PTR [esp+0xc],0x0
   0x08048972 <+44>:    mov    DWORD PTR [esp+0x8],0x1
   0x0804897a <+52>:    mov    DWORD PTR [esp+0x4],0x0
   0x08048982 <+60>:    mov    DWORD PTR [esp],0x0
   0x08048989 <+67>:    call   0x8048540 <ptrace@plt>
   0x0804898e <+72>:    test   eax,eax
   0x08048990 <+74>:    jns    0x80489a8 <main+98>
   0x08048992 <+76>:    mov    DWORD PTR [esp],0x8048fa8
   0x08048999 <+83>:    call   0x80484e0 <puts@plt>
   0x0804899e <+88>:    mov    eax,0x1
   0x080489a3 <+93>:    jmp    0x8048eb2 <main+1388>
   0x080489a8 <+98>:    mov    DWORD PTR [esp],0x8048fc4
   0x080489af <+105>:   call   0x80484d0 <getenv@plt>
   0x080489b4 <+110>:   test   eax,eax
   0x080489b6 <+112>:   je     0x80489ea <main+164>
   0x080489b8 <+114>:   mov    eax,ds:0x804b040
   0x080489bd <+119>:   mov    edx,eax
   0x080489bf <+121>:   mov    eax,0x8048fd0
   0x080489c4 <+126>:   mov    DWORD PTR [esp+0xc],edx
   0x080489c8 <+130>:   mov    DWORD PTR [esp+0x8],0x25
   0x080489d0 <+138>:   mov    DWORD PTR [esp+0x4],0x1
   0x080489d8 <+146>:   mov    DWORD PTR [esp],eax
   0x080489db <+149>:   call   0x80484c0 <fwrite@plt>
   0x080489e0 <+154>:   mov    eax,0x1
   0x080489e5 <+159>:   jmp    0x8048eb2 <main+1388>
   0x080489ea <+164>:   mov    DWORD PTR [esp+0x4],0x0
   0x080489f2 <+172>:   mov    DWORD PTR [esp],0x8048ff6
   0x080489f9 <+179>:   call   0x8048500 <open@plt>
   0x080489fe <+184>:   test   eax,eax
   0x08048a00 <+186>:   jle    0x8048a34 <main+238>
   0x08048a02 <+188>:   mov    eax,ds:0x804b040
   0x08048a07 <+193>:   mov    edx,eax
   0x08048a09 <+195>:   mov    eax,0x8048fd0
   0x08048a0e <+200>:   mov    DWORD PTR [esp+0xc],edx
   0x08048a12 <+204>:   mov    DWORD PTR [esp+0x8],0x25
   0x08048a1a <+212>:   mov    DWORD PTR [esp+0x4],0x1
   0x08048a22 <+220>:   mov    DWORD PTR [esp],eax
   0x08048a25 <+223>:   call   0x80484c0 <fwrite@plt>
   0x08048a2a <+228>:   mov    eax,0x1
   0x08048a2f <+233>:   jmp    0x8048eb2 <main+1388>
   0x08048a34 <+238>:   mov    DWORD PTR [esp+0x4],0x0
   0x08048a3c <+246>:   mov    DWORD PTR [esp],0x8049009
   0x08048a43 <+253>:   call   0x804871c <syscall_open>
   0x08048a48 <+258>:   mov    DWORD PTR [esp+0x14],eax
   0x08048a4c <+262>:   cmp    DWORD PTR [esp+0x14],0xffffffff
   0x08048a51 <+267>:   jne    0x8048e88 <main+1346>
   0x08048a57 <+273>:   mov    eax,ds:0x804b040
   0x08048a5c <+278>:   mov    edx,eax
   0x08048a5e <+280>:   mov    eax,0x804901c
   0x08048a63 <+285>:   mov    DWORD PTR [esp+0xc],edx
   0x08048a67 <+289>:   mov    DWORD PTR [esp+0x8],0x46
   0x08048a6f <+297>:   mov    DWORD PTR [esp+0x4],0x1
   0x08048a77 <+305>:   mov    DWORD PTR [esp],eax
   0x08048a7a <+308>:   call   0x80484c0 <fwrite@plt>
   0x08048a7f <+313>:   mov    eax,0x1
   0x08048a84 <+318>:   jmp    0x8048eb2 <main+1388>
   0x08048a89 <+323>:   mov    DWORD PTR [esp+0x4],0x8049063
   0x08048a91 <+331>:   lea    eax,[esp+0x1c]
   0x08048a95 <+335>:   mov    DWORD PTR [esp],eax
   0x08048a98 <+338>:   call   0x8048843 <isLib>
   0x08048a9d <+343>:   test   eax,eax
   0x08048a9f <+345>:   je     0x8048aae <main+360>
   0x08048aa1 <+347>:   mov    DWORD PTR [esp+0x10],0x1
   0x08048aa9 <+355>:   jmp    0x8048e89 <main+1347>
   0x08048aae <+360>:   cmp    DWORD PTR [esp+0x10],0x0
   0x08048ab3 <+365>:   je     0x8048e89 <main+1347>
   0x08048ab9 <+371>:   mov    DWORD PTR [esp+0x4],0x8049068
   0x08048ac1 <+379>:   lea    eax,[esp+0x1c]
   0x08048ac5 <+383>:   mov    DWORD PTR [esp],eax
   0x08048ac8 <+386>:   call   0x8048843 <isLib>
   0x08048acd <+391>:   test   eax,eax
   0x08048acf <+393>:   je     0x8048e46 <main+1280>
   0x08048ad5 <+399>:   mov    eax,ds:0x804b060
   0x08048ada <+404>:   mov    edx,eax
   0x08048adc <+406>:   mov    eax,0x804906c
   0x08048ae1 <+411>:   mov    DWORD PTR [esp+0xc],edx
   0x08048ae5 <+415>:   mov    DWORD PTR [esp+0x8],0x20
   0x08048aed <+423>:   mov    DWORD PTR [esp+0x4],0x1
   0x08048af5 <+431>:   mov    DWORD PTR [esp],eax
   0x08048af8 <+434>:   call   0x80484c0 <fwrite@plt>
   0x08048afd <+439>:   call   0x80484b0 <getuid@plt>
   0x08048b02 <+444>:   mov    DWORD PTR [esp+0x18],eax
   0x08048b06 <+448>:   mov    eax,DWORD PTR [esp+0x18]
   0x08048b0a <+452>:   cmp    eax,0xbbe
   0x08048b0f <+457>:   je     0x8048ccb <main+901>
   0x08048b15 <+463>:   cmp    eax,0xbbe
   0x08048b1a <+468>:   ja     0x8048b68 <main+546>
   0x08048b1c <+470>:   cmp    eax,0xbba
   0x08048b21 <+475>:   je     0x8048c3b <main+757>
   0x08048b27 <+481>:   cmp    eax,0xbba
   0x08048b2c <+486>:   ja     0x8048b4d <main+519>
   0x08048b2e <+488>:   cmp    eax,0xbb8
   0x08048b33 <+493>:   je     0x8048bf3 <main+685>
   0x08048b39 <+499>:   cmp    eax,0xbb8
   0x08048b3e <+504>:   ja     0x8048c17 <main+721>
   0x08048b44 <+510>:   test   eax,eax
   0x08048b46 <+512>:   je     0x8048bc6 <main+640>
   0x08048b48 <+514>:   jmp    0x8048e06 <main+1216>
   0x08048b4d <+519>:   cmp    eax,0xbbc
   0x08048b52 <+524>:   je     0x8048c83 <main+829>
   0x08048b58 <+530>:   cmp    eax,0xbbc
   0x08048b5d <+535>:   ja     0x8048ca7 <main+865>
   0x08048b63 <+541>:   jmp    0x8048c5f <main+793>
   0x08048b68 <+546>:   cmp    eax,0xbc2
   0x08048b6d <+551>:   je     0x8048d5b <main+1045>
   0x08048b73 <+557>:   cmp    eax,0xbc2
   0x08048b78 <+562>:   ja     0x8048b95 <main+591>
   0x08048b7a <+564>:   cmp    eax,0xbc0
   0x08048b7f <+569>:   je     0x8048d13 <main+973>
   0x08048b85 <+575>:   cmp    eax,0xbc0
   0x08048b8a <+580>:   ja     0x8048d37 <main+1009>
   0x08048b90 <+586>:   jmp    0x8048cef <main+937>
   0x08048b95 <+591>:   cmp    eax,0xbc4
   0x08048b9a <+596>:   je     0x8048da3 <main+1117>
   0x08048ba0 <+602>:   cmp    eax,0xbc4
   0x08048ba5 <+607>:   jb     0x8048d7f <main+1081>
   0x08048bab <+613>:   cmp    eax,0xbc5
   0x08048bb0 <+618>:   je     0x8048dc4 <main+1150>
   0x08048bb6 <+624>:   cmp    eax,0xbc6
   0x08048bbb <+629>:   je     0x8048de5 <main+1183>
   0x08048bc1 <+635>:   jmp    0x8048e06 <main+1216>
   0x08048bc6 <+640>:   mov    eax,ds:0x804b060
   0x08048bcb <+645>:   mov    edx,eax
   0x08048bcd <+647>:   mov    eax,0x8049090
   0x08048bd2 <+652>:   mov    DWORD PTR [esp+0xc],edx
   0x08048bd6 <+656>:   mov    DWORD PTR [esp+0x8],0x21
   0x08048bde <+664>:   mov    DWORD PTR [esp+0x4],0x1
   0x08048be6 <+672>:   mov    DWORD PTR [esp],eax
   0x08048be9 <+675>:   call   0x80484c0 <fwrite@plt>
   0x08048bee <+680>:   jmp    0x8048e2f <main+1257>
   0x08048bf3 <+685>:   mov    eax,ds:0x804b060
   0x08048bf8 <+690>:   mov    ebx,eax
   0x08048bfa <+692>:   mov    DWORD PTR [esp],0x80490b2
   0x08048c01 <+699>:   call   0x8048604 <ft_des>
   0x08048c06 <+704>:   mov    DWORD PTR [esp+0x4],ebx
   0x08048c0a <+708>:   mov    DWORD PTR [esp],eax
   0x08048c0d <+711>:   call   0x8048530 <fputs@plt>
   0x08048c12 <+716>:   jmp    0x8048e2f <main+1257>
   0x08048c17 <+721>:   mov    eax,ds:0x804b060
   0x08048c1c <+726>:   mov    ebx,eax
   0x08048c1e <+728>:   mov    DWORD PTR [esp],0x80490cc
   0x08048c25 <+735>:   call   0x8048604 <ft_des>
   0x08048c2a <+740>:   mov    DWORD PTR [esp+0x4],ebx
   0x08048c2e <+744>:   mov    DWORD PTR [esp],eax
   0x08048c31 <+747>:   call   0x8048530 <fputs@plt>
   0x08048c36 <+752>:   jmp    0x8048e2f <main+1257>
   0x08048c3b <+757>:   mov    eax,ds:0x804b060
   0x08048c40 <+762>:   mov    ebx,eax
   0x08048c42 <+764>:   mov    DWORD PTR [esp],0x80490e6
   0x08048c49 <+771>:   call   0x8048604 <ft_des>
   0x08048c4e <+776>:   mov    DWORD PTR [esp+0x4],ebx
   0x08048c52 <+780>:   mov    DWORD PTR [esp],eax
   0x08048c55 <+783>:   call   0x8048530 <fputs@plt>
   0x08048c5a <+788>:   jmp    0x8048e2f <main+1257>
   0x08048c5f <+793>:   mov    eax,ds:0x804b060
   0x08048c64 <+798>:   mov    ebx,eax
   0x08048c66 <+800>:   mov    DWORD PTR [esp],0x8049100
   0x08048c6d <+807>:   call   0x8048604 <ft_des>
   0x08048c72 <+812>:   mov    DWORD PTR [esp+0x4],ebx
   0x08048c76 <+816>:   mov    DWORD PTR [esp],eax
   0x08048c79 <+819>:   call   0x8048530 <fputs@plt>
   0x08048c7e <+824>:   jmp    0x8048e2f <main+1257>
   0x08048c83 <+829>:   mov    eax,ds:0x804b060
   0x08048c88 <+834>:   mov    ebx,eax
   0x08048c8a <+836>:   mov    DWORD PTR [esp],0x804911a
   0x08048c91 <+843>:   call   0x8048604 <ft_des>
   0x08048c96 <+848>:   mov    DWORD PTR [esp+0x4],ebx
   0x08048c9a <+852>:   mov    DWORD PTR [esp],eax
   0x08048c9d <+855>:   call   0x8048530 <fputs@plt>
   0x08048ca2 <+860>:   jmp    0x8048e2f <main+1257>
   0x08048ca7 <+865>:   mov    eax,ds:0x804b060
   0x08048cac <+870>:   mov    ebx,eax
   0x08048cae <+872>:   mov    DWORD PTR [esp],0x8049134
   0x08048cb5 <+879>:   call   0x8048604 <ft_des>
   0x08048cba <+884>:   mov    DWORD PTR [esp+0x4],ebx
   0x08048cbe <+888>:   mov    DWORD PTR [esp],eax
   0x08048cc1 <+891>:   call   0x8048530 <fputs@plt>
   0x08048cc6 <+896>:   jmp    0x8048e2f <main+1257>
   0x08048ccb <+901>:   mov    eax,ds:0x804b060
   0x08048cd0 <+906>:   mov    ebx,eax
   0x08048cd2 <+908>:   mov    DWORD PTR [esp],0x804914e
   0x08048cd9 <+915>:   call   0x8048604 <ft_des>
   0x08048cde <+920>:   mov    DWORD PTR [esp+0x4],ebx
   0x08048ce2 <+924>:   mov    DWORD PTR [esp],eax
   0x08048ce5 <+927>:   call   0x8048530 <fputs@plt>
   0x08048cea <+932>:   jmp    0x8048e2f <main+1257>
   0x08048cef <+937>:   mov    eax,ds:0x804b060
   0x08048cf4 <+942>:   mov    ebx,eax
   0x08048cf6 <+944>:   mov    DWORD PTR [esp],0x8049168
   0x08048cfd <+951>:   call   0x8048604 <ft_des>
   0x08048d02 <+956>:   mov    DWORD PTR [esp+0x4],ebx
   0x08048d06 <+960>:   mov    DWORD PTR [esp],eax
   0x08048d09 <+963>:   call   0x8048530 <fputs@plt>
   0x08048d0e <+968>:   jmp    0x8048e2f <main+1257>
   0x08048d13 <+973>:   mov    eax,ds:0x804b060
   0x08048d18 <+978>:   mov    ebx,eax
   0x08048d1a <+980>:   mov    DWORD PTR [esp],0x8049182
   0x08048d21 <+987>:   call   0x8048604 <ft_des>
   0x08048d26 <+992>:   mov    DWORD PTR [esp+0x4],ebx
   0x08048d2a <+996>:   mov    DWORD PTR [esp],eax
   0x08048d2d <+999>:   call   0x8048530 <fputs@plt>
   0x08048d32 <+1004>:  jmp    0x8048e2f <main+1257>
   0x08048d37 <+1009>:  mov    eax,ds:0x804b060
   0x08048d3c <+1014>:  mov    ebx,eax
   0x08048d3e <+1016>:  mov    DWORD PTR [esp],0x804919c
   0x08048d45 <+1023>:  call   0x8048604 <ft_des>
   0x08048d4a <+1028>:  mov    DWORD PTR [esp+0x4],ebx
   0x08048d4e <+1032>:  mov    DWORD PTR [esp],eax
   0x08048d51 <+1035>:  call   0x8048530 <fputs@plt>
   0x08048d56 <+1040>:  jmp    0x8048e2f <main+1257>
   0x08048d5b <+1045>:  mov    eax,ds:0x804b060
   0x08048d60 <+1050>:  mov    ebx,eax
   0x08048d62 <+1052>:  mov    DWORD PTR [esp],0x80491b6
   0x08048d69 <+1059>:  call   0x8048604 <ft_des>
   0x08048d6e <+1064>:  mov    DWORD PTR [esp+0x4],ebx
   0x08048d72 <+1068>:  mov    DWORD PTR [esp],eax
   0x08048d75 <+1071>:  call   0x8048530 <fputs@plt>
   0x08048d7a <+1076>:  jmp    0x8048e2f <main+1257>
   0x08048d7f <+1081>:  mov    eax,ds:0x804b060
   0x08048d84 <+1086>:  mov    ebx,eax
   0x08048d86 <+1088>:  mov    DWORD PTR [esp],0x80491d0
   0x08048d8d <+1095>:  call   0x8048604 <ft_des>
   0x08048d92 <+1100>:  mov    DWORD PTR [esp+0x4],ebx
   0x08048d96 <+1104>:  mov    DWORD PTR [esp],eax
   0x08048d99 <+1107>:  call   0x8048530 <fputs@plt>
   0x08048d9e <+1112>:  jmp    0x8048e2f <main+1257>
   0x08048da3 <+1117>:  mov    eax,ds:0x804b060
   0x08048da8 <+1122>:  mov    ebx,eax
   0x08048daa <+1124>:  mov    DWORD PTR [esp],0x80491ea
   0x08048db1 <+1131>:  call   0x8048604 <ft_des>
   0x08048db6 <+1136>:  mov    DWORD PTR [esp+0x4],ebx
   0x08048dba <+1140>:  mov    DWORD PTR [esp],eax
   0x08048dbd <+1143>:  call   0x8048530 <fputs@plt>
   0x08048dc2 <+1148>:  jmp    0x8048e2f <main+1257>
   0x08048dc4 <+1150>:  mov    eax,ds:0x804b060
   0x08048dc9 <+1155>:  mov    ebx,eax
   0x08048dcb <+1157>:  mov    DWORD PTR [esp],0x8049204
   0x08048dd2 <+1164>:  call   0x8048604 <ft_des>
   0x08048dd7 <+1169>:  mov    DWORD PTR [esp+0x4],ebx
   0x08048ddb <+1173>:  mov    DWORD PTR [esp],eax
   0x08048dde <+1176>:  call   0x8048530 <fputs@plt>
   0x08048de3 <+1181>:  jmp    0x8048e2f <main+1257>
   0x08048de5 <+1183>:  mov    eax,ds:0x804b060
   0x08048dea <+1188>:  mov    ebx,eax
   0x08048dec <+1190>:  mov    DWORD PTR [esp],0x8049220
   0x08048df3 <+1197>:  call   0x8048604 <ft_des>
   0x08048df8 <+1202>:  mov    DWORD PTR [esp+0x4],ebx
   0x08048dfc <+1206>:  mov    DWORD PTR [esp],eax
   0x08048dff <+1209>:  call   0x8048530 <fputs@plt>
   0x08048e04 <+1214>:  jmp    0x8048e2f <main+1257>
   0x08048e06 <+1216>:  mov    eax,ds:0x804b060
   0x08048e0b <+1221>:  mov    edx,eax
   0x08048e0d <+1223>:  mov    eax,0x8049248
   0x08048e12 <+1228>:  mov    DWORD PTR [esp+0xc],edx
   0x08048e16 <+1232>:  mov    DWORD PTR [esp+0x8],0x38
   0x08048e1e <+1240>:  mov    DWORD PTR [esp+0x4],0x1
   0x08048e26 <+1248>:  mov    DWORD PTR [esp],eax
   0x08048e29 <+1251>:  call   0x80484c0 <fwrite@plt>
   0x08048e2e <+1256>:  nop
   0x08048e2f <+1257>:  mov    eax,ds:0x804b060
   0x08048e34 <+1262>:  mov    DWORD PTR [esp+0x4],eax
   0x08048e38 <+1266>:  mov    DWORD PTR [esp],0xa
   0x08048e3f <+1273>:  call   0x8048520 <fputc@plt>
   0x08048e44 <+1278>:  jmp    0x8048ead <main+1383>
   0x08048e46 <+1280>:  mov    DWORD PTR [esp+0x4],0x8049281
   0x08048e4e <+1288>:  lea    eax,[esp+0x1c]
   0x08048e52 <+1292>:  mov    DWORD PTR [esp],eax
   0x08048e55 <+1295>:  call   0x80487be <afterSubstr>
   0x08048e5a <+1300>:  test   eax,eax
   0x08048e5c <+1302>:  jne    0x8048e89 <main+1347>
   0x08048e5e <+1304>:  mov    eax,ds:0x804b040
   0x08048e63 <+1309>:  mov    edx,eax
   0x08048e65 <+1311>:  mov    eax,0x8049294
   0x08048e6a <+1316>:  mov    DWORD PTR [esp+0xc],edx
   0x08048e6e <+1320>:  mov    DWORD PTR [esp+0x8],0x30
   0x08048e76 <+1328>:  mov    DWORD PTR [esp+0x4],0x1
   0x08048e7e <+1336>:  mov    DWORD PTR [esp],eax
   0x08048e81 <+1339>:  call   0x80484c0 <fwrite@plt>
   0x08048e86 <+1344>:  jmp    0x8048ead <main+1383>
   0x08048e88 <+1346>:  nop
   0x08048e89 <+1347>:  mov    eax,DWORD PTR [esp+0x14]
   0x08048e8d <+1351>:  mov    DWORD PTR [esp+0x8],eax
   0x08048e91 <+1355>:  mov    DWORD PTR [esp+0x4],0x100
   0x08048e99 <+1363>:  lea    eax,[esp+0x1c]
   0x08048e9d <+1367>:  mov    DWORD PTR [esp],eax
   0x08048ea0 <+1370>:  call   0x804874c <syscall_gets>
   0x08048ea5 <+1375>:  test   eax,eax
   0x08048ea7 <+1377>:  jne    0x8048a89 <main+323>
   0x08048ead <+1383>:  mov    eax,0x0
   0x08048eb2 <+1388>:  mov    edx,DWORD PTR [esp+0x11c]
   0x08048eb9 <+1395>:  xor    edx,DWORD PTR gs:0x14
   0x08048ec0 <+1402>:  je     0x8048ec7 <main+1409>
   0x08048ec2 <+1404>:  call   0x80484a0 <__stack_chk_fail@plt>
   0x08048ec7 <+1409>:  mov    ebx,DWORD PTR [ebp-0x4]
   0x08048eca <+1412>:  leave
   0x08048ecb <+1413>:  ret
End of assembler dump.
```
Massive yikes.

There appears to be a jump table at `<main+439>`, using the result of `getuid`.

We can check our current userid with the `id` command.
```bash
level14@SnowCrash:~$ id
uid=2014(level14) gid=2014(level14) groups=2014(level14),100(users)
```

However, since our target is the `flag14` account, the uid we'll be searching for is 3014 or 0xBC6
```asm
   0x08048bb6 <+624>:   cmp    eax,0xbc6
   0x08048bbb <+629>:   je     0x8048de5 <main+1183>
```

With our offset in hand, we can get the final flag.
```bash
level14@SnowCrash:~$ gdb -batch -ex 'file /bin/getflag' -ex 'b*main' -ex r -ex 'call ft_des(0x8049220)' -ex 'x/s$1'
level14@SnowCrash:~$ gdb -batch -ex 'file /bin/getflag' -ex 'b*main+67' -ex r -ex 'set $pc=*main+1183' -ex c
Breakpoint 1 at 0x8048989

Breakpoint 1, 0x08048989 in main ()
7QiHafiNa3HVozsaXkawuYrTstxbpABHD8CPnHJ
[Inferior 1 (process 22590) exited normally]
level14@SnowCrash:~$ su flag14
Password: 7QiHafiNa3HVozsaXkawuYrTstxbpABHD8CPnHJ
Congratulation. Type getflag to get the key and send it to me the owner of this livecd :)
flag14@SnowCrash:~$ getflag
Check flag.Here is your token : 7QiHafiNa3HVozsaXkawuYrTstxbpABHD8CPnHJ
flag14@SnowCrash:~$
```

### Reversing

Having already reversed the `ft_des` function from the previous level, which is the same function in the `getflag` binary, all we need is the encrypted string.

We can use `gdb` or `strings` to find it.
```bash
level14@SnowCrash:~$ gdb -batch -ex 'file /bin/getflag' -ex 'x/s 0x8049220'
0x8049220:       "g <t61:|4_|!@IF.-62FH&G~DCK/Ekrvvdwz?v|"
level14@SnowCrash:~$ strings /bin/getflag
...
PTRh@
QVhF
UWVS
[^_]
0123456
You should not reverse this
LD_PRELOAD
Injection Linked lib detected exit..
/etc/ld.so.preload
/proc/self/maps
/proc/self/maps is unaccessible, probably a LD_PRELOAD attempt exit..
libc
Check flag.Here is your token :
You are root are you that dumb ?
I`fA>_88eEd:=`85h0D8HE>,D
7`4Ci4=^d=J,?>i;6,7d416,7
<>B16\AD<C6,G_<1>^7ci>l4B
B8b:6,3fj7:,;bh>D@>8i:6@D
?4d@:,C>8C60G>8:h:Gb4?l,A
G8H.6,=4k5J0<cd/D@>>B:>:4
H8B8h_20B4J43><8>\ED<;j@3
78H:J4<4<9i_I4k0J^5>B1j`9
bci`mC{)jxkn<"uD~6%g7FK`7
Dc6m~;}f8Cj#xFkel;#&ycfbK
74H9D^3ed7k05445J0E4e;Da4
70hCi,E44Df[A4B/J@3f<=:`D
8_Dw"4#?+3i]q&;p6 gtw88EC
boe]!ai0FB@.:|L6l@A?>qJ}I
g <t61:|4_|!@IF.-62FH&G~DCK/Ekrvvdwz?v|
Nope there is no token here for you sorry. Try again :)
00000000 00:00 0
LD_PRELOAD detected through memory maps exit ..
;*2$"$
GCC: (Ubuntu/Linaro 4.6.3-1ubuntu5) 4.6.3
...
```
