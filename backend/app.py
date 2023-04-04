from flask import Flask, request, send_file ,jsonify
from flask_cors import CORS
import os
from calc import calc
from analyze import getall,haddlechange
import urllib.request
from  Scp import  upload_img
import json

app = Flask(__name__)
cors= CORS(app)
#app.config['UPLOAD_FOLDER'] = './uploads'  # 上传文件的保存目录
num = 0
@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']  # 获取上传的文件
    filename = file.filename
    #file.save(os.path.join(f'./backend/uploads/{num}.nii.gz'))  # 保存文件到本地
    file.save(os.path.join(f'./public/now.nii.gz'))
    #upload_img('now.nii.gz')
    return 'File saved successfully!'


@app.route('/analyse', methods=['POST'])
def anlayse():
    #return calc()
    return jsonify(getall())

@app.route('/download')
def download():
    file_url = request.args.get('file_url')
    print(file_url)
    file_name = os.path.basename(file_url)
    print(file_name)
    file_url=r'C:\Users\86159\Desktop\vuenii\change.nii.gz'
    #urllib.request.urlretrieve(file_url, file_name)
    return send_file(file_url, as_attachment=True)

@app.route('/Change', methods=['POST','GET'])
def change():
    post_data = request.get_json()
    changedata=json.dumps(post_data)
    changedata=json.loads(changedata)
    #print(len(changedata),changedata[0]['_value'])
    haddlechange(changedata)
    file_url=r'C:\Users\86159\Desktop\vuenii\change.nii.gz'
    return send_file(file_url, as_attachment=True)

if __name__ == '__main__':
    app.run()
