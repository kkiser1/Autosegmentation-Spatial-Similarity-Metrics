import numpy as np
from APIs import utility_APIs as util


"""
Each function takes "auto" and "gt" arguments, which are respectively the autosegmentation and ground truth 
segmentation represented as three-dimensional NumPy arrays. The array dimensions should be the dimensions 
of the original image, and each array element should be 0 if its corresponding image pixel is not part of 
the segmentation or 1 if it is.
"""

def FalseNegativeVolume(auto, gt):
    '''
    Returns the false negative volume, in pixels
    
    Steps:
    1. Find pixels where the mask is present in gt but not in auto (wherever gt is 1 but auto is 0)
    2. Convert comparison from bool to int
    3. Compute # pixels
    '''
    
    fnv = (gt > auto).astype(int).sum()
    return fnv


def AddedPathLength(auto, gt):
    '''
    Returns the added path length, in pixels
    
    Steps:
    1. Find pixels at the edge of the mask for both auto and gt
    2. Count # pixels on the edge of gt that are not in the edge of auto
    '''
    
    # Check if auto and gt have same dimensions. If not, then raise a ValueError
    if auto.shape != gt.shape:
        raise ValueError('Shape of auto and gt must be identical!')

    # edge_auto has the pixels which are at the edge of the automated segmentation result
    edge_auto = util.getEdgeOfMask(auto)
    # edge_gt has the pixels which are at the edge of the ground truth segmentation
    edge_gt = util.getEdgeOfMask(gt)
    
    # Count # pixels on the edge of gt that are on not in the edge of auto
    apl = (edge_gt > edge_auto).astype(int).sum()
    
    return apl 


def FalseNegativePathLength(auto, gt):
    '''
    Returns the false negative path length, in pixels
    
    Steps:
    1. Find pixels at the edge of the mask for gt
    2. Count # pixels on the edge of gt that are not in the auto mask volume
    '''
    
    # Check if auto and gt have same dimensions. If not, then raise a ValueError
    if auto.shape != gt.shape:
        raise ValueError('Shape of auto and gt must be identical!')
    
    # edge_gt has the pixels which are at the edge of the ground truth segmentation
    edge_gt = util.getEdgeOfMask(gt)
    
    # Count # pixels where the edges in grount truth == 1 and auto == 0
    fnpl = (edge_gt > auto).astype(int).sum() 
    
    return fnpl
