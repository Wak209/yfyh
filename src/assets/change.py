from PIL import Image
import numpy as np

# 打开原始图片
image = Image.open(r"C:\Users\86159\Desktop\vuenii\src\assets\login1.jpg")

# 将 PIL.Image 转换为 numpy 数组
image_np = np.array(image)

# 计算需要填充的边距
top = 0
bottom = 960 - image_np.shape[0]
left = 0
right = 1920 - image_np.shape[1]

# 填充图片
new_image_np = np.pad(image_np, ((top, bottom), (left, right), (0, 0)), mode='edge')

# 将 numpy 数组转换为 PIL.Image
new_image = Image.fromarray(new_image_np)

# 保存新图片
new_image.save(r"C:\Users\86159\Desktop\vuenii\src\assets\login2.jpg")
