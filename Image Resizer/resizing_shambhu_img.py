# Use this method to scale image proportionally

import cv2

# loading image
image = cv2.imread("shivJi.jpg")

# Desired width and height
new_width = 400
new_height = 200

# Calculating aspect_ratio
aspect_ratio = image.shape[1]/image.shape[0]

if (new_width/aspect_ratio) <= new_height:
    resized_image = cv2.resize(image, (new_width, int(new_width/aspect_ratio)))
else:
    resized_image = cv2.resize(image, (int(new_width*aspect_ratio), new_height))

cv2.imshow("Shiva", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


