from datetime import datetime
import os
import rasterio as rio
import rasterio.mask
import numpy as np
import fiona
import shutil

# Kurze Info zu "i in range()":
## https://medium.com/better-programming/stop-using-range-in-your-python-for-loops-53c04593f936

start_time = datetime.now()

### ----- TIFF Data ----- ###
## Jonas Folder:
directory = "F:/411/LST/GeoTIFF/Thuringia/scaled"
## Marlin Folder:
# directory = "F:/GEO411_data/MODIS_Daten/MODIS_download"

### ----- Shapefile Data ----- ###
## Shapefile Marlin:
# shapefolder = "F:/GEO411_data/Daten_Sandra/new/"
# shapefile = "Stationen_Thüringen_Umland_3x3box_reprojected.shp"
## Shapefile Jonas:
shapefolder = "C:/Users/jz199/Documents/Studium/Master/2. Semester/Vorlesungsmitschriften/GEO411 - Landschaftsmanagement und Fernerkundung/Auszug_Daten_SandraBauer_MA/Auszug_Daten_SandraBauer_MA/"
shapefile = "Stationen_Thüringen_Umland_3x3box_reprojected.shp"

shape_path = shapefolder + shapefile