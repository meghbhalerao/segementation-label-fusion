import os 
import numpy as np
import nibabel as nib
from utils import *
from losses import *
label_path = "/cbica/home/bhaleram/comp_space/fets/new_scripts/Label_fusion/calculate_dice/labels/"
gt = np.expand_dims(one_hot_nonoverlap(nib.load("gt.nii.gz").get_fdata()),axis=0)
for label in os.listdir(label_path):
    seg = np.expand_dims(one_hot_nonoverlap(nib.load(label_path+label).get_fdata()),axis=0)
    et_loss,nec_loss,ed_loss,bag_loss= MCD_loss_2(seg,gt)
    print("The Individual Class Dice Scores for "+label+" are:")
    #print("Enhancing Tumor Dice:", 1-et_loss)
    #print("Necrosis Tumor Dice:", 1-nec_loss)
    #print("Edema Tumor Dice:", 1-ed_loss)
    #print("Background Tumor Dice:", 1-bag_loss)
    print("The average dice score is:",1- (et_loss+nec_loss+ed_loss+bag_loss)/4)
