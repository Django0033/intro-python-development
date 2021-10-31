from PIL import Image

image_original = Image.open('./img/beach.jpg') # Loading the img
pixels_original = image_original.load() # Getting pixels info
pixels = [pixels_original[100, 200], pixels_original[101, 200], pixels_original[102, 200],pixels_original[103, 200],pixels_original[104, 200]] # List of pixels to work with
number_pixel = 0

image_original.show() # Opens a window to show an image

for pixel in pixels:
    r, g, b = pixel # Getting the RGB values for each pixel
    print(f'{r}, {g}, {b}') # Printing the RGB values

for x in range (100, 104):
    pixels_original[x, 200] = (255, 0, 255)

image_original.save('changed-pixels.jpg')
changed_pixels = Image.open('./changed-pixels.jpg')
changed_pixels.show()
