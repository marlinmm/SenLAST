##############################     IMPORT OF REQUIRED MODULES    ###################################

from datetime import datetime
import os
import rasterio as rio
import rasterio.mask
import numpy as np
import fiona
import shutil


start_time = datetime.now()

def main():
    ###################################     INPUT    ########################################

    ### ----- TIFF Data ----- ###
    ## Jonas Folder:
    # directory = "F:/411/LST/GeoTIFF/Thuringia/scaled"
    # global
    directory = ""
    ## Marlin Folder:
    directory = "F:/GEO411_data/MODIS_Daten/MODIS_download"

    ### ----- Shapefile Data ----- ###
    ## Shapefile Marlin:
    shapefolder = "F:/GEO411_data/Daten_Sandra/new/"
    shapefile = "Stationen_Thüringen_Umland_3x3box_reprojected.shp"
    ## Shapefile Jonas:
    # shapefolder = "C:/Users/jz199/Documents/Studium/Master/2. Semester/Vorlesungsmitschriften/GEO411 - Landschaftsmanagement und Fernerkundung/Auszug_Daten_SandraBauer_MA/Auszug_Daten_SandraBauer_MA/"
    # shapefile = "Stationen_Thüringen_Umland_3x3box_reprojected.shp"

    shape_path = shapefolder + shapefile

    ####################### USER-DEPENDENT FILTER-FUNCTIONS TO BE USED #######################

    extract_SENTINEL = ['example function']
    extract_MODIS = ['example function']
    comparison = ['example function']
    test_stations = ['example function']

    return directory, shape_path, extract_SENTINEL, extract_MODIS, comparison, test_stations

def extract_S3_data(directory, shape_path, extract_SENTINEL):

def extract_MODIS_data(directory, shape_path, extract_SENTINEL):

def compare_data():

if __name__ == '__main__':
    start_time = datetime.now()
    in_variables = main()

    # call this function to execute extract_S3_data:
    # extract_S3_data()

    # call this function to execute extract_MODIS_data:
    # extract_MODIS_data

    # call this function to execute compare_data():
    # compare_data()