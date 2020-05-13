# Fun with Python for Geodata
Personal practices in geodata analysis with python.
## 1. Data Visulization

### 1.1 [covid-19 and Benford's law](https://github.com/fsn1995/Fun-with-Python-for-Geodata/blob/master/covid19Benford.ipynb)
Benford's law is an interesting theory so I did some experiment with covid-19 data. It's out of my specialization so there's no gurantee in the accuracy and quality of this analysis. Be doubtful and just for fun.
Here the screenshot is confirmed cases from three countries that I had lived. 
<img src="pic/covidBenford.png" width="80%" height="80%">

### 1.2 [**data visualization exercise**](https://nbviewer.jupyter.org/github/fsn1995/Fun-with-Python-for-Geodata/blob/master/dataVisualization/DataVisual.ipynb)
Scripts or jupyter notebooks for processing, visualizing and analyzing data.Some are exported as interactive html files in [**dataVisualization**](https://github.com/fsn1995/Fun-with-Python-for-Geodata/tree/master/dataVisualization/dataVisualHTML) folder or for preview in the links given.  

The [raw ipynb file](https://github.com/fsn1995/Fun-with-Python-for-Geodata/blob/master/dataVisualization/DataVisual.ipynb) contains contents of custom JavaScript plots will be rendered as static html (see [GitHub help](https://help.github.com/en/github/managing-files-in-a-repository/working-with-jupyter-notebook-files-on-github)), same for exported html files.  

Interactive figures or maps for:
#### 1.2.1 Global Annual Temperature Anomaly Interactive scatter plots with lowess trendlines
<img src="pic/temp.png" width="70%" height="70%">

#### 1.2.2 COVID-19 related spatial visualization
- [**Total test per thousand people**](https://nbviewer.jupyter.org/github/fsn1995/Fun-with-Python-for-Geodata/blob/master/dataVisualization/dataVisualHTML/TotalTestsCovid19.html)

<img src="pic/testcovid19.png" width="70%" >

- [**Comparison of COVID-19 Case Growth and Government Response Stringency Index**](https://nbviewer.jupyter.org/github/fsn1995/Fun-with-Python-for-Geodata/blob/master/dataVisualization/dataVisualHTML/covidpolicy.html)

<img src="pic/covidpolicy.png" width="50%" >

- **Ridgeline Plot of COVID-19 Daily Cases**  
[New Cases](https://nbviewer.jupyter.org/github/fsn1995/Fun-with-Python-for-Geodata/blob/master/dataVisualization/dataVisualHTML/covidNewCaseRidge.html) | [New Deaths](https://nbviewer.jupyter.org/github/fsn1995/Fun-with-Python-for-Geodata/blob/master/dataVisualization/dataVisualHTML/covidNewDeathRidge.html)

<img src="pic/covidridge.png" width="85%" >

#### 1.2.3 Time series plots
- **Time series bubble plots**

<img src="pic/cause of death.png" width="50%" height="50%">

- **time series heatmap of drought condition**

<img src="pic/droughtHeat.png" width="70%" height="70%">

- **Mass Balance of Storglaciären**

![python4](pic/storglaciaren2.png)
#### 1.2.4 Mapping the World
- [**Global Airports Connection Interactive Map**](https://nbviewer.jupyter.org/github/fsn1995/Fun-with-Python-for-Geodata/blob/master/dataVisualization/dataVisualHTML/airportConnection.html), inspired by altair template and OpenFlights.org. 

<img src="pic/airportconnection.png" width="80%" height="80%">

- [**Global Power Plant**](https://nbviewer.jupyter.org/github/fsn1995/Fun-with-Python-for-Geodata/blob/master/dataVisualization/dataVisualHTML/globalpowerplant.html), mixed subplots treemaps with plotly. 

<img src="pic/generatorglobal.png" width="75%" height="75%">
<img src="pic/generatortreemap.png" width="80%" height="80%">

### 1.3 [Raster Data Visualization](https://nbviewer.jupyter.org/github/fsn1995/Fun-with-Python-for-Geodata/blob/master/dataVisualization/georasterVisual.ipynb)
#### 1.3.1 [Interactive DEM viewer](https://nbviewer.jupyter.org/github/fsn1995/Fun-with-Python-for-Geodata/blob/master/dataVisualization/dataVisualHTML/dem3d.html)

<img src="pic/dem.png" width="100%" height="100%">

## 2. Automation
### 2.1 [EarthdataDownload.py](https://github.com/fsn1995/Fun-with-Python-for-Geodata/blob/master/automation/EarthdataDownload.py)
This is used to bulk download data from earthdata.nasa.gov. Input required is the link list.
### 2.2 [mosaic.py](https://github.com/fsn1995/Fun-with-Python-for-Geodata/blob/master/automation/mosaic.py)
This is practice to do mosaic and subset by roi for geotiff data. The process is done with rasterio library.

## 3. [geopyfsn](https://github.com/fsn1995/Fun-with-Python-for-Geodata/blob/master/dataVisualization/geopyfsn.py)
This is a collection of some functions used for myself.
- getxy: This can be used to obtain the x, y coordinates of a tiff file.

```python
import rasterio 
from geopyfsn import getxy

src = rasterio.open('image.tif')
x, y = getxy(src)
```
### 