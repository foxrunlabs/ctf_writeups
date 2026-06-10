#!/usr/bin/env python3

import cv2

image = cv2.imread('flag.png')
detector = cv2.QRCodeDetector()
data, _, _ = detector.detectAndDecode(image)

if data:
    print(f'Decoded data: {data}')
else:
    print('No QR code detected.')
