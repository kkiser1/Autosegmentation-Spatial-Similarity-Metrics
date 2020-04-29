# Novel Autosegmentation Accuracy Metrics
__________________________________

### Code for calculating the added path length, added path volume, and corrections path length between an automated segmentation and its corresponding expert-corrected segmentation. 

The added path length is a novel metric introduced by Vaassen et al. (https://doi.org/10.1016/j.phro.2019.12.001) and is conceptually the distance which an editor's cursor needs to travel when making additive (but not subtractive) corrections to an automated segmentation. It is numerically the number of pixels in corrected segmentation edge that are not shared in the automated segmentation.

