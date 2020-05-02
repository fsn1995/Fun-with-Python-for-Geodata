# -*- coding: utf-8 -*-
"""
This is the script that reads the landcover data exported from GEE. It reads
and analyzes the annual results. Time series plots and landcover transition 
will be done. All the figures/text files will be saved or exported for future 
use.

Created on Wed Mar 11 16:26:49 2020

@author: Shunan Feng sfeng@icrc.org
"""
#%%
import os
import numpy as np
import matplotlib.pyplot as plt

import rasterio
from rasterio.plot import show
#%% lucc transition
folder = r"tif/"
subdir = sorted(os.listdir(folder))
fileNum = len(subdir)

countsPixelc = np.ones((11, 1))
countsPixeld = np.ones((11, fileNum))

for i in range(fileNum - 1):
    with rasterio.open(folder + "\\" + subdir[i]) as src:
        A = src.read(1)
        titlestr = subdir[i][0:4]
        show(src, title=titlestr)
#        f1.savefig("output\landcover" + titlestr + ".png" , dpi = 300)
    with rasterio.open(folder + "\\" + subdir[i + 1]) as src:
        B = src.read(1)
#        titlestr = subdir[i + 1][0:4]
    abDiff = B - A
    index = np.nonzero(abDiff)
    print('landcover changed ', 100 * np.count_nonzero(abDiff) / np.count_nonzero(A), '%\n')
    C = np.zeros(np.shape(B))
    C[index] = A[index]
    figtitle = "landcover pre-change " + subdir[i][0:4]
    show(C, title = figtitle)
    uniqueC, counts = np.unique(C, return_counts=True)
    uniquePixel = np.delete(uniqueC, 0)
    countsPixelc = np.delete(counts, 0)
#    f2.savefig("output\change\\" + figtitle + ".png" , dpi = 300)
    D = np.zeros(np.shape(B))
    D[index] = B[index]
    figtitle = "landcover post-change " + subdir[i + 1][0:4]
    show(D, title = figtitle)
    uniqueD, counts = np.unique(D, return_counts=True)
    # uniquePixeld[:, i] = np.delete(uniqueD, 0)
    countsPixeld[:, i] = np.delete(counts, 0)
np.savetxt('output\\countsPixelc.txt', countsPixelc)
np.savetxt('output\\countsPixeld.txt', countsPixeld)
# np.savetxt('output\\uniquePixelc.txt', uniquePixelc)
# np.savetxt('output\\uniquePixeld.txt', uniquePixeld)
#%% lucc summary
# there are 11 different luccclasses in total
folder = r"tif/"
subdir = sorted(os.listdir(folder))
fileNum = len(subdir)

uniquePixel = np.ones((11, fileNum))
countsPixel = np.ones((11, fileNum))

luccClass = 'Rainfed croplands', 'Mosaic cropland vegetation', \
             'Mosaic vegetation cropland', 'broadleaved deciduous forest', \
             'needleleaved evergreen forest ', \
             'broadleaved and needleleaved forest', \
             'Mosaic forest-shrubland grassland',\
             'Mosaic grassland forest-shrubland',\
             'Closed to open shrubland', 'Sparse vegetation ',\
             'Water bodies'
luccColor = ['#aaefef','#dcef63','#cdcd64','#009f00','#003b00','#788300',\
             '#8d9f00','#bd9500','#956300','#ffebae','#0046c7']

for i in range(fileNum):
    with rasterio.open(folder + "\\" + subdir[i]) as src:
        A = src.read(1)
        titlestr = subdir[i][0:4]
    uniqueA, counts =  np.unique(A, return_counts=True)
    fig1, ax1 = plt.subplots()
    ax1.pie(counts, labels = luccClass, colors = luccColor)
    ax1.set_title(titlestr)
    fig1.savefig('output/pie/' + titlestr +'.png', dpi = 300)
    uniquePixel[:, i] = uniqueA
    countsPixel[:, i] = counts
    # ax1.pie(np.delete(counts, 0), labels = luccClass, colors = luccColor)
    # ax1.set_title(titlestr)
    # fig1.savefig(r'output/pie/' + titlestr, +'.png', dpi = 300)
    # uniquePixel[:, i] = np.delete(uniqueA, 0)
    # countsPixel[:, i] = np.delete(counts, 0)

time = np.arange(1984, 2020)  # 1984-2019
for i in range(11):
    fig2, ax2 = plt.subplots()
    ax2.scatter(time, countsPixel[i, :], label = luccClass[i])
    ax2.set(title = luccClass[i], ylabel = 'Pixels (30 m)')
    # fig2.ylabel('Pixels (30 m)')
    fig2.savefig('output/scatter/' + luccClass[i] +'.png', dpi = 300)
    
np.savetxt('output\\countsPixelTotal.txt', countsPixel)
np.savetxt('output\\uniquePixelTotal.txt', uniquePixel)
# for i in uniquePixel:
#     for m in range(fileNum):
#         with rasterio.open(folder + "\\" + subdir[m]) as src:
#             A = src.read(1)
#             index = A != i
#             A[tuple(index)] = 0