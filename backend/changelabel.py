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
OLD_NAME=['背景','脾脏','右肾','左肾','胆囊','食管','肝脏','胃','主动脉','下腔静脉','胰腺','右肾上腺','左肾上腺','十二指肠','膀胱','前列腺/子宫',]
NEW_NAME=['背景','脾脏','右肾','左肾','胆囊','食管','肝脏','胃','主动脉','下腔静脉','胰腺','膀胱']
def changelabels(filepath,list):
    Label = sitk.ReadImage(filepath)
    Label_array = sitk.GetArrayFromImage(Label)
    need=[]
    for i in list:
        need.append(NEW_NAME[int(i)])
    for i in range(len(OLD_NAME)):
        if OLD_NAME[i] not in need :
            Label_array[Label_array == i] = 0

    temp_image = sitk.GetImageFromArray(Label_array.astype(np.uint8))
    temp_image.SetOrigin(Label.GetOrigin())
    temp_image.SetSpacing(Label.GetSpacing())
    temp_image.SetDirection(Label.GetDirection())
    sitk.WriteImage(temp_image, r"C:\Users\86159\Desktop\vuenii\public\15972129987\after\change\\"+"1.nii.gz")
