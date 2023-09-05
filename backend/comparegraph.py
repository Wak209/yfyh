import matplotlib.pyplot as plt
import numpy as np
import cv2

def drawc(input_msg, id):
    plt.clf()
    count=len(input_msg[0])
    # 设置中文编码
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    # 输入
    '''input_msg = [
        [{'name': '3a93b3d5-b8be-4b6f-bd00-922d6080d9fb.nii.gz', 'num': 131700.16, 'id': 1, 'Xlen': 104.14, 'Ylen': 99.3, 'Zlen': 60.0, 'p': 0.73, 'XS': 1262.4, 'YS': 1319.92, 'ZS': 3581.24},
         {'name': '93d3c6a9-cf23-4b60-8f0d-75dd7080f1be.nii.gz', 'num': 103266.77, 'id': 1, 'Xlen': 82.96, 'Ylen': 61.91, 'Zlen': 78.75, 'p': 0.63, 'XS': 1496.77, 'YS': 2553.96, 'ZS': 2070.4}],
        [{'name': '3a93b3d5-b8be-4b6f-bd00-922d6080d9fb.nii.gz', 'num': 185246.48, 'id': 2, 'Xlen': 69.63, 'Ylen': 82.34, 'Zlen': 85.0, 'p': 0.91, 'XS': 3896.19, 'YS': 2770.02, 'ZS': 2791.97},
         {'name': '93d3c6a9-cf23-4b60-8f0d-75dd7080f1be.nii.gz', 'num': 198295.65, 'id': 2, 'Xlen': 68.72, 'Ylen': 72.44, 'Zlen': 117.5, 'p': 0.88, 'XS': 4192.36, 'YS': 4098.71, 'ZS': 2377.45}],
        [{'name': '3a93b3d5-b8be-4b6f-bd00-922d6080d9fb.nii.gz', 'num': 237166.96, 'id': 3, 'Xlen': 87.79, 'Ylen': 78.71, 'Zlen': 110.0, 'p': 0.82, 'XS': 3666.11, 'YS': 3859.86, 'ZS': 2374.79},
         {'name': '93d3c6a9-cf23-4b60-8f0d-75dd7080f1be.nii.gz', 'num': 157541.33, 'id': 3, 'Xlen': 68.11, 'Ylen': 59.44, 'Zlen': 116.25, 'p': 0.96, 'XS': 3669.96, 'YS': 4549.91, 'ZS': 1487.73}],
        [{'name': '3a93b3d5-b8be-4b6f-bd00-922d6080d9fb.nii.gz', 'num': 9419.59, 'id': 4, 'Xlen': 44.8, 'Ylen': 45.41, 'Zlen': 40.0, 'p': 0.73, 'XS': 305.76, 'YS': 233.11, 'ZS': 256.25},
         {'name': '93d3c6a9-cf23-4b60-8f0d-75dd7080f1be.nii.gz', 'num': 35399.6, 'id': 4, 'Xlen': 46.44, 'Ylen': 58.2, 'Zlen': 35.0, 'p': 0.97, 'XS': 1210.42, 'YS': 602.89, 'ZS': 1533.34}],
        [{'name': '3a93b3d5-b8be-4b6f-bd00-922d6080d9fb.nii.gz', 'num': 7870.74, 'id': 5, 'Xlen': 35.12, 'Ylen': 18.16, 'Zlen': 35.0, 'p': 0.9, 'XS': 390.53, 'YS': 765.92, 'ZS': 188.06},
         {'name': '93d3c6a9-cf23-4b60-8f0d-75dd7080f1be.nii.gz', 'num': 8131.03, 'id': 5, 'Xlen': 28.48, 'Ylen': 40.24, 'Zlen': 53.75, 'p': 0.91, 'XS': 472.1, 'YS': 284.8, 'ZS': 195.12}],
        [{'name': '3a93b3d5-b8be-4b6f-bd00-922d6080d9fb.nii.gz', 'num': 1348414.86, 'id': 6, 'Xlen': 214.34, 'Ylen': 148.34, 'Zlen': 150.0, 'p': 0.97, 'XS': 4522.85, 'YS': 12627.05, 'ZS': 13427.55},
         {'name': '93d3c6a9-cf23-4b60-8f0d-75dd7080f1be.nii.gz', 'num': 1122622.61, 'id': 6, 'Xlen': 223.51, 'Ylen': 137.45, 'Zlen': 166.25, 'p': 0.8, 'XS': 3250.49, 'YS': 12816.22, 'ZS': 7326.31}],
        [{'name': '3a93b3d5-b8be-4b6f-bd00-922d6080d9fb.nii.gz', 'num': 252761.8, 'id': 7, 'Xlen': 137.44, 'Ylen': 115.04, 'Zlen': 95.0, 'p': 0.84, 'XS': 2134.28, 'YS': 1813.38, 'ZS': 2847.32},
         {'name': '93d3c6a9-cf23-4b60-8f0d-75dd7080f1be.nii.gz', 'num': 305638.23, 'id': 7, 'Xlen': 117.02, 'Ylen': 107.73, 'Zlen': 121.25, 'p': 0.92, 'XS': 5466.24, 'YS': 2481.21, 'ZS': 2399.68}],
        [{'name': '3a93b3d5-b8be-4b6f-bd00-922d6080d9fb.nii.gz', 'num': 52890.12, 'id': 8, 'Xlen': 30.27, 'Ylen': 44.2, 'Zlen': 210.0, 'p': 0.76, 'XS': 2291.7, 'YS': 1386.52, 'ZS': 222.52},
         {'name': '93d3c6a9-cf23-4b60-8f0d-75dd7080f1be.nii.gz', 'num': 70629.1, 'id': 8, 'Xlen': 30.34, 'Ylen': 78.63, 'Zlen': 226.25, 'p': 0.89, 'XS': 4143.6, 'YS': 923.29, 'ZS': 302.07}],
        [{'name': '3a93b3d5-b8be-4b6f-bd00-922d6080d9fb.nii.gz', 'num': 64824.54, 'id': 9, 'Xlen': 33.3, 'Ylen': 37.54, 'Zlen': 225.0, 'p': 0.92, 'XS': 3278.61, 'YS': 3142.38, 'ZS': 255.51},
         {'name': '93d3c6a9-cf23-4b60-8f0d-75dd7080f1be.nii.gz', 'num': 69367.44, 'id': 9, 'Xlen': 34.67, 'Ylen': 39.01, 'Zlen': 225.0, 'p': 'error', 'XS': 3248.17, 'YS': 1804.02, 'ZS': 313.95}],
        [{'name': '3a93b3d5-b8be-4b6f-bd00-922d6080d9fb.nii.gz', 'num': 74302.78, 'id': 10, 'Xlen': 148.95, 'Ylen': 49.04, 'Zlen': 65.0, 'p': 0.94, 'XS': 460.16, 'YS': 2585.35, 'ZS': 837.66},
         {'name': '93d3c6a9-cf23-4b60-8f0d-75dd7080f1be.nii.gz', 'num': 69363.13, 'id': 10, 'Xlen': 131.88, 'Ylen': 64.39, 'Zlen': 77.5, 'p': 0.9, 'XS': 694.99, 'YS': 802.56, 'ZS': 686.94}],
        [{'name': '3a93b3d5-b8be-4b6f-bd00-922d6080d9fb.nii.gz', 'num': 4488.92, 'id': 11, 'Xlen': 18.77, 'Ylen': 32.7, 'Zlen': 35.0, 'p': 0.89, 'XS': 387.5, 'YS': 148.34, 'ZS': 244.52},
         {'name': '93d3c6a9-cf23-4b60-8f0d-75dd7080f1be.nii.gz', 'num': 3590.9, 'id': 11, 'Xlen': 17.34, 'Ylen': 39.01, 'Zlen': 35.0, 'p': 0.98, 'XS': 448.88, 'YS': 101.38, 'ZS': 182.85}],
        [{'name': '3a93b3d5-b8be-4b6f-bd00-922d6080d9fb.nii.gz', 'num': 4479.76, 'id': 12, 'Xlen': 20.59, 'Ylen': 33.3, 'Zlen': 35.0, 'p': 0.95, 'XS': 233.11, 'YS': 151.37, 'ZS': 174.13},
         {'name': '93d3c6a9-cf23-4b60-8f0d-75dd7080f1be.nii.gz', 'num': 3937.81, 'id': 12, 'Xlen': 16.72, 'Ylen': 35.91, 'Zlen': 42.5, 'p': 0.99, 'XS': 380.77, 'YS': 89.78, 'ZS': 106.57}],
        [{'name': '3a93b3d5-b8be-4b6f-bd00-922d6080d9fb.nii.gz', 'num': 54307.0, 'id': 13, 'Xlen': 101.72, 'Ylen': 49.04, 'Zlen': 75.0, 'p': 0.98, 'XS': 287.6, 'YS': 2664.06, 'ZS': 623.21},
         {'name': '93d3c6a9-cf23-4b60-8f0d-75dd7080f1be.nii.gz', 'num': 43125.25, 'id': 13, 'Xlen': 86.06, 'Ylen': 42.1, 'Zlen': 121.25, 'p': 0.82, 'XS': 334.34, 'YS': 3126.66, 'ZS': 282.13}],
        [{'name': '3a93b3d5-b8be-4b6f-bd00-922d6080d9fb.nii.gz', 'num': 57131.59, 'id': 14, 'Xlen': 62.97, 'Ylen': 62.36, 'Zlen': 30.0, 'p': 0.76, 'XS': 1104.98, 'YS': 1274.51, 'ZS': 2878.12},
         {'name': '93d3c6a9-cf23-4b60-8f0d-75dd7080f1be.nii.gz', 'num': 99920.25, 'id': 14, 'Xlen': 89.78, 'Ylen': 65.01, 'Zlen': 40.0, 'p': 0.91, 'XS': 1596.61, 'YS': 2234.33, 'ZS': 3764.36}],
        [{'name': '3a93b3d5-b8be-4b6f-bd00-922d6080d9fb.nii.gz', 'num': 24026.47, 'id': 15, 'Xlen': 38.14, 'Ylen': 32.7, 'Zlen': 30.0, 'p': 0.74, 'XS': 914.26, 'YS': 1114.06, 'ZS': 981.73},
         {'name': '93d3c6a9-cf23-4b60-8f0d-75dd7080f1be.nii.gz', 'num': 121468.02, 'id': 15, 'Xlen': 61.91, 'Ylen': 85.44, 'Zlen': 71.25, 'p': 0.77, 'XS': 2935.5, 'YS': 1422.48, 'ZS': 2338.73}]]
'''    
    # 数据
    labels = ['脾脏', '右肾', '左肾', '胆囊', '食管', '肝脏', '胃', '主动脉', '下腔静脉', '胰腺', 'error', 'error', 'error', '膀胱']
    label = ['体积/500', 'Xlen', 'Ylen', 'Zlen', 'XS/10', 'YS/10', 'ZS/10']
    #print(f'LEN:{len(input_msg[0])}')
    fig, ax = plt.subplots()
    ### 画柱状图
    for count_num in range(count):
        # 生成7个标签和对应的数据
        data=[]
        for key in ["num", "Xlen", "Ylen", "Zlen", "XS", "YS", "ZS"]:
            value = input_msg[id-1][count_num][key]
            if value == "error":
                value = 0
            if key == "num":
                value = value / 500
            elif key in ["XS", "YS", "ZS"]:
                value = value / 10
            data.append(value)
        ''' data = [input_msg[id-1][count_num]["num"]/500,
                input_msg[id-1][count_num]["Xlen"],
                input_msg[id-1][count_num]["Ylen"],
                input_msg[id-1][count_num]["Zlen"],
                input_msg[id-1][count_num]["XS"]/10,
                input_msg[id-1][count_num]["YS"]/10,
                input_msg[id-1][count_num]["ZS"]/10]
        print(data)'''
        # 绘制第一个柱形图
        ax.bar([i +0.4*count_num for i in range(len(label))], data, width=0.4, align='center', label=input_msg[id-1][count_num]["name"])
        ax.set_xticks([i + 0.4*count_num / count for i in range(len(label))])
        ax.set_xticklabels(label)
    ax.legend()
    plt.title(labels[id-1])
    plt.xticks(fontsize=11)
    # 显示图表
    if(1<=id<=14 and id != 11 and id != 12 and id != 13):
        plt.savefig(r"C:\Users\86159\Desktop\vuenii\public\15972129987\graph\\compare" + str(id) + '.jpg')
        #x2 = cv2.imread("id" + str(id) + '.jpg')
        #print(x2.shape)
        #plt.show()
        #plt.clf()
    else:
        print("error")

if __name__ == '__main__':
    drawc(count=2, id=10)     # count为画的文件的数量，而id取1-10和14，对应11个器官

    # 设置图表标题和标签
    # plt.xticks(rotation=30,fontsize=12)
    # plt.title(mode)
    # plt.savefig(mode + '.jpg')
    # x2 = cv2.imread(mode + '.jpg')
    # output_x2 = cv2.resize(x2, (480, 480))
    # cv2.imwrite(mode + '.jpg', output_x2)
    # x3 = cv2.imread(mode + '.jpg')