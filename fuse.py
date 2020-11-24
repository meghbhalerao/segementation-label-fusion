import numpy as np
import nibabel as nib 
from utils import * 

def convert_to_3D(seg):
    seg = seg[0,:,:,:]*4 + seg[1,:,:,:]*1 + seg[2,:,:,:]*2 + seg[3,:,:,:]*0
    return seg



def majority_voting(seg_DeepMedic,seg_UNet,seg_ResUNet,seg_FCN,seg_UInc):
    aff = nib.load(seg_UNet).affine
    dm = nib.load(seg_DeepMedic).get_fdata()
    unet = nib.load(seg_UNet).get_fdata()
    resunet = nib.load(seg_ResUNet).get_fdata()
    fcn = nib.load(seg_FCN).get_fdata()
    uinc = nib.load(seg_UInc).get_fdata()
    dm = one_hot_nonoverlap(dm.astype(int))
    unet = one_hot_nonoverlap(unet.astype(int)) 
    resunet = one_hot_nonoverlap(resunet.astype(int))
    fcn = one_hot_nonoverlap(fcn.astype(int))
    seg = dm + unet + resunet + fcn + uinc
    seg = (seg>2.5).astype(int)
    seg = convert_to_3D(seg)    
    seg = nib.Nifti1Image(seg,aff)
    return seg

def 
