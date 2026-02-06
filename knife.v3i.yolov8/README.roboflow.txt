
knife - v3 2026-02-02 2:41am
==============================

This dataset was exported via roboflow.com on February 2, 2026 at 7:13 AM GMT

Roboflow is an end-to-end computer vision platform that helps you
* collaborate with your team on computer vision projects
* collect & organize images
* understand and search unstructured image data
* annotate, and create datasets
* export, train, and deploy computer vision models
* use active learning to improve your dataset over time

For state of the art Computer Vision training notebooks you can use with this dataset,
visit https://github.com/roboflow/notebooks

To find over 100k other datasets and pre-trained models, visit https://universe.roboflow.com

The dataset includes 3909 images.
Knife are annotated in YOLOv8 format.

The following pre-processing was applied to each image:
* Resize to 640x640 (Fit (black edges))

The following augmentation was applied to create 3 versions of each source image:
* 50% probability of horizontal flip
* Randomly crop between 0 and 10 percent of the image
* Random shear of between -5° to +5° horizontally and -0° to +0° vertically
* Random brigthness adjustment of between -20 and +20 percent
* Random Gaussian blur of between 0 and 1.5 pixels
* Salt and pepper noise was applied to 0.1 percent of pixels


