# This is a simple code of a QR Code Generator Python script that can be run from the command line.
# Copyright (c) 2022 Vaibhav Ganeriwala

# import the qrcode module
import qrcode

qrcodeimg = qrcode.make(input("Enter the URL need to be converted to QR Code: "))
qrcodeimg.save("qrcode.jpg")
print("QR Code Generated Successfully!")
