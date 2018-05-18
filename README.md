# app-binvolvolume
This service computes the volume of binary nifti images and reads the eTIV (estimated total intracranial volume aka icv) from freesurfer (http://freesurfer.net/fswiki/eTIV). It saves down the raw volumes (volumes.json) as well as the proportion of ICV (volumes_icvproportion.json) for each image (volume normalized by eTIV - vol/eTIV). 
