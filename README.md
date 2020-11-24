# segementation-label-fusion
Different Label Fusion Approaches for segmentation masks 
## Instructions to do STAPLE Label Fusion:
First, `cd` to the `STAPLE` Folder
1. Entry point is `cli.py` file. 
2. Run `cli.py` using `run.sh`.
3. Open the `run.sh` to see what parameters to be passed.
4. The parameters that need to be passed are the list of segmentations of **individual** classes, since `STAPLE` operates on individual classes.

## Instructions to do SIMPLE Label Fusion:
1. `cd` to the `SIMPLE` Folder
2. Run the `SIMPLE.sh` to run the **SIMPLE** algorithm. Make sure the paths to the individual segmentations exist (This applies to the above also)

## Instructions to do Majority Voting Label Fusion:
1. `cd` to the `majority_voting` Folder
2. Run the `mv.sh` to run the **Majority Voting** algorithm.

