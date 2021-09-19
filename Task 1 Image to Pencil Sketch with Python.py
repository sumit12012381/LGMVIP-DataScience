
""" This program will convertes an image into  Grey image, inverted grey image, Blurred image of inverted grey image,
inverted (Blurred image of inverted grey image), Pencil Sketch"""

# Import the library
import cv2

# Get the image

original_image = cv2.imread("boy.jpg")

# Convert the original image to grey scale

grey_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

#Convert the grey image into inverted_grey_image

inverted_grey_image = 255 - grey_image

# Convert the inverted grey image into Blur the Image By Gaussiab Function

blurred_img = cv2.GaussianBlur(inverted_grey_image, (21,21), 0)

#Convert blured image into Inverted the blurred image

inverted_blurred_img = 255 - blurred_img

# Create the pencil sketch image by dividing grey image and inverted blurred image

pencil_sketch_img = cv2.divide(grey_image,inverted_blurred_img, scale=256.0)

#show the image after converting

cv2.imshow('Pencil sketch image', pencil_sketch_img )
cv2.imshow('Inverted Blured image', inverted_blurred_img)
cv2.imshow('Blured image', blurred_img)
cv2.imshow('Inverted image', inverted_grey_image)
cv2.imshow('Grey image', grey_image)
cv2.imshow('Original Image', original_image)
cv2.waitKey(0)