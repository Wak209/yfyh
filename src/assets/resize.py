from PIL import Image
 
img = Image.open("src/assets/12.png")
 
print( img.size)
x = int(img.size[0]*(945/1570))
y = int(img.size[1]*(945/1570))
out = img.resize((x,y))
 
out.save("src/assets/new.png")
 
 