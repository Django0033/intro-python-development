from PIL import Image

# Final Requirements
print()

# Background images variables
background_image_list = [ './img/beach.jpg',  './img/desert.jpg',  './img/sunset.jpg']
background_pick = int(input('\
Type the number of the background of your choice. 1.Beach 2.Desert 3.Sunset: '))
background_pick = background_image_list[background_pick - 1]
background_image = Image.open(background_pick)
background_pixels = background_image.load()

# Green sreen images variables
green_image_list = [ './img/boat.jpg',  './img/cactus.jpg',  './img/cat.jpg']
green_screen_pick = int(input('\
Type the number of the green screen image of your choice. 1.Boat 2.Cactus 3.Cat: '))
green_screen_pick = green_image_list[green_screen_pick - 1]
green_image = Image.open(green_screen_pick)
green_pixels = green_image.load()
(green_width, green_height) = green_image.size

for i in range(green_width):
    for j in range(green_height):
        r, g, b = green_pixels[i, j] 

        if r <= 140 and g >= 180 and b <= 120:
            green_pixels[i, j] = background_pixels[i, j]

green_image.show()
green_image.save('merged-image.jpg')
