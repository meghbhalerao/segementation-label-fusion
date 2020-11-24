#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 16:24:24 2019
@author: bhaleram
# This is the ENTRY POINT OF THE STAPLE ALGORITHM
Console script for staple
"""

import sys 
import click

import SimpleITK as sitk
from staple import STAPLE, get_images

@click.command()
@click.argument('input_files', nargs = -1, type = click.Path(exists=True))
@click.argument('output_file', nargs = 1, type = click.Path())
@click.option('--verbose/--no-verbose', default = False)
@click.option('--binarize/--probablities', default = True)
@click.option('--convergence-threshold')
def main(input_files, output_file, verbose, binarize, convergence_threshold):
    images = get_images(input_files)
    arrays = [sitk.GetArrayFromImage(image) for image in images]
    staple = STAPLE(arrays, verbose = verbose, convergence_threshold = convergence_threshold)
    output_array = staple.run()
    click.echo('Sensitivities: {}'.format(staple.sensitivity.flatten()))
    click.echo('Specificities: {}'.format(staple.specificity.flatten()))
    output_image = sitk.GetImageFromArray(output_array)
    one_image = images[0]
    if binarize:
        output_image = sitk.BinaryThreshold(output_image, 0.5)
    output_image.SetSpacing(one_image.GetSpacing())
    output_image.SetOrigin(one_image.GetOrigin())
    output_image.SetDirection(one_image.GetDirection())
    sitk.WriteImage(output_image, output_file)
    return 0



if __name__ == "__main__":
    sys.exit(main())
        
    
