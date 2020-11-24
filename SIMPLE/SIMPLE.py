import numpy as np
import nibabel as nib 
from utils import * 
from losses import *
#list of the segmentation paths as the input 
def SIMPLE(seg_path_list):
    seg_sum = np.zeros((4,240,240,155),dtype=float) # placeholder for storing the sum of the segmentations
    for seg in seg_path_list:
        seg = nib.load(seg).get_fdata()
        seg = one_hot_nonoverlap(seg.astype(int))
        seg_sum+=seg
    init_seg = (seg_sum/len(seg_path_list)>(0.5)).astype(int) # Taking the average of the input segmentations and initializing it as the starting point of SIMPLE algorithm
    dice_list = []
    for seg in seg_path_list:
        seg = nib.load(seg).get_fdata()
        seg = one_hot_nonoverlap(seg.astype(int))
        dice_score = 1 - MCD_loss(seg,init_seg,4)
        dice_list.append(dice_score)
    num_iter = len(seg_path_list) - 1  
    print(dice_list) # Just printing out the dice list i.e dice of the individual segmentations
#Here the iterative procedure starts 
    for i in range(num_iter): # Number of iterating to be done for the SIMPLE algorithm
        order = np.array(dice_list).argsort()
        del dice_list[order[0]] 
        del seg_path_list[order[0]] # No idea why I am doing this
        print(dice_list)
        dice_list = []
        for seg in seg_path_list: # Iterating thru the seg path list to get the list of dice scores
            seg = nib.load(seg).get_fdata()
            seg = one_hot_nonoverlap(seg.astype(int))  
            dice_score = 1 - MCD_loss(seg,init_seg,4)
            dice_list.append(dice_score)
        j = 0
        for seg in seg_path_list: # Iterating through the path of the segmentations
            seg = nib.load(seg).get_fdata()
            seg = one_hot_nonoverlap(seg.astype(int))  
            seg_sum+=dice_list[j]*seg # This is part of the logic of the SIMPLE algorithm
            #seg_sum+=seg
            j+=1
        init_seg = (seg_sum/(sum(dice_list))>0.5).astype(int)
        #init_seg = (seg_sum>(len(seg_path_list)/2)).astype(int) 
        seg_sum = seg_sum*0
    return init_seg
seg = SIMPLE(["/cbica/home/bhaleram/comp_space/fets/Indiviual_Labels/DeepMedic/validation/BraTS19_CBICA_AAM_1.nii.gz","/cbica/home/bhaleram/comp_space/fets/Indiviual_Labels/ResUNet/validation/BraTS19_CBICA_AAM_1.nii.gz","/cbica/home/bhaleram/comp_space/fets/Indiviual_Labels/UNet/validation/BraTS19_CBICA_AAM_1.nii.gz","/cbica/home/bhaleram/comp_space/fets/Docker_Repos/brats/gbmnet-18/data/results/tumor_GBMNet18_class.nii.gz","/cbica/home/bhaleram/comp_space/fets/Docker_Repos/brats/mic-dkfz/data/results/tumor_isen2018_class.nii.gz","/cbica/home/bhaleram/comp_space/fets/Docker_Repos/brats/pvg-18/code/src/data/results/tumor_PVG_Unet_class.nii.gz"])
seg = convert_to_3D(seg)
seg = nib.Nifti1Image(seg,affine = np.eye(4))
nib.save(seg,"seg.nii.gz")
                           
