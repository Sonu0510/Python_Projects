# Using scaling factor to resize image

import cv2

image = cv2.imread("shivJi.jpg")
scaling_factor = 1.5
# Calculating new_height and new_width based on scaling factor
new_width = int(image.shape[1] * scaling_factor)
new_height = int(image.shape[0] * scaling_factor)

resized_image = cv2.resize(image, (new_width, new_height))

cv2.imshow("ShivJi", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()



