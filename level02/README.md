# level02

Upon entering level02, we are greeted with a packet-capture file:
```bash
level02@SnowCrash:~ $ ls
level02.pcap
level02@SnowCrash:~ $ cp level02.pcap /tmp/
```

Wireshark is the de-facto standard tool for creating, parsing and analyzing such files.
For scripting convenience purposes I used the command line interface `tshark`
```bash
root@kali:~# scp level02@SnowCrash:/tmp/level02.pcap ./level02.pcap
#OUTPUT
root@kali:~# tshark -z follow,tcp,raw,0,30-50 -r level02.pcap | awk '$0 ~ /^[[:xdigit:]]$/ { print $1 }'
#OUTPUT
```

Claim flag
#TODO
