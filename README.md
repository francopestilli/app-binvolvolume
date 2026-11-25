<h1 align="center">Compute Volume of Binary Nifti images</h1>

<p align="center">
  Computes the volume of each binary tract mask and its proportion of FreeSurfer estimated total intracranial volume (eTIV), saved as JSON.
</p>

<p align="center">
  <a href="https://github.com/brainlife/abcd-spec"><img src="https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg" alt="ABCD Spec v1.1"></a>
  <a href="https://doi.org/10.25663/bl.app.32"><img src="https://img.shields.io/badge/Brainlife-bl.app.32-blue.svg" alt="Run on brainlife.io"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-see_LICENSE-lightgrey.svg" alt="License"></a>
</p>

## At a glance

<!-- brainlife-app:begin (generated from the App manifest; edit the manifest, not this block) -->

> **Computes the volume of each binary tract mask and its proportion of FreeSurfer estimated total intracranial volume (eTIV), saved as JSON.**

Reads eTIV from the FreeSurfer stats/aseg.stats file, counts non-zero voxels in every *Vol.nii.gz mask in the input directory, multiplies by voxel volume and writes volumes.json (mm^3) and volumes_icvproportion.json (volume/eTIV). Use it to quantify tract volumes normalised for head size.

| | |
|---|---|
| **Inputs** | `neuro/freesurfer` · `neuro/tractmasks` |
| **Outputs** | `raw` |
| **Container** | `brainlife/dipy:0.13` |
| **Resources** | 8 CPUs · 0.25 h walltime |
| **Run it** | [doi.org/10.25663/bl.app.32](https://doi.org/10.25663/bl.app.32) |

#### Inputs

| Input | Datatype | Required | Description |
|---|---|---|---|
| `fsurfer` | `neuro/freesurfer` | yes | FreeSurfer subject directory used for eTIV. Must contain stats/aseg.stats. |
| `vols` | `neuro/tractmasks` | yes | Directory of binary tract masks. Only files ending in Vol.nii.gz are measured. |

#### Outputs

| Output | Datatype | Description |
|---|---|---|
| `output` | `raw` | volumes.json (volume per mask in mm^3) and volumes_icvproportion.json (volume divided by eTIV, plus eTIV). |

<!-- brainlife-app:end -->

## Running the App

### On brainlife.io

Open the App at [doi.org/10.25663/bl.app.32](https://doi.org/10.25663/bl.app.32), choose `neuro/freesurfer`, `neuro/tractmasks` from your project and press **Execute**. The results are saved to your project as `raw`.

### Locally

You need [Singularity/Apptainer](https://apptainer.org/) (the App runs in `brainlife/dipy:0.13`), [`jq`](https://jqlang.github.io/jq/).

1. Clone this repository.
2. Create `config.json` with the paths to your inputs and the parameters:

   ```json
   {
       "fsurfer": "/path/to/fsurfer/fsurfer",
       "maskdir": "/path/to/vols/maskdir"
   }
   ```

3. Run `./main`.

## Citing

If you use this App, please cite it, the software it builds on and brainlife.io:

- Compute Volume of Binary Nifti images. brainlife.io App. [doi:10.25663/bl.app.32](https://doi.org/10.25663/bl.app.32)
- Fischl. FreeSurfer. *NeuroImage* 62:774-781 (2012). [doi:10.1016/j.neuroimage.2012.01.021](https://doi.org/10.1016/j.neuroimage.2012.01.021)
- Garyfallidis et al. Dipy, a library for the analysis of diffusion MRI data. *Frontiers in Neuroinformatics* 8 (2014). [doi:10.3389/fninf.2014.00008](https://doi.org/10.3389/fninf.2014.00008)
- Hayashi S, Caron BA, Heinsfeld AS, et al. brainlife.io: a decentralized and open-source cloud platform to support neuroscience research. *Nature Methods* 21:809–813 (2024). [doi:10.1038/s41592-024-02237-2](https://doi.org/10.1038/s41592-024-02237-2)
- Avesani P, McPherson B, Hayashi S, et al. The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services. *Scientific Data* 6:69 (2019). [doi:10.1038/s41597-019-0073-y](https://doi.org/10.1038/s41597-019-0073-y)

## Authors

- Lindsey Kitchell

**Contributors**

- Soichi Hayashi

## Funding

[![Wellcome-226486/Z/22/Z](https://img.shields.io/badge/Wellcome-226486%2FZ%2F22%2FZ-purple.svg)](https://wellcome.org/)
[![NIH-NINDS-U24NS140384](https://img.shields.io/badge/NIH_NINDS-U24NS140384-green.svg)](https://reporter.nih.gov/project-details/11261037)
[![NIH-NINDS-UM1NS132207](https://img.shields.io/badge/NIH_NINDS-UM1NS132207-green.svg)](https://reporter.nih.gov/project-details/11411328)
[![NIH-NIBIB-R01EB029272](https://img.shields.io/badge/NIH_NIBIB-R01EB029272-green.svg)](https://reporter.nih.gov/project-details/10262925)
[![NIH-NIBIB-R01EB030896](https://img.shields.io/badge/NIH_NIBIB-R01EB030896-green.svg)](https://reporter.nih.gov/project-details/10428625)
[![NIH-NIMH-R01MH126699](https://img.shields.io/badge/NIH_NIMH-R01MH126699-green.svg)](https://reporter.nih.gov/project-details/10460628)
[![NIH-NIDCD-R01DC020088](https://img.shields.io/badge/NIH_NIDCD-R01DC020088-green.svg)](https://reporter.nih.gov/project-details/11140284)
[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-2203524](https://img.shields.io/badge/NSF_BCS-2203524-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2203524)
[![NSF-IIS-1636893](https://img.shields.io/badge/NSF_IIS-1636893-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-OAC-2148729](https://img.shields.io/badge/NSF_OAC-2148729-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2148729)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NSF-IIS-2148700](https://img.shields.io/badge/NSF_IIS-2148700-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2148700)
[![NSF-OAC-1916518](https://img.shields.io/badge/NSF_OAC-1916518-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1916518)

<sub>brainlife.io, which runs this App, is publicly funded by Wellcome, the U.S. National Institutes of Health and the U.S. National Science Foundation; acknowledging that support helps keep it running.</sub>

## License

See [LICENSE](LICENSE).
