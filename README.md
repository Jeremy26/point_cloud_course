# Welcome to the Point Clouds Fast Course

In this course, you will learn to build a 3D Object detection system.
The course can be found here: https://www.thinkautonomous.ai/point-clouds


## DATASET
The dataset used is the KITTI dataset.
I use a subset of 20 point cloud files for this course.
[Link to the full dataset](http://www.cvlibs.net/download.php?file=data_object_velodyne.zip).


## Instructions
Usually, all courses are built in a Jupyter environment using Google Colab. It allows you to have no installation, you just open a browser.

However, visualizing 3D point clouds in Colab is still not mature enough to make the course a full Colab course.

This is why you'll need to run the course on your own machine.
NO PANIC - The list of requirements is extremely small.

To follow the course, you'll need the following libraries:
* Python 3.6
* Open3D 0.10.0
```
pip install open3d
```
To check Open3D Installation in a Python script:
```python
import open3d
open3d.__version__
```
* NumPy
* Matplotlib
* Pandas
* For Better Visualization (optional): PPTK
```
pip install pptk
```

The course will work on:
* Ubuntu 18.04+
* macOS 10.14+
* Windows 10 (64-bit)

### Earlier Versions
If you don't have these versions available or don't want to upgrade, no worries; it will still work but will require adjustments in terms of versions for Open3D.
At the bottom left of the Open3D page, select an earlier version (0.7.0 for example) and install it.
http://www.open3d.org/docs/0.7.0/getting_started.html#id2
[Link to the documentation](http://www.open3d.org/docs/0.7.0/getting_started.html#id2).

## DOCUMENTATION
The course uses the documentation provided by [Open 3D](http://www.open3d.org/docs/release/tutorial/Basic/pointcloud.html)

