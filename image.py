from PIL import Image,ImageFilter

img = Image.open('./pokedex/astro.jpg')
img.thumbnail((400,400))
#new_img = img.resize((400,400))
img.save('thubnail.jpg')
print(img.size)
#filtered_img = img.filter(ImageFilter.SHARPEN)#1 method
#filtered_img = img.converet('L')#2nd method
#filtered_img.save('blur.png','png')
