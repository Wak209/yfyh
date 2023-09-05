import nibabel as nib
import numpy as np
import matplotlib.pyplot as plt
import cv2
def mainpic(filepath,x,y,z,mode_str):
# 定义显示图像的大小
    height_show, width_show = 400, 400
    img = nib.load(filepath)    # 中间切片预览
    data = img.get_fdata()
    print(data.shape)

    # 输入坐标
    #coord_str = input("请输入坐标(x,y,z): ")
    # 分割字符串并转换为浮点数
    #x, y, z = map(float, coord_str.strip('()').split(','))
    # 输出坐标
    '''print("x = ", x)
    print("y = ", y)
    print("z = ", z)'''

    # 输入图像处理方式
    #mode_str = input("请输入图像处理方法: ")
    print(x,y,z)
    # 将数据转换为灰度图像（2D）
    pic_z = data[:,int(x),:]
    pic_c = data[int(y),:,:]
    pic_f = data[:,:,int(z)]
    
    # 原始图像的尺寸
    height, width = data.shape[0], data.shape[2]
    # 定义变换前后的四个点坐标
    src_points = np.float32([[0, 0], [width - 1, 0], [0, height - 1]])
    dst_points = np.float32([[0, 0], [height - 1, 0], [0, height - 1]])
    # 计算仿射变换矩阵
    affine_matrix = cv2.getAffineTransform(src_points, dst_points)
    # 进行仿射变换
    transformed_image_z = cv2.warpAffine(pic_z, affine_matrix, (data.shape[0], data.shape[0]))
    transformed_image_z = transformed_image_z.astype(np.uint8)
    transformed_image_z_rgb = cv2.cvtColor(transformed_image_z, cv2.COLOR_BGR2RGB)
    transformed_image_c = cv2.warpAffine(pic_c, affine_matrix, (data.shape[0], data.shape[0]))
    transformed_image_c = transformed_image_c.astype(np.uint8)
    transformed_image_c_rgb = cv2.cvtColor(transformed_image_c, cv2.COLOR_BGR2RGB)
    transformed_image_f = pic_f.astype(np.uint8)
    transformed_image_f_rgb = cv2.cvtColor(transformed_image_f, cv2.COLOR_BGR2RGB)
    if mode_str == "0":
        plt.figure("三维显示")
        plt.rcParams['figure.figsize']=(20, 20)
        plt.subplot(1,3,1)
        transformed_image_z_rgb=cv2.resize(transformed_image_z_rgb,(height_show, width_show))
        plt.imshow(transformed_image_z_rgb)
        plt.axis('off')
        plt.subplot(1,3,2)
        transformed_image_c_rgb=cv2.resize(transformed_image_c_rgb,(height_show, width_show))
        plt.imshow(transformed_image_c_rgb)
        plt.axis('off')
        plt.subplot(1,3,3)
        transformed_image_f_rgb=cv2.resize(transformed_image_f_rgb,(height_show, width_show))
        plt.imshow(transformed_image_f_rgb)
        plt.axis('off')
        #plt.show()
        cv2.imwrite(r"C:\Users\86159\Desktop\vuenii\public\15972129987\before\1.jpg",transformed_image_z_rgb)
        cv2.imwrite(r"C:\Users\86159\Desktop\vuenii\public\15972129987\before\2.jpg",transformed_image_c_rgb)
        cv2.imwrite(r"C:\Users\86159\Desktop\vuenii\public\15972129987\before\3.jpg",transformed_image_f_rgb)
        plt.clf()
    # 将数据转换为灰度图像（2D）
    gray_data = np.squeeze(np.mean(data, axis=-1))
    gray = gray_data.astype(np.uint8)
    gray = np.clip(gray, a_min=0, a_max=255)
    grayf = gray_data.astype(np.float32)
    grayf = np.clip(grayf, a_min=0, a_max=255)
    gray_rgb = cv2.cvtColor(gray, cv2.COLOR_BGR2RGB)

    ### 1.腐蚀膨胀
    if mode_str == "1":
        # 定义膨胀和腐蚀的核大小和迭代次数
        dilation_kernel_size = (2, 2)
        erosion_kernel_size = (2, 2)
        iterations = 2
        # 创建膨胀和腐蚀的核
        dilation_kernel = np.ones(dilation_kernel_size, np.uint8)
        erosion_kernel = np.ones(erosion_kernel_size, np.uint8)
        # 对角点图像进行膨胀操作，以便更好地显示角点
        gray_d = cv2.erode(gray, erosion_kernel, iterations=iterations)
        gray_d = cv2.dilate(gray_d, dilation_kernel, iterations=iterations)
        gray_d_rgb = cv2.cvtColor(gray_d, cv2.COLOR_BGR2RGB)

        transformed_image_d_z = cv2.erode(transformed_image_z, erosion_kernel, iterations=iterations)
        transformed_image_d_z = cv2.dilate(transformed_image_d_z, dilation_kernel, iterations=iterations)
        transformed_image_d_z_rgb = cv2.cvtColor(transformed_image_d_z, cv2.COLOR_BGR2RGB)

        transformed_image_d_c = cv2.erode(transformed_image_c, erosion_kernel, iterations=iterations)
        transformed_image_d_c = cv2.dilate(transformed_image_d_c, dilation_kernel, iterations=iterations)
        transformed_image_d_c_rgb = cv2.cvtColor(transformed_image_d_c, cv2.COLOR_BGR2RGB)

        transformed_image_d_f = cv2.erode(transformed_image_f, erosion_kernel, iterations=iterations)
        transformed_image_d_f = cv2.dilate(transformed_image_d_f, dilation_kernel, iterations=iterations)
        transformed_image_d_f_rgb = cv2.cvtColor(transformed_image_d_f, cv2.COLOR_BGR2RGB)

        plt.figure("腐蚀膨胀")
        plt.subplot(1,3,1)
        transformed_image_d_z_rgb=cv2.resize(transformed_image_d_z_rgb,(height_show, width_show))
        plt.imshow(transformed_image_d_z_rgb)
        plt.axis('off')
        plt.subplot(1,3,2)
        transformed_image_d_c_rgb=cv2.resize(transformed_image_d_c_rgb,(height_show, width_show))
        plt.imshow(transformed_image_d_c_rgb)
        plt.axis('off')
        plt.subplot(1,3,3)
        transformed_image_d_f_rgb=cv2.resize(transformed_image_d_f_rgb,(height_show, width_show))
        plt.imshow(transformed_image_d_f_rgb)
        plt.axis('off')
        #plt.show()
        cv2.imwrite(r"C:\Users\86159\Desktop\vuenii\public\15972129987\before\1.jpg",transformed_image_d_z_rgb)
        cv2.imwrite(r"C:\Users\86159\Desktop\vuenii\public\15972129987\before\2.jpg",transformed_image_d_c_rgb)
        cv2.imwrite(r"C:\Users\86159\Desktop\vuenii\public\15972129987\before\3.jpg",transformed_image_d_f_rgb)
        plt.clf()

    ### 2.直方图均衡化
    if mode_str == "2":
        gray_e = cv2.equalizeHist(gray)
        gray_e_rgb = cv2.cvtColor(gray_e, cv2.COLOR_BGR2RGB)

        transformed_image_e_z = cv2.equalizeHist(transformed_image_z)
        transformed_image_e_z_rgb = cv2.cvtColor(transformed_image_e_z, cv2.COLOR_BGR2RGB)

        transformed_image_e_c = cv2.equalizeHist(transformed_image_c)
        transformed_image_e_c_rgb = cv2.cvtColor(transformed_image_e_c, cv2.COLOR_BGR2RGB)

        transformed_image_e_f = cv2.equalizeHist(transformed_image_f)
        transformed_image_e_f_rgb = cv2.cvtColor(transformed_image_e_f, cv2.COLOR_BGR2RGB)

        plt.figure("直方图均衡化")
        plt.subplot(1,3,1)
        transformed_image_e_z_rgb=cv2.resize(transformed_image_e_z_rgb,(height_show, width_show))
        plt.imshow(transformed_image_e_z_rgb)
        plt.axis('off')
        plt.subplot(1,3,2)
        transformed_image_e_c_rgb=cv2.resize(transformed_image_e_c_rgb,(height_show, width_show))
        plt.imshow(transformed_image_e_c_rgb)
        plt.axis('off')
        plt.subplot(1,3,3)
        transformed_image_e_f_rgb=cv2.resize(transformed_image_e_f_rgb,(height_show, width_show))
        plt.imshow(transformed_image_e_f_rgb)
        plt.axis('off')
        #plt.show()
        cv2.imwrite(r"C:\Users\86159\Desktop\vuenii\public\15972129987\before\1.jpg",transformed_image_e_z_rgb)
        cv2.imwrite(r"C:\Users\86159\Desktop\vuenii\public\15972129987\before\2.jpg",transformed_image_e_c_rgb)
        cv2.imwrite(r"C:\Users\86159\Desktop\vuenii\public\15972129987\before\3.jpg",transformed_image_e_f_rgb)
        plt.clf()

    ### 3.锐化滤波
    if mode_str == "3":
        def dft_shift(image):
            # 傅立叶变化
            src_dft = cv2.dft(np.float32(image), flags=cv2.DFT_COMPLEX_OUTPUT)
            # 将图片中心从左上角移到中心
            src_dft_shift = np.fft.fftshift(src_dft)

            # 制作掩膜令中心为0,后面才能过滤掉中心低频
            rows, cols = image.shape
            crow, ccol = int(rows / 2), int(cols / 2)
            mask = np.ones((rows, cols, 2), np.uint8)
            mask[crow - 10:crow + 10, ccol - 10:ccol + 10] = 0

            # 用掩膜对图像进行处理
            src_dft_shift_over = src_dft_shift * mask

            # 将中心移回左上角
            src_dft_shift_over_ishift = np.fft.ifftshift(src_dft_shift_over)

            # 傅立叶逆变换
            src_dft_shift_over_ishift_idft = cv2.idft(src_dft_shift_over_ishift)

            # 后续操作,将矢量转换成标量,并映射到合理范围之内
            src_dft_shift_over_ishift_idft = cv2.magnitude(src_dft_shift_over_ishift_idft[:, :, 0],
                                                        src_dft_shift_over_ishift_idft[:, :, 1])
            src_dft_shift_over_ishift_idft = np.abs(src_dft_shift_over_ishift_idft)
            src_dft_shift_over_ishift_idft = (src_dft_shift_over_ishift_idft - np.amin(src_dft_shift_over_ishift_idft)) / (
                        np.amax(src_dft_shift_over_ishift_idft) - np.amin(src_dft_shift_over_ishift_idft))

            src_dft_shift_over_ishift_idft_rgb = cv2.cvtColor(src_dft_shift_over_ishift_idft, cv2.COLOR_BGR2RGB)
            return src_dft_shift_over_ishift_idft_rgb


        gray_f = dft_shift(gray)
        gray_f_rgb = cv2.cvtColor(gray_f, cv2.COLOR_BGR2RGB)
        gray_f *= 255.0

        transformed_image_f_z = dft_shift(transformed_image_z)
        transformed_image_f_z_rgb = cv2.cvtColor(transformed_image_f_z, cv2.COLOR_BGR2RGB)
        transformed_image_f_z *= 255.0

        transformed_image_f_c = dft_shift(transformed_image_c)
        transformed_image_f_c_rgb = cv2.cvtColor(transformed_image_f_c, cv2.COLOR_BGR2RGB)
        transformed_image_f_c *= 255.0

        transformed_image_f_f = dft_shift(transformed_image_f)
        transformed_image_f_f_rgb = cv2.cvtColor(transformed_image_f_f, cv2.COLOR_BGR2RGB)
        transformed_image_f_f *= 255.0

        plt.figure("锐化滤波")
        plt.subplot(1, 3, 1)
        transformed_image_f_z_rgb=cv2.resize(transformed_image_f_z_rgb,(height_show, width_show))
        plt.imshow(transformed_image_f_z_rgb)
        plt.axis('off')
        plt.subplot(1, 3, 2)
        transformed_image_f_c_rgb=cv2.resize(transformed_image_f_c_rgb,(height_show, width_show))
        plt.imshow(transformed_image_f_c_rgb)
        plt.axis('off')
        plt.subplot(1, 3, 3)
        transformed_image_f_f_rgb=cv2.resize(transformed_image_f_f_rgb,(height_show, width_show))
        plt.imshow(transformed_image_f_f_rgb)
        plt.axis('off')
        #plt.show()
        plt.imsave(r"C:\Users\86159\Desktop\vuenii\public\15972129987\before\1.jpg",transformed_image_f_z_rgb)
        plt.imsave(r"C:\Users\86159\Desktop\vuenii\public\15972129987\before\2.jpg",transformed_image_f_c_rgb)
        plt.imsave(r"C:\Users\86159\Desktop\vuenii\public\15972129987\before\3.jpg",transformed_image_f_f_rgb)
        plt.clf()




    ### 4.平滑滤波
    if mode_str == "4":

        gray_g = cv2.GaussianBlur(gray, ksize=(3,3), sigmaX=1.3)
        gray_g_rgb = cv2.cvtColor(gray_g, cv2.COLOR_BGR2RGB)

        transformed_image_g_z = cv2.GaussianBlur(transformed_image_z, ksize=(3,3), sigmaX=1.3)
        transformed_image_g_z_rgb = cv2.cvtColor(transformed_image_g_z, cv2.COLOR_BGR2RGB)

        transformed_image_g_c =cv2.GaussianBlur(transformed_image_c, ksize=(3,3), sigmaX=1.3)
        transformed_image_g_c_rgb = cv2.cvtColor(transformed_image_g_c, cv2.COLOR_BGR2RGB)

        transformed_image_g_f = cv2.GaussianBlur(transformed_image_f, ksize=(3,3), sigmaX=1.3)
        transformed_image_g_f_rgb = cv2.cvtColor(transformed_image_g_f, cv2.COLOR_BGR2RGB)

        plt.figure("平滑滤波")
        plt.subplot(1, 3, 1)
        transformed_image_g_z_rgb=cv2.resize(transformed_image_g_z_rgb,(height_show, width_show))
        plt.imshow(transformed_image_g_z_rgb)
        plt.axis('off')
        plt.subplot(1, 3, 2)
        transformed_image_g_c_rgb=cv2.resize(transformed_image_g_c_rgb,(height_show, width_show))
        plt.imshow(transformed_image_g_c_rgb)
        plt.axis('off')
        plt.subplot(1, 3, 3)
        transformed_image_g_f_rgb=cv2.resize(transformed_image_g_f_rgb,(height_show, width_show))
        plt.imshow(transformed_image_g_f_rgb)
        plt.axis('off')
        #plt.show()
        cv2.imwrite(r"C:\Users\86159\Desktop\vuenii\public\15972129987\before\1.jpg",transformed_image_g_z_rgb)
        cv2.imwrite(r"C:\Users\86159\Desktop\vuenii\public\15972129987\before\2.jpg",transformed_image_g_c_rgb)
        cv2.imwrite(r"C:\Users\86159\Desktop\vuenii\public\15972129987\before\3.jpg",transformed_image_g_f_rgb)
        plt.clf()


    ### 5.边缘检测
    # 腐蚀膨胀预处理
    if mode_str == "5":
        edges_transformed_image_z = cv2.Canny(transformed_image_z, 100, 200)
        edges_transformed_image_z_rgb = cv2.cvtColor(edges_transformed_image_z, cv2.COLOR_BGR2RGB)
        edges_transformed_image_c = cv2.Canny(transformed_image_c, 100, 200)
        edges_transformed_image_c_rgb = cv2.cvtColor(edges_transformed_image_c, cv2.COLOR_BGR2RGB)
        edges_transformed_image_f = cv2.Canny(transformed_image_f, 100, 200)
        edges_transformed_image_f_rgb = cv2.cvtColor(edges_transformed_image_f, cv2.COLOR_BGR2RGB)

        plt.figure("边缘检测")
        plt.subplot(1,3,1)
        edges_transformed_image_z_rgb=cv2.resize(edges_transformed_image_z_rgb,(height_show, width_show))
        plt.imshow(edges_transformed_image_z_rgb)
        plt.axis('off')
        plt.subplot(1,3,2)
        edges_transformed_image_c_rgb=cv2.resize(edges_transformed_image_c_rgb,(height_show, width_show))
        plt.imshow(edges_transformed_image_c_rgb)
        plt.axis('off')
        plt.subplot(1,3,3)
        edges_transformed_image_f_rgb=cv2.resize(edges_transformed_image_f_rgb,(height_show, width_show))
        plt.imshow(edges_transformed_image_f_rgb)
        plt.axis('off')
        #plt.show()
        cv2.imwrite(r"C:\Users\86159\Desktop\vuenii\public\15972129987\before\1.jpg",edges_transformed_image_z_rgb)
        cv2.imwrite(r"C:\Users\86159\Desktop\vuenii\public\15972129987\before\2.jpg",edges_transformed_image_c_rgb)
        cv2.imwrite(r"C:\Users\86159\Desktop\vuenii\public\15972129987\before\3.jpg",edges_transformed_image_f_rgb)
        plt.clf()


    ### 6.基于阈值的图像分割
    if mode_str == "6":
        _, binary_transformed_image_z= cv2.threshold(transformed_image_z, 127, 255, cv2.THRESH_BINARY)
        binary_transformed_image_z_rgb = cv2.cvtColor(binary_transformed_image_z, cv2.COLOR_BGR2RGB)
        _, binary_transformed_image_c= cv2.threshold(transformed_image_c, 127, 255, cv2.THRESH_BINARY)
        binary_transformed_image_c_rgb = cv2.cvtColor(binary_transformed_image_c, cv2.COLOR_BGR2RGB)
        _, binary_transformed_image_f= cv2.threshold(transformed_image_f, 127, 255, cv2.THRESH_BINARY)
        binary_transformed_image_f_rgb = cv2.cvtColor(binary_transformed_image_f, cv2.COLOR_BGR2RGB)
        plt.figure("阈值分割")
        plt.subplot(1,3,1)
        binary_transformed_image_z_rgb=cv2.resize(binary_transformed_image_z_rgb,(height_show, width_show))
        plt.imshow(binary_transformed_image_z_rgb)
        plt.axis('off')
        plt.subplot(1,3,2)
        binary_transformed_image_c_rgb=cv2.resize(binary_transformed_image_c_rgb,(height_show, width_show))
        plt.imshow(binary_transformed_image_c_rgb)
        plt.axis('off')
        plt.subplot(1,3,3)
        binary_transformed_image_f_rgb=cv2.resize(binary_transformed_image_f_rgb,(height_show, width_show))
        plt.imshow(binary_transformed_image_f_rgb)
        plt.axis('off')
        #plt.show()
        #print(height_show)
        cv2.imwrite(r"C:\Users\86159\Desktop\vuenii\public\15972129987\before\1.jpg",binary_transformed_image_z_rgb)
        cv2.imwrite(r"C:\Users\86159\Desktop\vuenii\public\15972129987\before\2.jpg",binary_transformed_image_c_rgb)
        cv2.imwrite(r"C:\Users\86159\Desktop\vuenii\public\15972129987\before\3.jpg",binary_transformed_image_f_rgb)
        plt.clf()
'''if __name__ == '__main__':
    post_data=[6, '10', '20', '30']
    mainpic(f'./public/15972129987/before/result_0000.nii.gz',int(post_data[1]),int(post_data[2]),int(post_data[3]),"6")
'''
