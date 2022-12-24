# import qrcode

# img = qrcode.make("https://www.youtube.com")
# img.save("youtubeQR.jpg")

# img = qrcode.make("India is a country with many religious.")
# img.save("youtubeQR.jpg")

"""OpenCV is library of programming functions focused on reak time computer vision tasks."""
# Code to decode a QR code back to know the original string
import cv2
d = cv2.QRCodeDetector()
val, _, _ = d.detectAndDecode(cv2.imread("youtubeQR.jpg"))
print("Decoded text is: ", val)