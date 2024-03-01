
The authors introduce the **LVOS: Long-Term Video Object Segmentation** benchmark dataset, comprising 220 videos totaling 421 minutes, representing the first densely annotated long-term video object segmentation (VOS) dataset. The videos within LVOS have an average duration of 1.59 minutes, with each frame meticulously and manually annotated through a semi-automatic annotation pipeline, addressing potential errors in tracking, segmentation, and prediction. 

<i>**Disclaimer:** Dataset is made of 220 sequences, meant to be played as 6-fps videos, but is presented as individual annotated frames. Additionaly, each object instance is presented with an id tag, and a caption tag. </i>

To ensure dataset quality, the authors meticulously select 220 videos from an initial pool of 600 720P-resolution candidate videos, maintaining a balance between video quality and representation. The resulting dataset encompasses 126,280 frames and 156,432 annotations, surpassing the combined size of other datasets. For training, validation, and testing purposes, the videos are partitioned into subsets while preserving distribution and video length characteristics, with 120 videos designated for training, 50 for validation, and 50 for testing. Annotations for training and validation sets are publicly available, fostering the development of VOS methods, while those for the testing set remain private for competition purposes.

<img src="https://github.com/dataset-ninja/lvos/assets/115161827/9f875681-3bba-459e-a678-e55529caa832" alt="image" />
<span style="font-size: smaller; font-style: italic;">Example sequences of our Long-term Video Object Segmentation (LVOS)</span>

## Dataset Design

In addressing the absence of a dedicated dataset, LVOS strives to offer the community a new and specialized Video Object Segmentation (VOS) dataset for the training and assessment of resilient VOS models. The construction of LVOS adheres to the three principles outlined below.

1) **Long-Term VOS.** In the realm of Long-term Video Object Segmentation (VOS), LVOS distinguishes itself from existing datasets, wherein videos typically endure a mere 3-6 seconds. LVOS guarantees a more realistic representation by extending the duration of its videos to approximately 1.59 minutes (equivalent to 574 frames at 6 FPS), which is approximately 20 times longer than the brief duration of short-term videos, aligning more closely with real-world applications.

2) **Dense and high-quality annotation.** The labor-intensive process of mask annotation significantly limits the temporal scope and size of existing Video Object Segmentation (VOS) datasets. In order to train resilient VOS models and evaluate their effectiveness in practical scenarios, the creation of high-quality and densely annotated masks is imperative. Consequently, all frames within LVOS undergo meticulous manual annotation, facilitated through a semi-automatic annotation pipeline to ensure precision.

3) **Comprehensive labeling.** A category set with relevance to daily life is meticulously designed, comprising 5 parent classes and 27 subclasses. It is important to highlight that these 27 categories extend beyond the COCO dataset, incorporating additional classes, including, for instance, frisbee. Within the 27 categories, 7 are designated as unseen categories, strategically chosen to enhance the evaluation of model generalization capabilities.


## Semi-Automatic Annotation Pipeline

The fatigue induced by the mask annotation process significantly curtails the scale of Video Object Segmentation (VOS) datasets. To address this limitation, the authors introduce an innovative semi-automatic annotation pipeline aimed at enhancing the efficiency of frame annotation. This pipeline is specifically structured into four distinct steps.

<img src="https://github.com/dataset-ninja/lvos/assets/115161827/33d8eb05-0e2e-41bc-b877-2a889d20991c" alt="image" />

<span style="font-size: smaller; font-style: italic;">Annotation Pipeline, comprising four sequential steps. Step 1: 1 FPS Automatic Segmentation, where instance segmentation and tracking models are employed to automatically obtain the mask of the target object at 1 FPS. In Step 2, 1 FPS Manual Correction is performed, refining the masks obtained in Step 1 through manual adjustments. Step 3, Mask Propagation from 1 FPS to 6 FPS, involves extending the masks from 1 FPS to 6 FPS using a Video Object Segmentation (VOS) model. Finally, Step 4 entails 6 FPS Manual Correction, where the masks obtained in Step 3 are manually corrected.</span>

**Step 1: 1 FPS Automatic Segmentation.** Initially, the authors employ transfiner to produce pixel-wise segmentation for each object in the frames at a rate of 1 frame per second (FPS). Subsequently, the bounding boxes of the target objects are manually marked when they first appear, and MixFormer is utilized to propagate the box from the initial frame to all subsequent frames. By integrating information from pixel-wise segmentation and bounding boxes in each frame, the masks of the target objects are obtained at a rate of 1 FPS.

