##############################     IMPORT OF REQUIRED MODULES    ###################################
from datetime import datetime
from SenLAST.comparison import *
from SenLAST.data_preprocessing import *
from SenLAST.comparison import *
from SenLAST.analysis import *
from SenLAST.import_dwd_data import *
from SenLAST.base_information import *
from SenLAST.plots import *



start_time = datetime.now()

def main():
    ###################################     INPUT    ########################################

    #### ----- TIFF Data ----- ####
    ### Jonas base Folder:
    ## MODIS:
    # MODIS_directory = "F:/Test_MODIS/LST/GeoTIFF/Thuringia/scaled"
    # MODIS_directory = "F:/FINAL_LST_Daten/Datenpaare/2018_07_03/MODIS"
    # MODIS_directory = "F:/411/LST/GeoTIFF/Thuringia/scaled/cloud_free" # analysis.py, hier wieder final_selected path adden
    # MODIS_Datapair_directory = "F:/411/FINAL_LST_Daten/MODIS_Daten_final_final/MODIS_download/cloud_free"
    # MODIS_time_directory = "F:/411/FINAL_LST_Daten/MODIS_Daten_final_final/time_layer/cloud_free"
    MODIS_Datapair_directory = "F:/411/FINAL_LST_Daten/Datenpaare/2018_09_30/MODIS"
    ## Sentinel:
    # Sentinel_directory = "F:/Sentinel_3/S3_Daten-20200622T143538Z-001/S3_Daten"
    Sentinel_Datapair_directory = "F:/411/FINAL_LST_Daten/Datenpaare/2018_09_30/Sentinel"
    # Sentinel_directory = "F:/Test_SENTINEL/selected/cloud_free" # analysis.py, hier wieder final_selected path adden
    # Sentinel_directory = "F:/FINAL_LST_Daten/Datenpaare/2018_07_03/SENTINEL"

    ### Shapefiles:
    ## MODIS Shapefile:
    MODIS_Shapefile_directory = "C:/Users/jz199/Documents/Studium/Master/2. Semester/Vorlesungsmitschriften/GEO411 - Landschaftsmanagement und Fernerkundung/Auszug_Daten_SandraBauer_MA/Auszug_Daten_SandraBauer_MA/Stationen_Thüringen_Umland_3x3box_reprojected.shp"
    ## Sentinel Shapefile:
    SENTINEL_Shapefile_directory = "C:/Users/jz199/Documents/Studium/Master/2. Semester/Vorlesungsmitschriften/GEO411 - Landschaftsmanagement und Fernerkundung/Auszug_Daten_SandraBauer_MA/Auszug_Daten_SandraBauer_MA/Stationen_Thüringen_Umland_3x3box.shp"


    ### Marlin base Folder:
    ## MODIS:
    # MODIS_directory = "F:/GEO411_data/MODIS_Daten/MODIS_download"
    # MODIS_directory = "F:/GEO411_data/MODIS_Daten/MODIS_download/cloud_free"
    # MODIS_time_directory = "F:/GEO411_data/MODIS_Daten/time_layer/cloud_free"
    # MODIS_directory = "F:/GEO411_data/MODIS_Daten/MODIS_download/cloud_free/final_modis_selected" #analysis.py
    ## Sentinel:
    # Sentinel_directory = "F:/GEO411_data/Sentinel_Daten"
    # Sentinel_directory = "F:/GEO411_data/Sentinel_Daten/selected/cloud_free"
    # Sentinel_directory = "F:/GEO411_data/Sentinel_Daten/selected/cloud_free/final_sentinel_selected" #analysis.py

    ### Shapefiles:
    ## MODIS Shapefile:
    # MODIS_shapefile = "F:/GEO411_data/Daten_Sandra/new/Stationen_Thüringen_Umland_3x3box_reprojected.shp"
    ## Sentinel Shapefile:
    # Sentinel_shapefile = "F:/GEO411_data/Daten_Sandra/new/Stationen_Thüringen_Umland_3x3box.shp"

    ### CSV-Data:
    # csv_directory = "F:/GEO411_data/DWD_result_all/"


    ####################### USER-DEPENDENT FUNCTIONS TO BE USED #######################

    ### Extract correct Sentinel and MODIS data from all downloaded data ###
    # extract_SENTINEL_timestamp(sen_directory=Sentinel_directory)
    # extract_MODIS_timestamp(mod_directory=MODIS_directory)
    # eliminate_SENTINEL_cloudy_data(sen_directory=Sentinel_directory, shape_path=Sentinel_shapefile)
    # eliminate_MODIS_cloudy_data(mod_directory=MODIS_directory, shape_path=MODIS_shapefile)


    ### Sentinel selection needs to be run first, or MODIS folder will be deleted!!! ###
    ### OLD AND WORKING WITHOUT TIME ###
    # select_SENTINEL_scenes(mod_directory=MODIS_directory, sen_directory=Sentinel_directory)
    # select_MODIS_scenes(mod_directory=MODIS_directory, sen_directory=Sentinel_directory)


    ### NEW AND NOT WORKING ###
    # select_SENTINEL_scenes(mod_directory=MODIS_directory, sen_directory=Sentinel_directory, interval=90)
    # select_MODIS_scenes(mod_directory=MODIS_directory, sen_directory=Sentinel_directory, interval=0)

    ##### RASTER-ANALYSIS SECTION #####
    # analyze_SENTINEL_temperature(sen_directory=Sentinel_directory, shape_path=Sentinel_shapefile)
    # analyze_MODIS_temperature(mod_directory=MODIS_directory, shape_path=MODIS_shapefile)

    # rename_files(mod_directory=MODIS_directory, mod_time_directory=MODIS_time_directory, shape_path=MODIS_shapefile)

    mean_diff(mod_directory=MODIS_Datapair_directory, sen_directory=Sentinel_Datapair_directory, daytime_S3="NIGHT",
             sen_shape_path=SENTINEL_Shapefile_directory, mod_shape_path=MODIS_Shapefile_directory, daytime_MODIS="Night")

    ##### EXTRACT DWD DATA #####
    # import_DWD_data_Sentinel(sen_directory=Sentinel_directory, csv_directory=csv_directory)
    #import_DWD_data_MODIS(mod_directory=MODIS_directory, csv_directory=csv_directory)

    statistics_time = datetime.now()
    print("extract_files-time = ", statistics_time - start_time, "Hr:min:sec")


if __name__ == '__main__':
    main()
    start_time = datetime.now()
