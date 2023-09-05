from PIL import Image
import numpy as np

# 打开图片并转换为 numpy 数组
img = Image.open(r"C:\Users\86159\Desktop\vuenii\src\assets\1.jpg")
data = np.array(img)

# 定义一个函数来检查像素是否接近（7，15，26）
def is_close(pixel):
    r, g, b = pixel[:3]
    return abs(r - 7) <= 20 and abs(g - 15) <= 20 and abs(b - 26) <= 20
print(np.where(data==[255,255,255]))
# 创建一个布尔数组来标记接近（7，15，26）的像素

for i in range(len(data)):
    for j in range(len(data[i])):
        if is_close(data[i][j]):
            data[i][j]=[255,255,255]

            

print(np.where(data==[255,255,255]))
# 将修改后的数据保存为新图片
new_img = Image.fromarray(data)
new_img.save(r"C:\Users\86159\Desktop\vuenii\src\assets\2.jpg")
