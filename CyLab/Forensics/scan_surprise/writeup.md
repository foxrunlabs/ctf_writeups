# Scan Surprise
## Description
I've gotten bored of handing out flags as text. Wouldn't it be cool if they were an image instead?

You can download the challenge files here:
* [flag.png](flag.png)
## Hints
1. QR codes are a way of encoding data. While they're most known for storing URLs, they can store other things too.
2. Mobile phones have included native QR code scanners in their cameras since version 8 (Oreo) and iOS 11
3. If you don't have access to a phone, you can also use zbar-tools to convert an image to text
## Solution
The file `flag.png` is a photo of a QR code. Let’s use some Python to decode it from the command line.

```python
#!/usr/bin/env python3

import cv2

image = cv2.imread('flag.png')
detector = cv2.QRCodeDetector()
data, _, _ = detector.detectAndDecode(image)

if data:
    print(f'Decoded data: {data}')
else:
    print('No QR code detected.')
```

What do we find?

```console
% ./decode.py
Decoded data: picoCTF{p33k_@_b00_19eccd10}
```

The flag is revealed: `picoCTF{p33k_@_b00_19eccd10}`