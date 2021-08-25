import imageio
import os

imagess = []
for filename in os.listdir('images'):
    image = imageio.imread(f'images/{filename}')
    imagess.append(image)

imageio.mimsave('fun.gif' , imagess)