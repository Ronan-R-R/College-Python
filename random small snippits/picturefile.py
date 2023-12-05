import os
from PIL import Image

#Open the image file
SHORSE = Image.open("./SHORSE.PNG")

#resize an image
SHORSE = SHORSE.resize((1440,240))

#save the resized photo, name
SHORSE.save('resize.PNG')
SHORSE.show()