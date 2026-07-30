<div align="center">

## 7CCSMPRJ Individual Project
# Transformer-Based Traversability Prediction and Terrain Segmentation for Off-Road Autonomous Ground Vehicles

### King's College London – MSc Advanced Computing
Noel Varga

<i>I verify that I am the sole author of the programs contained in this archive, except where explicitly stated to the contrary</i>

~~[<a href=#>Thesis documentation</a>]~~ // To be available

</div>

<br>
<br>
<br>

# OVERVIEW

This dissertation was developed for the degree of MSc in Advanced Computing. 

<br>
<br>
<br>

# INITIALISATION

## Step 1) Clone repository

```bash
git clone https://github.com/NoelVar/Transformer-Based-Terrain-Perception-for-Off-Road-Environments
cd Transformer-Based-Terrain-Perception-for-Off-Road-Environments
```

## Step 2) Create and activate Conda environment

```bash
conda env create -f environment.yml                                                 
conda activate offroad-dissertation
```

## Step 3) Install PyTorch and verify download
```bash
pip install torch==2.1.0 torchvision==0.16.0 --index-url https://download.pytorch.org/whl/cu118                      
```
```bash
python -c "import torch; print(torch.__version__); print(torch.cuda.is_available())"
```

## Step 4) Install OpenMIM and verify download
```bash
pip install -U openmim 
```
```bash
mim --version
```

## Step 5) Install mmengine, and mmcv 
```bash
mim install mmengine 
mim install mmcv==2.1.0    
```

## Step 6) Install MMSegmentation framework from the Google Drive link below
This project depends on a modified version of MMSegmentation containing:
- custom dataset registrations
- modified model implementations
- custom training configurations
<div align="center">
    [<a href="https://drive.google.com/file/d/1yJewPuMaIOBoTLOWoV4D2BAHEEgTOq77/view?usp=sharing">mmsegmentation.zip</a>]
</div>

## Step 7) Extract the mmsegmentation.zip folder into the root folder of the project
```bash
Transformer-Based-Terrain-Perception-for-Off-Road-Environments
│
├── config/
├── notebooks/
├── scripts/
├── src/
├── mmsegmentation/ '<== ADDED'
├── .gitignore
├── README.md
├── environment.yml
├── requirements.txt
└── test.py
```

## Step 8) Install mmsegmentation
Run the command from the root directory
```bash
pip install -e ./mmsegmentation
```

## Step 9) Verify installation
Run the script in the root project folder to see if the packages are installed successfully (<i>The output should be "Success"</i>).
```bash
python ./test.py
```

## Step 10) Download the processed dataset
The processed data contains the split files and converted annotations for both datasets. The following link allows to download the processed data from Google Drive:
<div align="center">
    [<a href="https://drive.google.com/drive/folders/1jI_yRuMDHR2xNYuFdz1HuszxXuR820hu?usp=sharing">processed data</a>]
</div>

## Step 11) Create the data directory and place processed data
```bash
Transformer-Based-Terrain-Perception-for-Off-Road-Environments
│
├── config/
├── data/ '<== CREATED'
│   └── processed/ '<== ADD "processed" HERE'
├── notebooks/
├── scripts/
├── src/
├── mmsegmentation/
├── .gitignore
├── README.md
├── environment.yml
├── requirements.txt
└── test.py
```

## Step 12) OPTIONAL: Download RUGD and RELLIS datasets
To reproduce the data analysis and pre-processing download the original datasets following the links below:

- For RUGD download:
    - Raw Video Frames with Annotations. Extract the archive, and rename the extracted folder from "RUGD_frames-with-annotations" to "images"
    - RGB Annotation Files. Extract the archive, and rename the extracted folder from "RUGD_annotations" to "annotations"

Extract them so that your directory structure becomes

```text
data/
└── RUGD/
    ├── images/
    └── annotations/
```

- For RELLIS-3D download:
    - Full Images. Extract the archive, and rename the extracted folder from "Rellis-3D" to "images"
    - Full Image Annotations ID Format. Extract the archive, and rename the extracted folder from "Rellis-3D" to "annotations"

Extract them so that your directory structure becomes

```text
data/
└── RELLIS-3D/
    ├── images/
    └── annotations/
```

<div align="center">
    [<a href="http://rugd.vision/#download">RUGD</a>]
    [<a href="https://github.com/unmannedlab/RELLIS-3D#image-download">RELLIS-3D</a>]
</div>

The final directory structure **must** match the following:

```bash
Transformer-Based-Terrain-Perception-for-Off-Road-Environments
│
├── config/
├── data/
│   ├── processed/
│   ├── RELLIS-3D/
│   │   ├── annotations/
│   │   └── images/
│   └── RUGD/
│       ├── annotations/
│       └── images/
├── notebooks/
├── mmsegmentation/
...
└── test.py
```

## Step 13) OPTIONAL: Download trained models and experiment results
To reproduce the evaluation of the results, download the results folder from the link below:
<div align="center">
    [<a href="https://drive.google.com/drive/folders/12flKLkAfe6npV8-vIFkpBXeYLyUCnLCZ?usp=sharing">results</a>]
</div>

The final directory structure **must** match the following:

```bash
Transformer-Based-Terrain-Perception-for-Off-Road-Environments
│
├── config/
├── data/
├── results/
├── notebooks/
├── mmsegmentation/
...
└── test.py
```

## Step 14) Run notebooks
To be able to run notebooks, the right Python interpreter needs to be selected.<br>
First find the "offroad-dissertation" environment path:
```bash
conda env list

"EXPECTED OUTPUT">> C:\..\..\anaconda3\envs\offroad-dissertation
```
Following this open the editor commands using Ctrl+Shift+P and select <i>"Python: Select Interpreter"</i>. <br>
From here, select <i>"Enter interpreter path.."</i> > <i>"Find..."</i> and navigate to the path previously revealed from the conda env list command. <br>
Once in the right directory e.g.: <i>"offroad-dissertation"</i> select the python.exe file. Now the notebook should run.

<br>
<br>
<br>

# REPOSITORY STRUCTURE:
```bash
Transformer-Based-Terrain-Perception-for-Off-Road-Environments
│
├── config/
├── data/
├── notebooks/
├── scripts/
├── src/ 
├── mmsegmentation/
├── results/ 
├── .gitignore
├── README.md
├── environment.yml
├── requirements.txt
└── test.py
```

## 1) config/
Contains information files from RUGD and RELLIS

### 1.1)config/rellis.yaml
Part of the downloaded RELLIS-3D dataset, which contains the class mapping information.

### 1.2) config/rugd.txt
Part of the downloaded RUGD dataset. Contains mapping information of classes.

## 2) data/
Contains the data to perform, analysis, pre-processing, split file creation, merging, dataset registration

### 2.1) data/processed
Contains data that has been processed as part of this project, for example: 
- Split files
- Configured annotation files (RGB -> ID)

### 2.2) data/RELLIS-3D & data/RUGD
Both folders contain their respective datasets, without any modifications.

## 3) notebooks/
Contains notebooks used to visualise results, or perform processing of data.

### 3.1) notebooks/eda
Contains exploratory data analysis. This includes analysis of the RELLIS-3D, and RUGD datasets separately, along with the merged four class datasets analysis. The four class merged datasets analysis contains distribution analysis along with calculation of the weights, for the weighted training of models.

### 3.2) notebooks/model_evaluation
The directory contains the evaluation of different models, along with the calculation of confusion matrix, recall, precision, F1-score, and IoU per-class for each model

## 4) results/
Contains each trained model, including best iteration, model setup, last 5 iterations.

## 5) scripts/
General python scripts used during development.

### 5.1) scripts/01_build_rugd_dataset.py & scripts/05_build_rugdrellis_dataset.py
These python files are used to test if the datasets were registered and built successfully

### 5.2) scripts/02_remap_classes_rugd.py & scripts/03_remap_classes_rellis.py
The purpose of these scripts is to re-map the annotation id's of both datasets to match the four class configuration established in the report.

### 5.3) scripts/04_symlink_images.py
Used to create a symlink of the image folders for both datasets, to reduce the amount of space needed for storing the same images.

## 6) src/
Contains python files that are used for dataset processing or result evaluation.

### 6.1) src/datasets/01_rugd_processing.py
Script to write the split files for RUGD.

### 6.2) src/datasets/02_split_combination.py
Used to write the combined split file of RUGD and RELLIS-3D merged dataset.

### 6.3) src/evaluation/01_rugd_deeplabv3_5000.py & src/evaluation/02_rugd_deeplabv3_16000.py
Used to create visual prediction files. These files are used in the notebooks.

### 6.4) src/utils/convert_rgb2id.py
Converts RUGD's annotation files from RGB to ID representation. The script is ran in rugd_analysis.ipynb. To use add the following to settings.json in .vscode folder:

```bash
{
    "python-envs.defaultEnvManager": "ms-python.python:conda",
    "python-envs.defaultPackageManager": "ms-python.python:conda",
    "python.analysis.extraPaths": [
        "./src/utils",
        "./mmsegmentation"
    ]
}
```

Or go to cell number 13 (<i>right after the title "Convert to grayscale (rgb -> id)"</i>), hover over "<i>convert_rgb2id</i>" click "<i>Quick Fix</i>" select "<i>Add './Transformer-Based-Terrain-Perception-for-Off-Road-Environments/src/utils' to extraPaths</i>".

<br>
<br>
<br>

# TRAINING
The models were trained and tested using Google Colab. Please ensure to follow the guidance provided in the notebook to train and test models. Find the training environment here:
<div align="center">
    [<a href="https://colab.research.google.com/drive/1vgOkMc9VzoKNOC2YNfY1hH6_3dgL3kmV?usp=sharing">Google Colab notebook</a>]
</div>

<br>
<br>
<br>

# REPRODUCIBILITY
This repository contains the processes used to prepare the data and models for training, and evaluate the results. The training process has been conducted on Google Collaboratory. 

Due to GitHub file size limitations, the modified MMSegmentation framework, processed datasets, and trained model outputs are hosted separately on Google Drive.

Furthermore, some paths in the code may require to be configured to match the local path of the used computer.

---