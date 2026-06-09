# Safe Opener 2
## Description
What can you do with this file?

I forgot the key to my safe but this [file](SafeOpener.class) is supposed to help me with retrieving the lost key. Can you help me unlock my safe?
## Hints
1. Download and try to decompile the file.
## Solution
Load the file into Ghidra. Take a look at the `openSafe` function.

```java
boolean openSafe_java.lang.String_boolean(String param1)
{
  PrintStream pPVar1;
  boolean bVar2;
  
  bVar2 = param1.equals("picoCTF{SAf3_0p3n3rr_y0u_solv3d_it_7db9fb8c}");
  if (bVar2 != false) {
    pPVar1 = System.out;
    pPVar1.println("Sesame open");
    return true;
  }
  pPVar1 = System.out;
  pPVar1.println("Password is incorrect\n");
  return false;
}
```

The flag is revealed: `picoCTF{SAf3_0p3n3rr_y0u_solv3d_it_7db9fb8c}`
