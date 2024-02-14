**LVOS: Long-term Video Object Segmentation** is a dataset for instance segmentation, semantic segmentation, object detection, and identification tasks. It is applicable or relevant across various domains. 

The dataset consists of 126289 images with 117151 labeled objects belonging to 1 single class (*object*).

Images in the LVOS dataset have pixel-level instance segmentation annotations. Due to the nature of the instance segmentation task, it can be automatically transformed into a semantic segmentation (only one mask for every class) or object detection (bounding boxes for every object) tasks. There are 31917 (25% of the total) unlabeled images (i.e. without annotations). There are 3 splits in the dataset: *train* (65237 images), *val* (31158 images), and *test* (29894 images). The dataset was released in 2023 by the Fudan University, China.

Here are the visualized examples for the classes:

[Dataset classes](https://github.com/dataset-ninja/lvos/raw/main/visualizations/classes_preview.webm)