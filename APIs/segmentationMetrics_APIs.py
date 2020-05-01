import numpy as np
from APIs import utility_APIs as util


"""
Each function takes "auto" and "gt" arguments, which are respectively the autosegmentation and ground truth 
segmentation represented as three-dimensional NumPy arrays. The array dimensions should be the dimensions 
of the original image, and each array element should be 0 if its corresponding image pixel is not part of 
the segmentation or 1 if it is.
"""

def addedPathVolume(auto, gt):
    '''
    Returns the added path volume, in pixels
    
    Steps:
    1. Find pixels where the mask is present in gt but not in auto (wherever gt is 1 but auto is 0)
    2. Convert comparison from bool to int
    3. Compute # pixels
    '''
    
    apv = (gt > auto).astype(int).sum()
    return apv


def correctionsPathLength(auto, gt):
    '''
    Returns the corrections path length, in pixels
    
    Steps:
    1. Find pixels at the edge of the mask for both auto and gt
    2. Count # pixels on the edge of gt that are not on the edge of auto
    '''
    
    # Check if auto and gt have same dimensions. If not, then raise a ValueError
    if auto.shape != gt.shape:
        raise ValueError('Shape of auto and gt must be identical!!!')

    # edge_auto has the pixels which are at the edge of the automated segmentation result
    edge_auto = util.getEdgeOfMask(auto)
    # edge_gt has the pixels which are at the edge of the ground truth segmentation
    edge_gt = util.getEdgeOfMask(gt)
    
    # Count # pixels on the edge of gt that are on not on the edge of auto
    cpl = (edge_gt > edge_auto).astype(int).sum()
    
    return cpl 


def addedPathLength(auto, gt):
    '''
    Returns the added path length, in pixels
    
    Steps:
    1. Find pixels at the edge of the mask for gt
    2. Count # pixels on the edge of gt that are not inside the mask in auto
    '''
    
    # Check if auto and gt have same dimensions. If not, then raise a ValueError
    if auto.shape != gt.shape:
        raise ValueError('Shape of auto and gt must be identical!!!')
    
    # edge_gt has the pixels which are at the edge of the ground truth segmentation
    edge_gt = util.getEdgeOfMask(gt)
    
    # Count # pixels where the edges in grount truth == 1 and auto == 0
    apl = (edge_gt > auto).astype(int).sum() 
    
    return apl