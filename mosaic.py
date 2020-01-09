"""
# =============================================================================
This script aims to do imagery mosaic automatically. It reads and exports in 
geotiff format. Note: error may happen if the image size exceeds the memory
limit.

reference:
https://rasterio.readthedocs.io/en/latest/quickstart.html
https://automating-gis-processes.github.io/CSC18/lessons/L6/raster-mosaic.html

Shunan Feng fsn.1995@gmail.com
# =============================================================================
"""
# if you want to clear all variables, run the following line
#%reset -f

import rasterio
from rasterio.merge import merge
from rasterio.plot import show

import glob
import os

# define the folder that contains the images
folderpath = r"C:\Users\A409118\Desktop\IQ_Rufaiat_19Feb19"
# define the full path for your output mosaic image
fileout = r"C:\Users\A409118\Desktop\IQ_Rufaiat_19Feb19\IQmosaic.tif"

# read images in the folder
searchCriteria = "I*.tif"
globInput = os.path.join(folderpath, searchCriteria)
tifList = glob.glob(globInput)

tifList2mosaic = []
for filepath in tifList:
    src = rasterio.open(filepath)
    tifList2mosaic.append(src)
immosaic, outTransform = merge(tifList2mosaic)
show(immosaic)

out_meta = src.meta.copy()
out_meta.update({"driver": "GTiff",
                         "height": immosaic.shape[1],
                          "width": immosaic.shape[2],
                          "transform": outTransform
                          }
                         )
with rasterio.open(fileout, "w", **out_meta) as dst:
             dst.write(immosaic)
