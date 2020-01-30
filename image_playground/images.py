from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')
# filtered_img = img.filter(ImageFilter.BLUR)
# filtered_img = img.filter(ImageFilter.SMOOTH)
# filtered_img = img.filter(ImageFilter.SHARPEN)
filtered_img = img.convert('L')
# filtered_img.save('grey.png', 'png')
# filtered_img.show()
# filtered_img.rotate(90)
# crooked = filtered_img.rotate(180)
# crooked.save('grey.png', 'png')
# resize = filtered_img.resize((300, 300))
# resize.save('grey.png', 'png')

# crop image
box = (100, 100, 400, 400)
region = filtered_img.crop(box)
region.save('grey.png', 'png')

# print(img)
# print(img.format)
# print(img.size)
# print(img.mode)
# print(dir(img))
