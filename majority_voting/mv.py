import os 
import numpy as np
from utils import *
import nibabel as nib

# This is the implementation of the majority voting algorithm,


def convert_to_3D(seg):
    seg = seg[0,:,:,:]*4 + seg[1,:,:,:]*1 + seg[2,:,:,:]*2 + seg[3,:,:,:]*0
    return seg

seg_path = "/cbica/home/bhaleram/comp_space/fets/new_scripts/Label_fusion/majority_voting/labels/"
seg_list = os.listdir(seg_path)
seg_sum = np.zeros((4,240,240,155),dtype=float)
for seg in seg_list:
    seg = nib.load(seg_path+seg).get_fdata()
    seg = one_hot_nonoverlap(seg.astype(int))
    seg_sum+=seg
seg = (seg_sum/len(seg_list)>(0.5)).astype(int)
seg = convert_to_3D(seg)
seg = nib.Nifti1Image(seg,affine = np.eye(4))
nib.save(seg,"seg.nii.gz")

