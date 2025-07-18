import cv2

# 1. Load the image
img = cv2.imread('cat.jpg')
if img is None:
    print("Image not found. Make sure 'cat.jpg' is in the folder.")
    exit()

# 2. Draw a rectangle
cv2.rectangle(img, (50, 50), (200, 200), (0, 255, 0), 2)

# 3. Write text on the image
cv2.putText(img, 'Sample Text', (60, 45), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

# 4. Save this image
cv2.imwrite('image_with_text.jpg', img)

# 5. Convert to different color spaces
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite('gray.jpg', gray)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imwrite('hsv.jpg', hsv)

lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
cv2.imwrite('lab.jpg', lab)

# 6. Flip, Rotate, Crop
flipped = cv2.flip(img, 1)
cv2.imwrite('flipped.jpg', flipped)

(h, w) = img.shape[:2]
center = (w // 2, h // 2)
matrix = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated = cv2.warpAffine(img, matrix, (w, h))
cv2.imwrite('rotated.jpg', rotated)

cropped = img[50:200, 50:200]
cv2.imwrite('cropped.jpg', cropped)

# 7. Show the final image
cv2.imshow('Final Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()