# -*- coding: utf-8 -*-
"""
Created on Wed May 16 11:50:46 2018

@author: JITESH
"""


from PIL import Image


op_image=Image.open('sample.jpg').convert('L')


op_image.size

op_image=op_image.transpose(Image.ROTATE_270)

op_image.size
#op_image=op_image.convert('1')




width,height=op_image.size

left = (width - 160)/2
top = (height - 204)/2
right = (width + 160)/2
bottom = (height + 204)/2

op_image=op_image.crop((left, top, right, bottom))
op_image.show()

op_image.thumbnail((75,75))

op_image.save('thumbnail.jpg', 'JPEG')
op_image.show()
