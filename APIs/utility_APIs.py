import numpy as np
import nilearn.image as ni_img

def loadNiftiReturnNumpy(filepath):
    '''
    filepath: path to nifti file
    '''
    niftiFile = ni_img.load_img(filepath)
    niftiArr = niftiFile.get_fdata()
    
    return niftiArr

def getEdgeOfMask(mask):
    '''
    Computes and returns edge of a segmentation mask
    '''
    # edge has the pixels which are at the edge of the mask
    edge = np.zeros_like(mask)
    
    # mask_pixels has the pixels which are inside the mask of the automated segmentation result
    mask_pixels = np.where(mask > 0)

    for idx in range(0,mask_pixels[0].size):

        x = mask_pixels[0][idx]
        y = mask_pixels[1][idx]
        z = mask_pixels[2][idx]

        # Count # pixels in 3x3 neighborhood that are in the mask
        # If sum < 27, then (x, y, z) is on the edge of the mask
        if mask[x-1:x+2, y-1:y+2, z-1:z+2].sum() < 27:
            edge[x,y,z] = 1
            
    return edge
