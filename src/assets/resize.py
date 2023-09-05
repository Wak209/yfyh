from PIL import Image

img = Image.open(r"C:\Users\86159\Desktop\vuenii\src\assets\wk.jpg")

print(img.size)

out = img.resize((200,300))
out.save(r"C:\Users\86159\Desktop\vuenii\src\assets\wkk.jpg")
