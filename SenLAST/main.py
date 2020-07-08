##############################     IMPORT OF REQUIRED MODULES    ###################################
from datetime import datetime
from SenLAST.comparison import *
from SenLAST.data_preprocessing import *
from SenLAST.comparison import *
from SenLAST.analysis import *
from SenLAST.import_dwd_data import *
from SenLAST.base_information import *


start_time = datetime.now()

def main():
    ###################################     INPUT    ########################################

    #### ----- TIFF Data ----- ####

    ### Base Folder:
    Base_Folder = "F:/GEO411_data/Processing/"

    ## MODIS ##
    MODIS_cloud_free_directory = Base_Folder + "MODIS/cloud_free"
    MODIS_time_overlap_directory = Base_Folder + "MODIS/time_overlap"

    ## SENTINEL ##
    SENTINEL_cloud_free_directory = Base_Folder + "Sentinel/cloud_free"
    SENTINEL_time_overlap_directory = Base_Folder + "Sentinel/time_overlap"

    ## DWD ##
    SENTINEL_DWD_directory = Base_Folder + "DWD/Sentinel"
    MODIS_DWD_directory = Base_Folder + "DWD/MODIS"

    ## SHAPEFILES ##
    SENTINEL_Shapefile_directory = Base_Folder + "Shapefiles/Stationen_Thüringen_Umland_3x3box.shp"
    MODIS_Shapefile_directory = Base_Folder + "Shapefiles/Stationen_Thüringen_Umland_3x3box_reprojected.shp"

    ####################### USER-DEPENDENT FUNCTIONS TO BE USED #######################



    statistics_time = datetime.now()
    print("extract_files-time = ", statistics_time - start_time, "Hr:min:sec")


if __name__ == '__main__':
    main()
    start_time = datetime.now()
