import os
import vtkmodules.all as vtk
from vtkmodules.util import *
from vtkmodules.util import *
from vtkmodules.util.vtkImageImportFromArray import *
#import vtkmodules.all as vtk
import SimpleITK as sitk
import numpy as np
import time
import datetime
import os
import sys
import nibabel as nib
import shutil
List=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
Name=['背景','脾脏','右肾','左肾','胆囊','食管','肝脏','胃','主动脉','下腔静脉','胰腺','右肾上腺','左肾上腺','十二指肠','膀胱','前列腺/子宫',]
label_name=[]
label_num=[]
def getall(label_path):
    file_path = r"C:\Users\86159\Desktop\vuenii\public\all"
    Path = file_path + r"\\" + label_path
    global label_array
    global List
    #label_path=r"C:\Users\86159\Desktop\vuenii\backend\submit\2.nii.gz"
    label_obj = nib.load(Path)
    label_array = label_obj.get_fdata()
    lt = np.unique(label_array, return_counts=True)
    #print(lt[0].tolist())#[0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0]
    label_name = lt[0].tolist()
    label_num = lt[1].tolist()

    pixdim =  label_obj.header['pixdim']
    #print(label_obj.header)
    Size = label_obj.header['dim'] #dim             : [  3 768 768  82   1   1   1   1]
    #print(label_array.shape)
    #print(pixdim)#[-1.          0.55598956  0.55598956  5.          0.          0.        0.          0.        ]
    nn=['name','num','id','Xlen','Ylen','Zlen','p','XS','YS','ZS']
    start = datetime.datetime.now()
    dct={}
    for i in range(len(label_name)):
        if int (i) != 0:
            index = int(label_name[i])
            Len = np.where(label_array==i)
            #print(Len[0],Len[1],Len[2])
            #print(np.max(Len[0]),np.min(Len[0]))
            mm=[]
            mm.append(label_path)#器官名称
            mm.append(round(label_num[i]*pixdim[1]*pixdim[2]*pixdim[3],2))#器官体积
            mm.append(int(label_name[i]))#器官标签id
            Xlength = round((np.max(Len[0])-np.min(Len[0]))*pixdim[1],2)
            mm.append(Xlength)#Xlen
            Ylength = round((np.max(Len[1])-np.min(Len[1]))*pixdim[2],2)
            mm.append(Ylength)#Ylen
            Zlength = round((np.max(Len[2])-np.min(Len[2]))*pixdim[3],2)
            mm.append(Zlength)#Zlen
            pp=getp(Name[int(label_name[i])],int(label_num[i]*pixdim[1]*pixdim[2]*pixdim[3]),Xlength,Ylength,Zlength)

            pp=round(pp,2)
            if(pp>0 and pp<1):
                mm.append(pp)#degree
            else:
                mm.append('error')
            #print(getarea(int(label_name[i]),(np.max(Len[0])+np.min(Len[0]))/2,(np.max(Len[1])+np.min(Len[1]))/2,(np.max(Len[2])+np.min(Len[2]))/2))
            XS,YS,ZS=getarea(int(label_name[i]),((np.max(Len[0])+np.min(Len[0]))/2),(np.max(Len[1])+np.min(Len[1]))/2,(np.max(Len[2])+np.min(Len[2]))/2)
            if XS != 'error':
                XS*=pixdim[2]*pixdim[3]
                XS=round(XS,2)
            if YS != 'error':
                YS*=pixdim[1]*pixdim[3]
                YS=round(YS,2)
            if ZS != 'error':
                ZS*=pixdim[1]*pixdim[2]
                ZS=round(ZS,2)
            mm.append(XS)#x截面面积
            mm.append(YS)#y截面面积
            mm.append(ZS)#z截面面积
            dct = dict(zip(nn,mm))
            List[index-1].append(dct)

    end = datetime.datetime.now()
    print(List)
    print(end - start )


