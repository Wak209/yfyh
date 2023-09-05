import nibabel as nib
import numpy as np
import matplotlib.pyplot as plt
import cv2
def get_shape(filepath):
    img = nib.load(filepath)
    data = img.get_fdata()
    #print(data.shape)
    return data.shape
