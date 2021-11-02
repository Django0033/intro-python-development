from PIL import Image

# image_original = Image.open('./img/beach.jpg') # Loading the img
# original_pixels = image_original.load() # Getting pixels info
# pixels = [original_pixels[100, 200], original_pixels[101, 200], original_pixels[102, 200],original_pixels[103, 200],original_pixels[104, 200]] # List of pixels to work with

# image_original.show() # Opens a window to show an image

# for pixel in pixels:
#     r, g, b = pixel # Getting the RGB values for each pixel
#     print(f'{r}, {g}, {b}') # Printing the RGB values

# for x in range (100, 104):
#     original_pixels[x, 200] = (255, 0, 255)

# image_original.save('changed-pixels.jpg')
# changed_pixels = Image.open('./changed-pixels.jpg')
# changed_pixels.show()

# Final Requirements

# Background image variables
background_image = Image.open('./img/beach.jpg')
background_pixels = background_image.load()

# Green image variables
green_image = Image.open('./img/cactus.jpg')
green_pixels = green_image.load()
(green_width, green_height) = green_image.size

r, g, b = green_pixels[0, 0] 

print(r, g, b)

for i in range(green_width):
    for j in range(green_height):
        r, g, b = green_pixels[i, j] 

        if r <= 150 and g >= 200 and b <= 150:
            green_pixels[i, j] = background_pixels[i, j]

green_image.save('merged-image.jpg')
