import nibabel as nib
import os
import numpy as np

ed ="/cbica/home/bhaleram/comp_space/fets/new_scripts/Label_fusion/STAPLE/staple_python/ed/result.nii.gz"
et ="/cbica/home/bhaleram/comp_space/fets/new_scripts/Label_fusion/STAPLE/staple_python/et/result.nii.gz"
nec ="/cbica/home/bhaleram/comp_space/fets/new_scripts/Label_fusion/STAPLE/staple_python/nec/result.nii.gz"
aff = nib.load(ed).affine
#class 1
ed = nib.load(ed).get_fdata()
#class 2
et = nib.load(et).get_fdata()
#class 3
nec =  nib.load(nec).get_fdata()
for x in range(240):
    for y in range(240):
        for z in range(155):
            print(x,y,z)
            pos = np.argmax([ed[x,y,z],et[x,y,z],nec[x,y,z]])
            if pos == 0:
                et[x,y,z]*=0
                nec[x,y,z]*=0
            if pos == 1:
                ed[x,y,z]*=0
                nec[x,y,z]*=0
            if pos == 2:
                et[x,y,z]*=0
                ed[x,y,z]*=0

ed = (ed>=0.5).astype(int)
et = (et>=0.5).astype(int)
nec = (nec>=0.5).astype(int)

seg_final = ed*2 + et*4 + nec*1
seg = nib.Nifti1Image(seg_final,aff)
nib.save(seg,"/cbica/home/bhaleram/comp_space/fets/new_scripts/Label_fusion/STAPLE/staple_python/staple.nii.gz")

