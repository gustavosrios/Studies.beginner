from PIL import Image
image_example = Image.open('example.jpg')
type(image_example)
#image_example
#image_example.filename
#image_example.format_description
#image_example.size



#cropping images
from PIL import Image
image_example = Image.open('example.jpg')
halfway = 1993/2
x = halfway - 200
y = 800
w = halfway + 200
h = 1257
image_example.crop((x,y,w,h))


from PIL import Image
pencils = Image.open('pencils.jpg')
pencils
pencils.size


x = 0
y = 0
width = 1950 * 0.3 #30% do comprimento
height = 1300 * 0.1 #10% da altura
cropped_pencil02 = pencils.crop((x,y,width,height))
cropped_pencil02

x = 0
y = 0
width = 1950 * 0.3 #30% do comprimento
height = 1300 * 0.1 #10% da altura
cropped_pencil02 = pencils.crop((x,y,width,height))
cropped_pencil02

copy_pencil = pencils.crop((x,y,width,height))
pencils.paste(im=copy_pencil,box=(777,0))
pencils

#pencils.resize((2000,500)) # use ((width,height)) tuple
#pencils.rotate(90) #90 degrees 

from PIL import Image #word matrix size (1015,559)
word_matrix = Image.open('word_matrix.png')
mask = Image.open('mask.png')
mask.putalpha(50)
mask = mask.resize((1015,559))
#mask
#word_matrix
word_matrix.paste(mask,(0,0),mask)
word_matrix