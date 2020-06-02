'''
@article{Zhou2018,
	author    = {Qian-Yi Zhou and Jaesik Park and Vladlen Koltun},
	title     = {{Open3D}: {A} Modern Library for {3D} Data Processing},
	journal   = {arXiv:1801.09847},
	year      = {2018},
}
'''
## IMPORT LIBRARIES
import numpy as np
import time
import open3d
import pandas as pd
import matplotlib.pyplot as plt

## USE http://www.open3d.org/docs/release/tutorial/Basic/

## CHALLENGE 1 - OPEN A FILE OF YOUR CHOICE AND VISUALIZE THE POINT CLOUD
# The supported extension names are: pcd, ply, xyz, xyzrgb, xyzn, pts.
pcd = 

## IF YOU HAVE PPTK INSTALLED, VISUALIZE USING PPTK
#import pptk
#v = pptk.viewer(pcd.points)

## CHALLENGE 2 - VOXEL GRID DOWNSAMPLING
print(f"Points before downsampling: {len(pcd.points)} ")
pcd = 
print(f"Points after downsampling: {len(pcd.points)}")# DOWNSAMPLING


## CHALLENGE 3 - SEGMENTATION
_, inliers = 

## CHALLENGE 4 - CLUSTERING USING DBSCAN
labels = 
max_label= labels.max()
print(f"point cloud has {max_label + 1} clusters")

## BONUS CHALLENGE - CLUSTERING USING KDTREE AND KNN INSTEAD
pcd_tree = 

## CHALLENGE 5 - BOUNDING BOXES IN 3D
bounding_boxes = 

## CHALLENGE 6 - VISUALIZE THE FINAL RESULTS
list_of_visuals = 

## BONUS CHALLENGE 2 - MAKE IT WORK ON A VIDEO
