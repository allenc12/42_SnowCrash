# level02

Upon entering level02, we are greeted with a packet-capture file:
```bash
level02@SnowCrash:~$ ls
level02.pcap
level02@SnowCrash:~$ cp level02.pcap /tmp/
level02@SnowCrash:~$ chmod 777 /tmp/level02.pcap
```

Wireshark is the de-facto standard tool for creating, parsing and analyzing such files.
For scripting convenience purposes I used the command line interface `tshark`.
The `-z` flag displays the contents of a TCP or UDP stream between two nodes.
See the relevant documentation [here](https://www.wireshark.org/docs/man-pages/tshark.html#z-follow-prot-mode-filter-range)
```bash
root@kali:~$ scp level02@SnowCrash:/tmp/level02.pcap ./level02.pcap
root@kali:~$ tshark -z follow,tcp,raw,0,30-50 -r level02.pcap | gawk '$0~/^[[:xdigit:]]{2}$/{print$1}' | tr '\n' ' ' | xxd -r
t_wandrNDRel
root@kali:~$
```

Claim flag
```bash
level02@SnowCrash:~$ su flag02
Password: t_wandrNDRel
Don't forget to launch getflag !
flag02@SnowCrash:~$ getflag
Check flag.Here is your token : kooda2puivaav1idi4f57q8iq
flag02@SnowCrash:~$ su level03
Password: kooda2puivaav1idi4f57q8iq
level03@SnowCrash:~$
```
