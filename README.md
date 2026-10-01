# CTF Challenge Writeups

A hands-on cybersecurity learning portfolio built around capture-the-flag challenges from **CyLab** (formerly picoCTF) and **CTFlearn**. These writeups document how I investigate unfamiliar programs, identify vulnerable behavior, and turn observations into working challenge solutions.

The main focus is **binary exploitation and reverse engineering**, supported by Linux command-line work, Python scripting, and file analysis. The repository spans introductory exercises and more involved investigations of format strings, position-independent executables, and heap behavior. It reflects practical learning in controlled CTF environments.

## Start here

For a quick look at the analysis and scripting in this repository:

| Writeup | What it demonstrates |
| --- | --- |
| [Echo Valley](cylab/binary_exploitation/echo_valley/writeup.md) | Investigating a format string vulnerability, leaking stack addresses, and using pwntools to overwrite a saved return address. Includes a breakdown of the generated payload. |
| [format string 3](cylab/binary_exploitation/format_string_3/writeup.md) | Using a libc address leak and a writable Global Offset Table entry to redirect `puts()` to `system()`. Includes a Python exploit. |
| [Cache Me Outside](cylab/binary_exploitation/cache_me_outside/writeup.md) | Examining glibc tcache state with GDB/GEF, matching the challenge's runtime, and tracing the effect of a single-byte heap modification. |
| [keygenme](cylab/reverse_engineering/keygenme/writeup.md) | Combining Ghidra decompilation with GDB breakpoints and memory inspection to recover a license key from a stripped binary. |
| [ARMssembly 3](cylab/reverse_engineering/armssembly_3/writeup.md) | Translating ARM assembly into C and simplifying the logic into a bit-counting operation. |
| [StegoRSA](cylab/general_skills/stegorsa/writeup.md) | Recovering a hex-encoded RSA private key from image metadata and decrypting the challenge message with OpenSSL. |
| [bytemancy 3](cylab/general_skills/bytemancy_3/writeup.md) | Automating ELF symbol lookup and sending correctly packed little-endian addresses with pwntools. |
| [Favorite Color](ctflearn/binary/favorite_color/writeup.md) | Reading x86 disassembly, calculating a stack overflow offset, and redirecting execution past a failed check. |

## Repository guide

Challenges are grouped by platform, then category.

| Location | Coverage |
| --- | --- |
| [cylab/binary_exploitation/](cylab/binary_exploitation/) | Stack and heap overflows, return-address and function-pointer control, format string reads and writes, PIE address calculations, filtered shellcode, and use-after-free. |
| [cylab/reverse_engineering/](cylab/reverse_engineering/) | x86 and ARM assembly, decompilation, debugger-assisted analysis, Java password checks, Python obfuscation, binary comparison, and UPX unpacking. |
| [cylab/general_skills/](cylab/general_skills/) | Shell navigation and pipelines, encodings, Python debugging, dictionary-based password checks, integer overflow, command injection, session cookie manipulation, and metadata-assisted RSA key recovery. |
| [cylab/forensics/](cylab/forensics/) | Image metadata, QR decoding, and a challenge involving restricted-shell behavior and `PATH` manipulation. |
| [ctflearn/binary/](ctflearn/binary/) | Buffer overflows, control-flow redirection, and an input-validation flaw in a betting game. |

Categories follow the existing repository organization, so some techniques cross category boundaries.

Within a challenge directory, start with `writeup.md`. Supporting material varies: some folders include challenge source code, binaries, encrypted files, shared libraries, or separate solution scripts. Many writeups keep their scripts directly in Markdown code blocks.

## Skills practiced

- **Program analysis:** connect source code and disassembly to runtime behavior; inspect registers, stack frames, memory, symbols, and comparison routines.
- **Exploit development in CTF labs:** calculate offsets, account for byte order and calling conventions, identify address leaks, and construct targeted payloads.
- **Automation:** use Python and pwntools to interact with challenge services, decode leaked data, resolve symbols, and generate format string payloads.
- **Linux and data investigation:** combine shell tools, file inspection, metadata extraction, and encoding conversions to test a hypothesis.
- **Technical communication:** explain the vulnerable behavior and solution with commands, code, debugger output, and, where useful, memory-layout tables.

The writeups range from short command-line solutions to detailed investigations. Together, they show practice moving from an initial clue to a testable explanation and a documented result.

## Tools used

Tools used in the documented solutions include:

- **Analysis and debugging:** GDB, GEF, Ghidra, `objdump`, `nm`, and `checksec`.
- **Scripting and payloads:** Python, pwntools, shell scripting, and NASM.
- **File and data inspection:** `file`, `strings`, `grep`, `find`, `xxd`, ExifTool, CyberChef, OpenSSL, and OpenCV.
- **Challenge interaction and runtime preparation:** Netcat, SSH, UPX, and `patchelf`.

## Reading and reproduction

**Spoilers:** the writeups contain complete solutions, payloads, and flags.

Each writeup records a particular challenge instance and environment. Remote hosts and ports may have changed, and some scripts contain fixed connection details or runtime-specific offsets. Linux ELF binaries may require the appropriate architecture, loader, and libc; individual Python scripts also have their own dependencies. Follow the relevant writeup and check its assumptions when reproducing a solution.

Use the included vulnerable programs and payloads in an isolated lab or an authorized CTF environment.

Challenge descriptions and supplied artifacts belong to their respective creators. This repository collects my solution notes and supporting work for learning and portfolio review.
