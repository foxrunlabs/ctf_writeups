# bytemancy 3
## Description
Can you conjure the right bytes? The program's source code can be downloaded [here](app.py) and the compiled spellbook binary can be downloaded [here](spellbook).
## Hints
1. `objdump -t spellbook` reveals the symbol table.
2. Send the addresses as 4 raw bytes in little-endian order.
3. `pwnlib.util.packing.p32()` simplifies crafting the payloads.
## Solution
The program asks for the 4-byte little endian address for different named procedures from the `spellbook` file.

```console
% python3 app.py
⊹──────[ BYTEMANCY-3 ]──────⊹
☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐

I will name four procedures hidden inside spellbook.
Each round, send me their *raw* 4-byte addresses in little-endian form. 3 correct answers unlock the flag.

☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐
⊹─────────────⟡─────────────⊹
[1/3] Send the 4-byte little-endian address for procedure 'ember_sigil'.
==> 
```

What is the `spellbook` file?

```console
% file spellbook
spellbook: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, BuildID[sha1]=0028c839fc5f43b51c9230d87125c038fdc9c6ce, for GNU/Linux 3.2.0, with debug_info, not stripped

% nm spellbook | awk '$2 == "T"'
080491c1 T astral_spark
080491e3 T binding_word
080490a0 T _dl_relocate_static_pie
08049176 T ember_sigil
0804930c T _fini
0804919a T glyph_conflux
08049000 T _init
08049300 T __libc_csu_fini
08049290 T __libc_csu_init
08049214 T main
08049060 T _start
08049287 T __x86.get_pc_thunk.ax
08049305 T __x86.get_pc_thunk.bp
080490b0 T __x86.get_pc_thunk.bx
```

This should be pretty easy for pwntools to handle.

```python
#!/usr/bin/env python3

from pwn import *

p = remote('green-hill.picoctf.net', 65193)
elf = ELF('spellbook', checksec=False)

for i in range(3):
    # Figure out which symbol to look up
    match = p.recvregex(br"Send the 4-byte little-endian address for procedure '(.+)'.\n", capture=True)
    symbol = match.group(1).decode()

    # Find the address and send it
    p.recvuntil(b'==> ')
    address = p32(elf.symbols[symbol])
    p.send(address)

    log.info(f'Symbol: {match.group(1).decode()} ({hex(elf.symbols[symbol])})')

flag = p.recvline().decode()
log.info(f'Flag: {flag}')

p.close()
```

Let’s give it a shot.

```console
% ./exploit.py
[+] Opening connection to green-hill.picoctf.net on port 65193: Done
[*] Symbol: glyph_conflux (0x804919a)
[*] Symbol: ember_sigil (0x8049176)
[*] Symbol: astral_spark (0x80491c1)
[*] Flag: picoCTF{0bjdump_m4g1c_bb59765a}
[*] Closed connection to green-hill.picoctf.net port 65193
```

## Flag
The flag is revealed: `picoCTF{0bjdump_m4g1c_bb59765a}`