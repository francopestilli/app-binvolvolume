#!/usr/bin/env python
"""
Created on Thu May 17 17:48:27 2018

@author: lindseykitchell
"""

import numpy as np
import nibabel as nib
import glob
import json
import os



with open('config.json') as config_json:
    config = json.load(config_json)
    

#asegstatsfile = config["fsurfer"]+"/stats/aseg.stats"
asegstatsfile = open(config["fsurfer"]+"/stats/aseg.stats", 'r')
lines =  asegstatsfile.readlines()
icv = float(lines[34][84:98]) 


volumes = {}
volumes_ICVprop = {}
volumes_ICVprop['eTIV'] = icv

for file in glob.glob(config["maskdir"] + "/*Vol.nii.gz"):
    tractname = os.path.basename(file)[0:-11]
    binvol = nib.load(file)
    header = binvol.header
    voxelvol = header.get_zooms()[0]*header.get_zooms()[1]*header.get_zooms()[2]
    num_vox = np.sum(binvol.get_data() > 0)
    vol = voxelvol*num_vox
    volumes[tractname] = vol
    volumes_ICVprop[tractname] = vol/icv

with open('volumes.json', 'w') as f:
    f.write(json.dumps(volumes, indent=4))
    
with open('volumes_icvproportion.json', 'w') as f:
    f.write(json.dumps(volumes_ICVprop, indent=4))
