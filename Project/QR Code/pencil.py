import cv2

# reading image
image = cv2.imread("about.JPG")

# converting BGR image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# image inversion for enhacing detail
inverted_image = 255 - gray_image

# creating pencil sketch by mixing tha grayscale image with inverted blurry image.
blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
inverted_blurred = 255-blurred
pencil_sketch = cv2.divide(gray_image,inverted_blurred,scale=256)

# displaying image with opencv
cv2.imshow("Original Image",image)
# cv2.imshow("Pencil Sketch",pencil_sketch)
cv2.waitKey(0)
