import paramiko  # 用于调用scp命令
from scp import SCPClient
import time 
 
# 将指定目录的图片文件上传到服务器指定目录
# remote_path远程服务器目录
# file_path本地文件夹路径
# img_name是file_path本地文件夹路径下面的文件名称
def upload_img(img_name, remote_path="./autodl-tmp/upload", file_path=r"C:\\Users\86159\Desktop\vuenii\public"):
    # img_name示例：07670ff76fc14ab496b0dd411a33ac95-6.webp
    host = "222.187.226.110"  #服务器ip地址
    port = 46951  # 端口号
    username = "root"  # ssh 用户名
    password = "lPiBLPRerb"  # 密码

    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    ssh_client.connect(host, port, username, password)
    scpclient = SCPClient(ssh_client.get_transport(),socket_timeout=15.0)
    local_path = file_path + "\\" + img_name
    try:
        scpclient.put(local_path, remote_path)
    except FileNotFoundError as e:
        print(e)
        print("系统找不到指定文件" + local_path)
        return False
    else:
        print("文件上传成功")
        return True
    ssh_client.close()


def download_img(img_name, remote_path="./autodl-tmp", file_path=r"C:\\Users\86159\Desktop\vuenii\public\basic"):
    # img_name示例：07670ff76fc14ab496b0dd411a33ac95-6.webp
    host = "222.187.226.110"  #服务器ip地址
    port = 46951  # 端口号
    username = "root"  # ssh 用户名
    password = "lPiBLPRerb"  # 密码

    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    ssh_client.connect(host, port, username, password)
    scpclient = SCPClient(ssh_client.get_transport(),socket_timeout=15.0)
    local_path = file_path 
    remote_path = remote_path  + img_name
    try:
        scpclient.get(remote_path, local_path)
    except :
        #print(e)
        print("系统找不到指定文件")
    else:
        print("文件下载成功")
    ssh_client.close()


def getanswer():
    flag=0
    while(flag == 0):
        flag = download_img('result.nii.gz')
        time.sleep(10)

'''if __name__ == "__main__":
    upload_img('before.nii.gz')'''