# -*- coding: utf-8 -*-
"""
Created on Wed May 13 15:48:06 2020

@author: shunan feng
"""
import numpy as np

def getxy(rasterfile):
  """
  getxy is used for getting the x and y coordinates of the rasterfile.

  [rasterfile]: variable read by rasterio
  [x,y]: the x, y coordinates of the input

  e.g.
  import rasterio 
  src = rasterio.open('image.tif')
  x, y = getxy(src)
  """
  rasterbound = rasterfile.bounds
  x = np.linspace(rasterbound.left, rasterbound.right, rasterfile.width)
  y = np.linspace(rasterbound.bottom, rasterbound.top, rasterfile.height)
  return x, y