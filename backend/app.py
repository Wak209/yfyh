from flask import Flask, request, send_file ,jsonify
from flask_cors import CORS
import os
from calc import calc
from analyze import getall,haddlechange
import urllib.request
from  Scp import  upload_img,getanswer
from showall import Main
import json
import time
import shutil 
from showbefore import get_shape
from threepic import mainpic
from changelabel import changelabels
from message import send_sms
from drawgraph import draw,adjust
from comparegraph import drawc

app = Flask(__name__)
cors= CORS(app)
#app.config['UPLOAD_FOLDER'] = './uploads'  # 上传文件的保存目录





@app.route('/uploadan', methods=['POST','GET'])
def uploadan():
    file = request.files['file']  # 获取上传的文件
    filename = file.filename
    #file.save(os.path.join(f'./backend/uploads/{num}.nii.gz'))  # 保存文件到本地
    file.save(os.path.join(f'./public/an.nii.gz'))
    #upload_img('now.nii.gz')
    dtt = getall(r"C:\Users\86159\Desktop\vuenii\public\an.nii.gz")
    draw(dtt,"Xlen")
    draw(dtt,"Ylen")
    draw(dtt,"Zlen")
    draw(dtt,"XS")
    draw(dtt,"YS")
    draw(dtt,"ZS")
    draw(dtt,"num")
    time.sleep(0.5)
    dtt=adjust(dtt)
    return jsonify(dtt)


@app.route('/uploadvol', methods=['POST','GET'])
def uploadvol():
    file = request.files['file']  # 获取上传的文件
    filename = file.filename
    #file.save(os.path.join(f'./backend/uploads/{num}.nii.gz'))  # 保存文件到本地
    file.save(os.path.join(f'./public/vol/{filename}'))
    #upload_img('now.nii.gz')
    return f'{filename}'


@app.route('/uploadall', methods=['POST','GET'])
def uploadall():
    files = request.files.getlist('file') # 获取上传的文件
    for file in files:
        filename = file.filename
            #file.save(os.path.join(f'./backend/uploads/{num}.nii.gz'))  # 保存文件到本地
        file.save(os.path.join(f'./public/all/{filename}'))
    #upload_img('now.nii.gz')
    #return jsonify(getall(r"C:\Users\86159\Desktop\vuenii\public\an.nii.gz"))
    list=Main()
    drawc(list,1)
    drawc(list,2)
    drawc(list,3)
    drawc(list,4)
    drawc(list,5)
    drawc(list,6)
    drawc(list,7)
    drawc(list,8)
    drawc(list,9)
    drawc(list,10)
    drawc(list,14)

    return jsonify(list)




@app.route('/Uploadgpu', methods=['POST'])
def Upload():
    upload_img('result_0000.nii.gz')
    time.sleep(60)
    getanswer()
    #time.sleep(1)
    return 'upload successfully'

@app.route('/analyse', methods=['POST'])
def anlayse():
    #return calc()
    dtt = getall(r"C:\Users\86159\Desktop\vuenii\public\15972129987\after\20230602_result.nii.gz")

    draw(dtt,"Xlen")
    draw(dtt,"Ylen")
    draw(dtt,"Zlen")
    draw(dtt,"XS")
    draw(dtt,"YS")
    draw(dtt,"ZS")
    draw(dtt,"num")
    time.sleep(0.5)

    dtt=adjust(dtt)
    return jsonify(dtt)

@app.route('/download')
def download():
    file_url = request.args.get('file_url')
    print(file_url)
    file_name = os.path.basename(file_url)
    print(file_name)
    
    File_url=r"C:\Users\86159\Desktop\vuenii\\"
    #urllib.request.urlretrieve(file_url, file_name)
    return send_file(File_url+file_url, as_attachment=True)

@app.route('/Change', methods=['POST','GET'])
def change():
    post_data = request.get_json()
    changedata=json.dumps(post_data)
    changedata=json.loads(changedata)
    #print(len(changedata),changedata[0]['_value'])
    haddlechange(changedata)
    file_url=r"C:\Users\86159\Desktop\vuenii\change.nii.gz"
    return send_file(file_url, as_attachment=True)


