##############################     IMPORT OF REQUIRED MODULES    ###################################
from datetime import datetime
from SenLAST.comparison import *
from SenLAST.data_preprocessing import eliminate_MODIS_cloudy_data, eliminate_SENTINEL_cloudy_data
from SenLAST.comparison import select_MODIS_scenes, select_SENTINEL_scenes
from SenLAST.analysis import *


start_time = datetime.now()

def main():
    ###################################     INPUT    ########################################

    #### ----- TIFF Data ----- ####
    ### Jonas base Folder:
    ## MODIS:
    MODIS_directory = "F:/Test_MODIS/LST/GeoTIFF/Thuringia/scaled"
    # MODIS_directory = "F:/411/LST/GeoTIFF/Thuringia/scaled/cloud_free" # analysis.py, hier wieder final_selected path adden
    ## Sentinel:
    # Sentinel_directory = "F:/Sentinel_3/S3_Daten-20200622T143538Z-001/S3_Daten"
    Sentinel_directory = "F:/Test_SENTINEL"
    # Sentinel_directory = "F:/Test_SENTINEL/selected/cloud_free" # analysis.py, hier wieder final_selected path adden

    ### Shapefiles:
    ## MODIS Shapefile:
    MODIS_shapefile = "C:/Users/jz199/Documents/Studium/Master/2. Semester/Vorlesungsmitschriften/GEO411 - Landschaftsmanagement und Fernerkundung/Auszug_Daten_SandraBauer_MA/Auszug_Daten_SandraBauer_MA/Stationen_Thüringen_Umland_3x3box_reprojected.shp"
    ## Sentinel Shapefile:
    Sentinel_shapefile = "C:/Users/jz199/Documents/Studium/Master/2. Semester/Vorlesungsmitschriften/GEO411 - Landschaftsmanagement und Fernerkundung/Auszug_Daten_SandraBauer_MA/Auszug_Daten_SandraBauer_MA/Stationen_Thüringen_Umland_3x3box.shp"


    ### Marlin base Folder:
    ## MODIS:
    # MODIS_directory = "F:/GEO411_data/MODIS_Daten/MODIS_download"
    # MODIS_directory = "F:/GEO411_data/MODIS_Daten/MODIS_download/cloud_free/final_modis_selected" #analysis.py
    ## Sentinel:
    # Sentinel_directory = "F:/GEO411_data/Sentinel_Daten"
    # Sentinel_directory = "F:/GEO411_data/Sentinel_Daten/selected/cloud_free/final_sentinel_selected" #analysis.py

    ### Shapefiles:
    ## MODIS Shapefile:
    # MODIS_shapefile = "F:/GEO411_data/Daten_Sandra/new/Stationen_Thüringen_Umland_3x3box_reprojected.shp"
    ## Sentinel Shapefile:
    # Sentinel_shapefile = "F:/GEO411_data/Daten_Sandra/new/Stationen_Thüringen_Umland_3x3box.shp"


    ####################### USER-DEPENDENT FUNCTIONS TO BE USED #######################

    ### Extract correct Sentinel and MODIS data from all downloaded data ###
    # extract_SENTINEL_timestamp(sen_directory=Sentinel_directory)
    # extract_MODIS_timestamp(mod_directory=MODIS_directory)
    # eliminate_SENTINEL_cloudy_data(sen_directory=Sentinel_directory, shape_path=Sentinel_shapefile)
    # eliminate_MODIS_cloudy_data(mod_directory=MODIS_directory, shape_path=MODIS_shapefile)


    ### Sentinel selection needs to be run first, or MODIS folder will be deleted!!! ###
    ### OLD AND WORKING WITHOUT TIME ###
    select_SENTINEL_scenes(mod_directory=MODIS_directory, sen_directory=Sentinel_directory)
    select_MODIS_scenes(mod_directory=MODIS_directory, sen_directory=Sentinel_directory)

    ### NEW AND NOT WORKING ###
    # select_SENTINEL_scenes(mod_directory=MODIS_directory, sen_directory=Sentinel_directory, start=90, end=90)
    # select_MODIS_scenes(mod_directory=MODIS_directory, sen_directory=Sentinel_directory, start=0, end=0)

    ##### RASTER-ANALYSIS SECTION #####
    # analyze_SENTINEL_temperature(sen_directory=Sentinel_directory, shape_path=Sentinel_shapefile)
    # analyze_MODIS_temperature(mod_directory=MODIS_directory, shape_path=MODIS_shapefile)


    statistics_time = datetime.now()
    print("extract_files-time = ", statistics_time - start_time, "Hr:min:sec")


if __name__ == '__main__':
    main()
    start_time = datetime.now()
