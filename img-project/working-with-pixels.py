from PIL import Image

image_original = Image.open('./img/beach.jpg') # Loading the img
pixels_original = image_original.load() # Getting pixels info
r1, g1, b1 = pixels_original[100, 200] # Getting RGB values
r2, g2, b2 = pixels_original[101, 200] 
r3, g3, b3 = pixels_original[101, 201] 
r4, g4, b4 = pixels_original[100, 201] 
r5, g5, b5 = pixels_original[99, 201] 

image_original.show() # Opens a window to show an image
print(f'{r1}, {g1}, {b1}')
print(f'{r2}, {g2}, {b2}')
print(f'{r3}, {g3}, {b3}')
print(f'{r4}, {g4}, {b4}')
print(f'{r5}, {g5}, {b5}')

pixels_original[100, 200] = (255, 0, 255) # Assigning new RGB values
pixels_original[101, 200] = (255, 0, 255)
pixels_original[101, 201] = (255, 0, 255)
pixels_original[100, 201] = (255, 0, 255)
pixels_original[99, 201] = (255, 0, 255) 

image_original.save('changed-pixels.jpg')
changed_pixels = Image.open('./changed-pixels.jpg')
changed_pixels.show()
