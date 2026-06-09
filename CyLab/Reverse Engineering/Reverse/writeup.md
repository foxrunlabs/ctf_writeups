# Reverse
## Description
Try reversing this file? Can ya?  
I forgot the password to this [file](ret). Please find it for me?
## Hints
(None)
## Solution
What type of file is `ret`?

```console
% file ret
ret: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=32195c65c0c8ca5bd239fa824d4d79231cca5f78, for GNU/Linux 3.2.0, not stripped
```

It's an executable. Let's check for any obvious strings.

```console
% strings ret
Enter the password to unlock this file: 
You entered: %s
Password correct, please see flag: picoCTF{3lf_r3v3r5ing_succe55ful_c83965de}
Access denied
:*3$"
GCC: (Ubuntu 9.4.0-1ubuntu1~20.04.1) 9.4.0
crtstuff.c
deregister_tm_clones
__do_global_dtors_aux
completed.8061
```

The flag is revealed: `picoCTF{3lf_r3v3r5ing_succe55ful_c83965de}`
