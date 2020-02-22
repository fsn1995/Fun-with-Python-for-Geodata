"""
# =============================================================================
This script aims to do simple tasks of imagery mosaic and subset by roi
automatically. It reads and exports in geotiff format. The exported image
will be compressed by default to save the space.
Note: error may happen if the image size exceeds the memory limit.
Some also report that the exported image cannot be read by ArcGIS desktop.

reference:
https://rasterio.readthedocs.io/en/latest/quickstart.html
https://automating-gis-processes.github.io/CSC18/lessons/L6/raster-mosaic.html

The compression may take a while as it will try to optimze the storage.
For comparison of the compression methods:
https://kokoalberti.com/articles/geotiff-compression-optimization-guide/

Shunan Feng fsn.1995@gmail.com
# =============================================================================
"""
# if you want to clear all variables, run the following line
#%reset -f

import rasterio
from rasterio.merge import merge
from rasterio.plot import show
import rasterio.mask

import glob
import os
import fiona
# define the folder that contains the images
folderpath = r"P:\GIS\GIS\Nigeria\2020\Pix\wathab2020\NG_Gwoza_27Jan20"
# define the full path for your output mosaic image
mosaicout = r"P:\GIS\GIS\Nigeria\2020\Pix\wathab2020\NG_Gwoza_27Jan20.tif"

# =============================================================================
# if you would like to clip by roi, change the clipFlag to 1 and specifiy the 
# shapefile path
clipFlag = 0
clipout = r"P:\GIS\GIS\Nigeria\2020\Pix\wathab2020\NG_Ngala_09Jan20clip.tif"
shapepath = r"P:\GIS\GIS\Nigeria\2020\Pix\wathab2020\NG_Ngala_09Jan20\ngala.shp"
# =============================================================================


    
# read images in the folder
searchCriteria = "*.tif"
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
#                 "compress": "lzw"
                 })

with rasterio.open(mosaicout, "w", **out_meta, COMPRESS="lzma") as dst:
             dst.write(immosaic)

# read shapefile
if clipFlag == 1:         
    with fiona.open(shapepath, "r") as shapefile:
        shapes = [feature["geometry"] for feature in shapefile]
    with rasterio.open(mosaicout) as src:
        img, imgTransform = rasterio.mask.mask(src, shapes, crop=True)
        imgMeta = src.meta
    show(img)
    imgMeta.update({"driver": "GTiff",
                 "height": img.shape[1],
                 "width": img.shape[2],
                 "transform": imgTransform})

    with rasterio.open(clipout, "w", **imgMeta,  COMPRESS="lzma") as dst:
        dst.write(img)