**Step 2: 1 FPS Manual Correction.** Potential inaccuracies or the absence of target object masks in certain frames may arise from tracking errors, segmentation defects, and other prediction errors. To address this, the authors employ EISeg ([GitHub](https://github.com/PaddleCV-SIG/EISeg)), an Efficient Interactive Segmentation Tool based on [PaddlePaddle](https://www.paddlepaddle.org.cn/en), to refine the masks. On average, around 30% of frames require correction through this refinement process.

**Step 3: Mask Propagation.** The authors employ a Video Object Segmentation (VOS) model, specifically AOT, to automatically extend the annotation masks obtained at 1 FPS in Step 2 to their adjacent unlabeled frames. This extension results in an increased frame rate from 1 FPS to 6 FPS.

**Step 4: 6 FPS Manual Correction.** Due to imperfections in masks segmented by the Video Object Segmentation (VOS) model, each frame is artificially corrected until satisfactory results are achieved. Approximately 40% of frames necessitate additional refinement in this step.

## Time and Quality Analysis

To assess annotation quality, the authors randomly select 100 videos from the HQYouTubeVIS training set and reannotate them using their semi-automatic annotation pipeline. Comparing the results with the ground truth, the average Intersection over Union (IoU) score is 0.93, indicating substantial consistency between the annotation results and ground truth, thereby validating the effectiveness of the pipeline. Additionally, annotators record the total time overheads, revealing that, on average, one annotator can label an entire long-term video (500 frames at 6 FPS) in 60 minutes using the pipeline, whereas a skilled annotator would spend 1500 minutes using the traditional method (3 minutes for one frame). The pipeline proves to be a significant cost-reduction tool while maintaining annotation quality.

## Attributes 

<i>**Disclaimer:** The entirety of the following data is sourced directly from the original paper and regrettably lacks representation in the dataset metadata. </i>

| Attribute       | Definition                                                             |
|-----------------|------------------------------------------------------------------------|
| BC              | Background Clutter. The appearances of background and target object are similar. |
| DEF             | Deformation. Target appearance deforms complexly.                     |
| MB              | Motion Blur. Boundaries of target object are blurred due to camera or object fast motion. |
| FM              | Fast Motion. The per-frame motion of the target is larger than 20 pixels, computed as the centroid's Euclidean distance. |
| LR              | Low Resolution. The average ratio between the target box area and the image area is smaller than 0.1. |
| OCC             | Occlusion. The target is partially or fully occluded in the video.     |
| OV              | Out-of-view. The target leaves the video frame completely.             |
| SV              | Scale Variation. The ratio of any pair of bounding boxes is outside the range [0.5, 2.0]. |
| DB              | Dynamic Background. Background regions undergo deformation.           |
| SC              | Shape Complexity. Boundaries of the target object are complex.         |
| AC              | Appearance Change. Significant appearance change due to rotations and illumination changes. |
| ---             | ---                                                                    |
| LRA             | Long-term Reappearance. Target object reappears after disappearing for at least 100 frames. |
| CTC             | Cross-temporal Confusion. There are multiple different objects that are similar to the target object but do not appear at the same time




<span style="font-size: smaller; font-style: italic;"> The table provides definitions for video attributes in LVOS, extending and modifying the previously defined short-term video challenges (top). This extension includes a complementary set of long-term video attributes (bottom). </span>

For a thorough and extensive analysis of Video Object Segmentation (VOS) approaches, it is crucial to identify video attributes. Each sequence is labeled with 13 challenges, as outlined in the provided table. These attributes encompass challenges specific to short-term videos, derived from DAVIS, and are augmented with an additional set tailored for long-term videos. Notably, these attributes are not mutually exclusive, allowing for the presence of multiple challenges within a single video. In LVOS, common challenges include Scale Variation (SV), Occlusion (OCC), Low Resolution (LR), and Fast Motion (FM). A notable distinction is observed in challenges between short-term and long-term videos, attributed to the extended length of the latter, resulting in more complex and varied object motion and background changes not readily apparent in short-term videos. The variation in attribute distribution imposes distinct and heightened requirements on the design of VOS models.

| Attributes distribution of each sequence in LVOS | Main mutual dependencies among attributes | Distribution comparison with DAVIS 2017 |
|:--------------:|:------------------:|:-----------------:|
| <img  src="https://github.com/dataset-ninja/lvos/assets/115161827/e5818309-233a-4ceb-ac95-5532a2db0152">           | <img src="https://github.com/dataset-ninja/lvos/assets/115161827/17bf5e0e-ac97-44c4-9678-3d9399179f6c">           | <img src="https://github.com/dataset-ninja/lvos/assets/115161827/16aa5982-87f5-43bc-84b9-41fb3ce67517">      |