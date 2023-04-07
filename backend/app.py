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

app = Flask(__name__)
cors= CORS(app)
#app.config['UPLOAD_FOLDER'] = './uploads'  # 上传文件的保存目录


@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']  # 获取上传的文件
    filename = file.filename
    #print(filename[-7:])
    #file.save(os.path.join(f'./backend/uploads/{num}.nii.gz'))  # 保存文件到本地
    if filename[-7:] == '.nii.gz':
        filename='result_0000.nii.gz'
        file.save(os.path.join(f'./public/result_0000.nii.gz'))
    else:
        file.save(os.path.join(f'./public/user/{filename}'))
    #upload_img('now.nii.gz')
    return f'{filename}'


@app.route('/uploadan', methods=['POST','GET'])
def uploadan():
    file = request.files['file']  # 获取上传的文件
    filename = file.filename
    #file.save(os.path.join(f'./backend/uploads/{num}.nii.gz'))  # 保存文件到本地
    file.save(os.path.join(f'./public/an.nii.gz'))
    #upload_img('now.nii.gz')
    return jsonify(getall(r"C:\Users\86159\Desktop\vuenii\public\an.nii.gz"))


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
    shutil.rmtree('C:\Users\86159\Desktop\vuenii\public\all')  
    os.mkdir('C:\Users\86159\Desktop\vuenii\public\all')  
    return jsonify(Main())




@app.route('/Uploadgpu', methods=['POST'])
def Upload():
    #upload_img('result_0000.nii.gz')
    #time.sleep(60)
    #getanswer()
    return 'upload successfully'

@app.route('/analyse', methods=['POST'])
def anlayse():
    #return calc()
    return jsonify(getall(r"C:\Users\86159\Desktop\vuenii\public\result.nii.gz"))

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

if __name__ == '__main__':
    app.run()
