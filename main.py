#!/usr/bin/env python
"""
Created on Thu May 17 17:48:27 2018

@author: lindseykitchell
"""

import numpy as np
import nibabel as nib
import glob
import json



with open('config.json') as config_json:
    config = json.load(config_json)
    

volumes = {}

for file in glob.glob(config["maskdir"] + "/*Vol.nii.gz"):
    tractname = file[0:-11]
    binvol = nib.load(file)
    header = binvol.header
    voxelvol = header.get_zooms()[0]*header.get_zooms()[1]*header.get_zooms()[2]
    num_vox = np.sum(binvol.get_data() > 0)
    vol = voxelvol*num_vox
    volumes[tractname] = vol

with open('volumes.json', 'w') as f:
    f.write(json.dumps(volumes, indent=4))