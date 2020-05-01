# Autosegmentation Accuracy Metrics
__________________________________

### Python code to calculate the added path length, added path volume, and corrections path length between an automated segmentation and its corresponding expert-corrected segmentation. 

The added path length (APL) is a novel metric introduced by Vaassen et al. (https://doi.org/10.1016/j.phro.2019.12.001) and is conceptually the distance that an editor's cursor travels when making additive (but not subtractive) corrections to an automated segmentation. Numerically it is the number of pixels in the corrected segmentation surface that are not shared in the automated segmentation.

![](images/APL.png)

Vaassen et al. demonstrated that the APL correlates better with the time required to correct a segmentation than do traditional, popular metrics such as the volumetric Dice similarity coefficient or the Hausdorff distance. As a measure of autosegmentation accuracy, the APL  captures the expected time-savings benefit of automated segmentation better than traditional metrics.

Inspired by the APL, we also present code two related metrics which we call the corrections path length (CPL) and the added path volume (APV). The corrections path length is like the APL but includes the surface area (in pixels) of subtractive corrections as well as additive ones.

![](images/CPL.png)

The APV is the corrected segmentation volume that is not included in the automated segmentation volume. Effectively this is the false negative volume.

![](images/APV.png)

