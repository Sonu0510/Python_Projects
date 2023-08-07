# Use this method to scale image as you want

import cv2

# Loads image
image = cv2.imread("yugen.jpg")

# Specifying new width and new height
new_width = 720
new_height = 600

# Resizing image : assigning new_width and new_height
resized_image = cv2.resize(image, (new_width, new_height))

cv2.imshow("Yugen", resized_image)
cv2.waitKey(0)  # to allow the window to remain open until you press any key
cv2.destroyAllWindows()  # press any key to clean up and close any open windows when you're done displaying images