@app.route('/login', methods=['POST','GET'])
def login():
    post_data = request.get_json()
    print(post_data)
    print(type(post_data))
    accounts = {}
    with open(r"C:\Users\86159\Desktop\vuenii\backend\file.txt", 'r') as f:
        for line in f:
            phonenum, password = line.strip().split()
            accounts[phonenum]=password
    if accounts.get(post_data[0]) == post_data[1]:
        return 'successfully'
    else:
        return 'wrong'

@app.route('/upload', methods=['POST','GET'])
def upload():
    print(request)
    file = request.files['file']  # 获取上传的文件
    filename = file.filename
    DIct=dict()
    #print(filename[-7:])
    #file.save(os.path.join(f'./backend/uploads/{num}.nii.gz'))  # 保存文件到本地
    if filename[-7:] == '.nii.gz':
        filename='result_0000.nii.gz'
        file.save(os.path.join(f'./public/15972129987/before/result_0000.nii.gz'))
        DIct["name"]=filename
        DIct["shape"]=get_shape(f'./public/15972129987/before/result_0000.nii.gz')
        mainpic(f'./public/15972129987/before/result_0000.nii.gz',DIct["shape"][0]/2,DIct["shape"][1]/2,DIct["shape"][2]/2,"0")
        print(DIct)
        return DIct
        #print(get_shape(f'./public/15972129987/before/result_0000.nii.gz'))
    else:
        file.save(os.path.join(f'./public/15972129987/before/{filename}'))
        DIct["name"]=filename
    #upload_img('now.nii.gz')
        return f'{filename}'

@app.route('/beforeshow', methods=['POST','GET'])
def beforeshow():
    post_data = request.get_json()
    print(post_data)
    mainpic(f'./public/15972129987/before/result_0000.nii.gz',int(post_data[1]),int(post_data[2]),int(post_data[3]),str(post_data[0]-1))
    
    return 'success'

@app.route('/changelabel', methods=['POST','GET'])
def changelabel():
    post_data = request.get_json()
    print(post_data)
    #mainpic(f'./public/15972129987/before/result_0000.nii.gz',int(post_data[1]),int(post_data[2]),int(post_data[3]),str(post_data[0]-1))
    changelabels(r"C:\Users\86159\Desktop\vuenii\public\15972129987\after\result.nii.gz",post_data)
    return 'success'


@app.route('/zhuce', methods=['POST','GET'])
def zhuce():
    post_data = request.get_json()
    return str(send_sms(str(post_data['phonenum'])))

@app.route('/confirmzhuce', methods=['POST','GET'])
def confirmzhuce():
    post_data = request.get_json()
    with open(r"C:\Users\86159\Desktop\vuenii\backend\file.txt", 'a') as f:
        f.write('\n'+post_data["phonenum"] +' '+ post_data["passwd"] )
    f.close()
    return 'success'

@app.route('/folders', methods=['POST','GET'])
def folders():
    before_file_path=os.listdir(r"C:\Users\86159\Desktop\vuenii\public\15972129987\before")
    del_list=[]
    for i in range(len(before_file_path)):
        print(before_file_path[i][-3:])
        if before_file_path[i][-3:] == "jpg":
            del_list.append(before_file_path[i])
    for i in del_list:
        before_file_path.remove(i)
    print(before_file_path)
    return before_file_path

@app.route('/afterfolders', methods=['POST','GET'])
def afterfolders():
    after_file_path=os.listdir(r"C:\Users\86159\Desktop\vuenii\public\15972129987\after")
    change_file=os.listdir(r"C:\Users\86159\Desktop\vuenii\public\15972129987\after\change")
    '''del_list=[]
    for i in range(len(before_file_path)):
        print(before_file_path[i][-3:])
        if before_file_path[i][-3:] == "jpg":
            del_list.append(before_file_path[i])
    for i in del_list:
        before_file_path.remove(i)
    print(before_file_path)'''
    after_file_path.remove("change")
    for i in change_file:
        after_file_path.append("change\\"+str(i))
    return after_file_path

@app.route('/graphfolders', methods=['POST','GET'])
def graphfolders():
    graph_file_path=os.listdir(r"C:\Users\86159\Desktop\vuenii\public\15972129987\graph")
    return graph_file_path
if __name__ == '__main__':
    app.run()
