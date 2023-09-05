import matplotlib.pyplot as plt
import numpy as np
import cv2
import warnings
warnings.simplefilter("ignore", UserWarning)


def draw(Input_msg,mode):
    # 设置中文编码
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    picture_size = 0.9  # 缩小0.9倍
    input_msg = Input_msg
    # 输入
    '''input_msg = [
        {'name': '脾脏', 'num': 190380.06, 'id': 1, 'Xlen': 93.38, 'Ylen': 85.5, 'Zlen': 95.0, 'p': 0.96, 'XS': 2694.38,
         'YS': 3827.81, 'ZS': 3015.35},
        {'name': '右肾', 'num': 203230.9, 'id': 2, 'Xlen': 73.69, 'Ylen': 74.25, 'Zlen': 85.0, 'p': 0.86, 'XS': 4038.75,
         'YS': 3585.94, 'ZS': 3088.44},
        {'name': '左肾', 'num': 177136.88, 'id': 3, 'Xlen': 72.0, 'Ylen': 65.25, 'Zlen': 95.0, 'p': 0.97, 'XS': 3538.12,
         'YS': 4232.81, 'ZS': 2131.95},
        {'name': '胆囊', 'num': 100008.11, 'id': 4, 'Xlen': 66.38, 'Ylen': 77.62, 'Zlen': 55.0, 'p': 0.67, 'XS': 2542.5,
         'YS': 1783.12, 'ZS': 2599.28},
        {'name': '食管', 'num': 5378.91, 'id': 5, 'Xlen': 26.44, 'Ylen': 21.94, 'Zlen': 15.0, 'p': 0.79, 'XS': 270.0,
         'YS': 393.75, 'ZS': 285.71},
        {'name': '肝脏', 'num': 1766295.18, 'id': 6, 'Xlen': 235.12, 'Ylen': 195.75, 'Zlen': 125.0, 'p': 0.84,
         'XS': 7025.62, 'YS': 11927.81, 'ZS': 12357.88},
        {'name': '胃', 'num': 350062.38, 'id': 7, 'Xlen': 140.06, 'Ylen': 149.06, 'Zlen': 110.0, 'p': 0.99,
         'XS': 2061.56, 'YS': 1909.69, 'ZS': 2378.11},
        {'name': '主动脉', 'num': 75758.73, 'id': 8, 'Xlen': 28.69, 'Ylen': 56.25, 'Zlen': 200.0, 'p': 0.93, 'XS': 4308.75,
         'YS': 1977.19, 'ZS': 374.62},
        {'name': '下腔静脉', 'num': 73689.43, 'id': 9, 'Xlen': 37.69, 'Ylen': 33.19, 'Zlen': 215.0, 'p': 0.96,
         'XS': 3642.19, 'YS': 2984.06, 'ZS': 305.65},
        {'name': '胰腺', 'num': 112960.2, 'id': 10, 'Xlen': 144.0, 'Ylen': 84.94, 'Zlen': 90.0, 'p': 0.75, 'XS': 632.81,
         'YS': 885.94, 'ZS': 1462.11},
        {'name': '右肾上腺', 'num': 6427.79, 'id': 11, 'Xlen': 26.44, 'Ylen': 41.62, 'Zlen': 40.0, 'p': 0.7, 'XS': 478.12,
         'YS': 180.0, 'ZS': 248.06},
        {'name': '左肾上腺', 'num': 6312.3, 'id': 12, 'Xlen': 20.81, 'Ylen': 36.0, 'Zlen': 50.0, 'p': 0.75, 'XS': 416.25,
         'YS': 174.38, 'ZS': 191.43},
        {'name': '十二指肠', 'num': 64782.6, 'id': 13, 'Xlen': 115.31, 'Ylen': 63.56, 'Zlen': 80.0, 'p': 0.92, 'XS': 247.5,
         'YS': 995.62, 'ZS': 747.04},
        {'name': '膀胱', 'num': 81444.55, 'id': 14, 'Xlen': 72.0, 'Ylen': 85.5, 'Zlen': 35.0, 'p': 0.85, 'XS': 1653.75,
         'YS': 1389.38, 'ZS': 3517.49},
        {'name': '前列腺/子宫', 'num': 31338.46, 'id': 15, 'Xlen': 45.56, 'Ylen': 36.0, 'Zlen': 35.0, 'p': 0.79,
         'XS': 1015.31, 'YS': 1265.62, 'ZS': 1029.9}]'''

    # 数据
    labels = ['脾脏', '右肾', '左肾', '胆囊', '食管', '肝脏', '胃', '主动脉', '下腔静脉', '胰腺', '膀胱']
    if mode == 'num':
        ### 1.画体积的饼图
        for i in input_msg:
            if i["num"] == 'error':
                i["num"] = 0
        sizes = [input_msg[0]["num"],
                 input_msg[1]["num"],
                 input_msg[2]["num"],
                 input_msg[3]["num"],
                 input_msg[4]["num"],
                 input_msg[5]["num"],
                 input_msg[6]["num"],
                 input_msg[7]["num"],
                 input_msg[8]["num"],
                 input_msg[9]["num"],
                 input_msg[13]["num"]]
        
        colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#ffb3e6', '#c2c2f0', '#ffb3b3', '#c2d6d6', '#d9b3ff', '#b3d9ff', '#ffccff']
        # 绘图
        fig = plt.figure(figsize=(4.8, 4.8))
        ax = fig.add_subplot(111)
        ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90, textprops={'fontsize': 12},  labeldistance=1.05, pctdistance=0.9, radius=picture_size)
        plt.title("体积", fontsize=18)
        ax.set_position([0.1, 0.1, 0.8, 0.8])
        ax.axis('equal')  # 使饼图为正圆形
        # 更改字体颜色
        '''for text in ax.texts:
            text.set_color('black')'''
        plt.setp(ax.texts,color=(0, 0, 139/255))
        plt.savefig('1.jpg')
        x1 = cv2.imread('1.jpg')
        output_x1 = cv2.resize(x1, (480, 480))
        cv2.imwrite(r"C:\Users\86159\Desktop\vuenii\public\15972129987\graph\\"+'v.jpg',output_x1)
        #plt.show()
        plt.clf()
    
    elif mode =='Xlen' or mode =='Ylen' or mode =='Zlen' or mode =='XS' or mode =='YS' or mode =='ZS':
        ### 2.画Xlen的柱状图
        # 生成11个标签和对应的数据
        dict={'Xlen':'直径(X)','Ylen':'直径(Y)','Zlen':'直径(Z)','XS':'横截面积(X)','YS':'横截面积(Y)','ZS':'横截面积(Z)'}
        for i in input_msg:
            if i[mode] == 'error':
                i[mode] = 0
        data = [input_msg[0][mode],
                input_msg[1][mode],
                input_msg[2][mode],
                input_msg[3][mode],
                input_msg[4][mode],
                input_msg[5][mode],
                input_msg[6][mode],
                input_msg[7][mode],
                input_msg[8][mode],
                input_msg[9][mode],
                input_msg[13][mode]]
        # 绘制柱形图
        plt.bar(labels, data, width=0.1)
        # 设置图表标题和标签
        data=[]
        plt.xticks(rotation=30,fontsize=12)
        #plt.yticks(fontsize=12)
        #plt.ylabel(mode)
        plt.title(f'{dict[mode]}', fontsize=18)
        plt.savefig(mode + '.jpg')
        x2 = cv2.imread(mode + '.jpg')
        output_x2 = cv2.resize(x2, (480, 480))
        cv2.imwrite(r"C:\Users\86159\Desktop\vuenii\public\15972129987\graph\\" +str(mode)+'.jpg', output_x2)
        # 显示图表
        plt.clf()
        #plt.show()
    else:
        print("error")

'''if __name__ == '__main__':
    draw("Xlen")'''

def adjust(lsit):
    Map=lsit
    for i in Map:
        if i['id'] == 11 or i['id'] == 12 or i['id'] == 13 or i['id'] == 15:
            Map.remove(i)
            
        if i['name'] == '膀胱' :
            i['id'] = 11
    for i in Map:
        if i['id'] == 12:
             Map.remove(i)
    for i in Map:
        if i['name'] == '膀胱' :
            i['id'] = 11
    #Map[-1],Map[-2] = Map[-2],Map[-1]
    print(Map)
    return Map