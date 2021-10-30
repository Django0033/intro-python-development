# This line imports or includes the library we will need
from PIL import Image

# This line opens the image and loads it into a variable called 'image_original'
image_original = Image.open('./img/beach.jpg')

#This line attempts to open a new window to display the image.
image_original.show()

# You should run this program at the same folder where it lies to see it works
