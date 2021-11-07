from PIL import Image

image_original = Image.open('./img/beach.jpg') # Loading the img
original_pixels = image_original.load() # Getting pixels info
pixels = [original_pixels[100, 200], original_pixels[101, 200], original_pixels[102, 200],original_pixels[103, 200],original_pixels[104, 200]] # List of pixels to work with

image_original.show() # Opens a window to show an image

for pixel in pixels:
    r, g, b = pixel # Getting the RGB values for each pixel
    print(f'{r}, {g}, {b}') # Printing the RGB values

for x in range (100, 104):
    original_pixels[x, 200] = (255, 0, 255)

image_original.save('changed-pixels.jpg')
changed_pixels = Image.open('./changed-pixels.jpg')
changed_pixels.show()
