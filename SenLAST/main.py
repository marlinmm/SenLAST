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

    ### Base Folder:
    # Base_Folder = "F:/GEO411_data/Processing/"
    # Marlin Laptop
    Base_Folder = "C:/Users/marli/Desktop/Processing/"

    ## MODIS ##
    MODIS_cloud_free_directory = Base_Folder + "MODIS/cloud_free"
    MODIS_time_overlap_directory = Base_Folder + "MODIS/time_overlap"

    ## SENTINEL ##
    SENTINEL_cloud_free_directory = Base_Folder + "Sentinel/cloud_free"
    SENTINEL_time_overlap_directory = Base_Folder + "Sentinel/time_overlap"

    ## Datapairs ##
    # Datapair_directory = Base_Folder + "Sen_MOD_Datenpaare"
    # Sentinel_Datapair_directory = Base_Folder + "Sen_MOD_Datenpaare/Sentinel"
    # MODIS_Datapair_directory = Base_Folder + "Sen_MOD_Datenpaare/MODIS"

    ### For allstations_alldata function use the following directories
    # Sentinel_Datapair_directory = "F:/GEO411_data/Processing/Sen_MOD_Datenpaare/Sentinel/2018_09_30"
    # MODIS_Datapair_directory = "F:/GEO411_data/Processing/Sen_MOD_Datenpaare/MODIS/2018_09_30"

    ## DWD ##
    SENTINEL_DWD_directory = Base_Folder + "DWD/Sentinel"
    MODIS_DWD_directory = Base_Folder + "DWD/MODIS/"

    ## SHAPEFILES ##
    SENTINEL_Shapefile_directory = Base_Folder + "Shapefiles/Stationen_Thüringen_Umland_3x3box.shp"
    MODIS_Shapefile_directory = Base_Folder + "Shapefiles/Stationen_Thüringen_Umland_3x3box_reprojected.shp"

    ####################### USER-DEPENDENT FUNCTIONS TO BE USED #######################

    ##### RASTER-ANALYSIS SECTION #####
    # analyze_SENTINEL_temperature(sen_directory=Sentinel_Datapair_directory, sen_shape_path=SENTINEL_Shapefile_directory, daytime_S3="DAY")
    # analyze_MODIS_temperature(mod_directory=MODIS_cloud_free_directory, mod_shape_path=MODIS_Shapefile_directory, daytime_MODIS="Day")
    # SenMod_DayNight(mod_directory=MODIS_Datapair_directory, sen_directory=Sentinel_Datapair_directory, daytime_S3="DAY",
    #           sen_shape_path=SENTINEL_Shapefile_directory, mod_shape_path=MODIS_Shapefile_directory, daytime_MODIS="Day")
    # mean_diff(mod_directory=MODIS_Datapair_directory, sen_directory=Sentinel_Datapair_directory, daytime_S3="DAY",
    #          sen_shape_path=SENTINEL_Shapefile_directory, mod_shape_path=MODIS_Shapefile_directory, daytime_MODIS="Day")
    # SenMod_scatter(mod_directory=MODIS_Datapair_directory, sen_directory=Sentinel_Datapair_directory, daytime_S3="DAY",
    #                 sen_shape_path=SENTINEL_Shapefile_directory, mod_shape_path=MODIS_Shapefile_directory,
    #                 daytime_MODIS="Day")
    analyze_MODIS_DWD(path_to_csv=MODIS_DWD_directory, mod_directory=MODIS_cloud_free_directory, mod_shape_path=MODIS_Shapefile_directory)

    statistics_time = datetime.now()
    print("extract_files-time = ", statistics_time - start_time, "Hr:min:sec")


if __name__ == '__main__':
    main()
    start_time = datetime.now()