def getp(ORname,V,xlen,ylen,zlen):
    P=0.6
    if ORname == '脾脏':
        ruler=202042.5641025641
        return  ((1-(ruler-V)*(1-P)/(ruler-95911)) if V<ruler else (590915-V)*(1-P)/(590915-ruler)+P)
    elif ORname == '右肾':
        ruler=154123.35897435897
        return  ((1-(ruler-V)*(1-P)/(ruler-74141)) if V<ruler else (298721-V)*(1-P)/(298721-ruler)+P)
    elif ORname == '左肾':
        ruler=166997.46153846153
        return  ((1-(ruler-V)*(1-P)/(ruler-69382)) if V<ruler else (323105-V)*(1-P)/(323105-ruler)+P)
    elif ORname == '胆囊':
        ruler=28316.846153846152
        return  ((1-(ruler-V)*(1-P)/(ruler-0)) if V<ruler else (116329-V)*(1-P)/(116329-ruler)+P)
    elif ORname == '食管':
        ruler=10407.666666666666
        return  ((1-(ruler-V)*(1-P)/(ruler-686)) if V<ruler else (23119-V)*(1-P)/(23119-ruler)+P)
    elif ORname == '肝脏':
        ruler=1384719.1282051282 
        return  ((1-(ruler-V)*(1-P)/(ruler-868877)) if V<ruler else (2358415-V)*(1-P)/(2358415-ruler)+P)
    elif ORname == '胃':
        ruler=358474.92307692306 
        return  ((1-(ruler-V)*(1-P)/(ruler-99840)) if V<ruler else (1173149-V)*(1-P)/(1173149-ruler)+P)
    elif ORname == '主动脉':
        ruler=85794.17948717948
        return  ((1-(ruler-V)*(1-P)/(ruler-31186)) if V<ruler else (208580-V)*(1-P)/(208580-ruler)+P)
    elif ORname == '下腔静脉':
        ruler=68947.41025641025
        return  ((1-(ruler-V)*(1-P)/(ruler-47342)) if V<ruler else (117923-V)*(1-P)/(117923-ruler)+P)
    elif ORname == '胰腺':
        ruler=82663.07692307692
        return  ((1-(ruler-V)*(1-P)/(ruler-28214)) if V<ruler else (130393-V)*(1-P)/(130393-ruler)+P)
    elif ORname == '右肾上腺':
        ruler=3398.769230769231
        return  ((1-(ruler-V)*(1-P)/(ruler-1442)) if V<ruler else (7481-V)*(1-P)/(7481-ruler)+P)
    elif ORname == '左肾上腺':
        ruler=3977.5897435897436
        return  ((1-(ruler-V)*(1-P)/(ruler-1627)) if V<ruler else (7734-V)*(1-P)/(7734-ruler)+P)
    elif ORname == '十二指肠':
        ruler=51884.05128205128
        return  ((1-(ruler-V)*(1-P)/(ruler-31870)) if V<ruler else (112719-V)*(1-P)/(112719-ruler)+P)
    elif ORname == '膀胱':
        ruler=127865.58974358975
        return  ((1-(ruler-V)*(1-P)/(ruler-7931)) if V<ruler else (819482-V)*(1-P)/(819482-ruler)+P)
    elif ORname == '前列腺/子宫':
        ruler=57452.05128205128
        return  ((1-(ruler-V)*(1-P)/(ruler-6642)) if V<ruler else (169473-V)*(1-P)/(169473-ruler)+P)
    

def getarea(id,x,y,z):
    #print(int(x))
    xarea = np.unique(label_array[int(x),:, :], return_counts=True)
    xindex= np.where(xarea[0]==id)
    if len(xindex[0]) !=0:
        Xarea=xarea[1][xindex][0]
    else:
        Xarea='error'
    #print(xarea)
    #print(Xarea)
    #print(len(index[0]))

    yarea = np.unique(label_array[:,int(y), :], return_counts=True)
    yindex= np.where(yarea[0]==id)
    if len(yindex[0]) !=0:
        Yarea=yarea[1][yindex][0]
    else:
        Yarea='error'

    zarea = np.unique(label_array[:,:,int(z)], return_counts=True)
    zindex= np.where(zarea[0]==id)
    if len(zindex[0]) !=0:
        Zarea=zarea[1][zindex][0]
    else:
        Zarea='error'
    return Xarea,Yarea,Zarea
    #print(Xarea,Yarea,Zarea)

def Main():
    global List
    List=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    filelist = os.listdir(r"C:\Users\86159\Desktop\vuenii\public\all")
    for file in filelist:
        getall(file)
    print(List)
    shutil.rmtree(r"C:\Users\86159\Desktop\vuenii\public\all")  
    os.mkdir(r"C:\Users\86159\Desktop\vuenii\public\all")  
    return List

'''if __name__ == "__main__":
    Main()'''
        