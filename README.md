[![Abcdspec-compliant](https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg)](https://github.com/brain-life/abcd-spec)
[![Run on Brainlife.io](https://img.shields.io/badge/Brainlife-bl.app.32-blue.svg)](https://doi.org/10.25663/bl.app.32)

# app-binvolvolume
This service computes the volume of binary nifti images and reads the eTIV (estimated total intracranial volume aka icv) from freesurfer (http://freesurfer.net/fswiki/eTIV). It saves down the raw volumes (volumes.json) as well as the proportion of ICV (volumes_icvproportion.json) for each image (volume normalized by eTIV - vol/eTIV).

### Author
- Lindsey Kitchell (kitchell@indiana.edu)

### Contributors
- Soichi Hayashi (hayashis@iu.edu)

### Funding 
[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-1636893](https://img.shields.io/badge/NSF_BCS-1636893-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1636893)


## Running the App 

### On Brainlife.io

You can submit this App online at [https://doi.org/10.25663/bl.app.32](https://doi.org/10.25663/bl.app.32) via the "Execute" tab.

### Running Locally (on your machine)

1. git clone this repo.
2. Inside the cloned directory, create `config.json` with something like the following content with paths to your input files.

```json
{
        "fsurfer": "../5b96cf5f161e01002a3206fb/5967bffa9b45c212bbec8958/output",
    "maskdir": "../5b96cf5f161e01002a3206fb/5b26aab9d821b2004f932b05/masks"
}
```

If you have singularity installed on your local machine:

3. Launch the App by executing `main`

```bash
./main
```

Otherwise:

3. Execute main.py in python.


### Sample Datasets

If you don't have your own input file, you can download sample datasets from Brainlife.io, or you can use [Brainlife CLI](https://github.com/brain-life/cli).


## Output

The main output of this App is two files called `volumes.json` and `volumes_icvproportion.json`. These files are .json files containing the volume and volume/eTIV for each binary image in the input folder.
 

### Dependencies

This App only requires [singularity](https://www.sylabs.io/singularity/) to run. If you don't have singularity, you will need to install following dependencies.  

  - NiBabel: http://nipy.org/nibabel/

