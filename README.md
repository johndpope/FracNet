# FracNet
A deep learning segmentation model for rib fracture detection.

## Abstract
*Background*: Diagnosis of rib fractures plays an important role in identifying trauma severity. However, quickly and precisely identifying the rib fractures in a large number of CT images with increasing number of patients is a tough task, which is also subject to the qualification of radiologist. We aim at a clinically applicable automatic system for rib fracture detection and segmentation from CT scans.
*Methods*: A total of 7,473 annotated traumatic rib fractures from 900 patients in a single center were enrolled into our dataset, named RibFrac Dataset, which were annotated with a human-in-the-loop labeling procedure. We developed a deep learning model, named FracNet, to detect and segment rib fractures. 720, 60 and 120 patients were randomly split as training cohort, tuning cohort and test cohort, respectively. FreeResponse ROC (FROC) analysis was used to evaluate the sensitivity and false positives of the detection performance, and Intersection-over-Union (IoU) and Dice Coefficient (Dice) were used to evaluate the segmentation performance of predicted rib fractures. Observer studies, including independent human-only study and human-collaboration study, were used to benchmark the FracNet with human performance and evaluate its clinical applicability. A annotated subset of RibFrac Dataset, including 420 for training, 60 for tuning and 120 for test, as well as our code for model training and evaluation, was open to research community to facilitate both clinical and engineering research.
*Findings*: Our method achieved a detection sensitivity of 92.9% with 5.27 false positives per scan and a segmentation Dice of 71.5%on the test cohort. Human experts achieved much lower false positives per scan, while underperforming the deep neural networks in terms of detection sensitivities with longer time in diagnosis. With human-computer collobration, human experts achieved higher detection sensitivities than human-only or computer-only diagnosis.
*Interpretation*: The proposed FracNet provided increasing detection sensitivity of rib fractures with significantly decreased clinical time consumed, which established a clinically applicable method to assist the radiologist in clinical practice.

For more details, please refer to our paper: 

**Deep-learning-assisted detection and segmentation of rib fractures from CT scans: Development and validation of FracNet**

*Liang Jin, [Jiancheng Yang](http://jiancheng-yang.com/), [Kaiming Kuang](http://kaimingkuang.github.io/), [Bingbing Ni](https://scholar.google.com/citations?user=eUbmKwYAAAAJ), Yiyi Gao, Yingli Sun, Pan Gao, Weiling Ma, Mingyu Tan, Hui Kang, Jiajun Chen, Ming Li*

EBioMedicine ([DOI](https://doi.org/10.1016/j.ebiom.2020.103106))

## Code Structure
* FracNet/
    * [`dataset/`](dataset/): PyTorch dataset and transforms.
    * [`models/`](models/): PyTorch 3D UNet model and losses.
    * [`utils/`](/utils): Utility functions.
    * [`main.py`](main.py): Training script.

# TODO
* [ ] DataLoader
* [ ] Models
* [ ] Training
* [ ] Evaluation from ribfrac-challenge
 
