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
    Base_Folder = "F:/GEO411_data/Processing/"

    ## MODIS ##
    MODIS_cloud_free_directory = Base_Folder + "MODIS/cloud_free"
    MODIS_time_overlap_directory = Base_Folder + "MODIS/time_overlap"

    ## SENTINEL ##
    SENTINEL_cloud_free_directory = Base_Folder + "Sentinel/S3B_renamed"
    SENTINEL_time_overlap_directory = Base_Folder + "Sentinel/time_overlap"

    ## Datapairs ##
    # Datapair_directory = Base_Folder + "Sen_MOD_Datenpaare"
    Sentinel_Datapair_directory = Base_Folder + "Sen_MOD_Datenpaare/S3B/Sentinel"
    MODIS_Datapair_directory = Base_Folder + "Sen_MOD_Datenpaare/S3B/MODIS"

    ### For allstations_alldata function use the following directories
    # Sentinel_Datapair_directory = "F:/GEO411_data/Processing/Sen_MOD_Datenpaare/Sentinel/2018_09_30"
    # MODIS_Datapair_directory = "F:/GEO411_data/Processing/Sen_MOD_Datenpaare/MODIS/2018_09_30"

    ## DWD ##
    SENTINEL_DWD_directory = Base_Folder + "DWD/Sentinel/S3B"
    # SENTINEL_DWD_directory = Base_Folder + "Juni_2020/Sentinel/DWD/"
    MODIS_DWD_directory = Base_Folder + "DWD/MODIS/"

    ## SHAPEFILES ##
    SENTINEL_Shapefile_directory = Base_Folder + "Shapefiles/Stationen_Thüringen_Umland_3x3box.shp"
    MODIS_Shapefile_directory = Base_Folder + "Shapefiles/Stationen_Thüringen_Umland_3x3box_reprojected.shp"

    ####################### USER-DEPENDENT FUNCTIONS TO BE USED #######################

    # station_land_covers(place="station")
    # station_height()

    # rename_sentinel(sen_directory=SENTINEL_time_overlap_directory)
    # import_DWD_data_Sentinel(sen_directory=SENTINEL_cloud_free_directory, csv_directory=SENTINEL_DWD_directory)

    # analyze_SENTINEL_temperature(sen_directory=Sentinel_Datapair_directory, sen_shape_path=SENTINEL_Shapefile_directory)
    # analyze_MODIS_temperature(mod_directory=MODIS_Datapair_directory, mod_shape_path=MODIS_Shapefile_directory)

    # SenMod_DayNight(mod_directory=MODIS_Datapair_directory, sen_directory=Sentinel_Datapair_directory, daytime_S3="DAY",
    #          sen_shape_path=SENTINEL_Shapefile_directory, mod_shape_path=MODIS_Shapefile_directory, daytime_MODIS="Day")

    # mean_diff(mod_directory=MODIS_Datapair_directory, sen_directory=Sentinel_Datapair_directory, daytime_S3="DAY",
    #          sen_shape_path=SENTINEL_Shapefile_directory, mod_shape_path=MODIS_Shapefile_directory, daytime_MODIS="Day")
    # barchart_mean_diff(mod_directory=MODIS_Datapair_directory, sen_directory=Sentinel_Datapair_directory,
    #                    daytime_S3="DAY",
    #                    sen_shape_path=SENTINEL_Shapefile_directory, mod_shape_path=MODIS_Shapefile_directory,
    #                    daytime_MODIS="Day")

    # SenMod_scatter(mod_directory=MODIS_Datapair_directory, sen_directory=Sentinel_Datapair_directory, daytime_S3="DAY",
    #                 sen_shape_path=SENTINEL_Shapefile_directory, mod_shape_path=MODIS_Shapefile_directory,
    #                 daytime_MODIS="Day")
    # SenMod_histogram(mod_directory=MODIS_Datapair_directory, sen_directory=Sentinel_Datapair_directory, daytime_S3="DAY",
    #                 sen_shape_path=SENTINEL_Shapefile_directory, mod_shape_path=MODIS_Shapefile_directory,
    #                 daytime_MODIS="Day")

    # analyze_MODIS_DWD(path_to_csv=MODIS_DWD_directory, mod_directory=MODIS_cloud_free_directory,
    #                   mod_shape_path=MODIS_Shapefile_directory, DWD_temp_parameter="TT_10")
    # analyze_Sentinel_DWD(path_to_csv=SENTINEL_DWD_directory, sen_directory=SENTINEL_cloud_free_directory,
    #                      sen_shape_path=SENTINEL_Shapefile_directory, DWD_temp_parameter="TT_10")
    # SenDWD_barchart(sen_directory=SENTINEL_cloud_free_directory, sen_shape_path=SENTINEL_Shapefile_directory,
    #                 path_to_csv=SENTINEL_DWD_directory)
    # ModDWD_barchart(path_to_csv=MODIS_DWD_directory, mod_directory=MODIS_cloud_free_directory,
    #                 mod_shape_path=MODIS_Shapefile_directory)

    ####################### DELIVERS SHIT RESULTS ###############################
    plot_Sentinel_DWD(sen_directory=SENTINEL_cloud_free_directory, sen_shape_path=SENTINEL_Shapefile_directory,
                      path_to_csv=SENTINEL_DWD_directory, DWD_temp_parameter="TT_10")
    #############################################################################

    # plot_MODIS_DWD(path_to_csv=MODIS_DWD_directory, mod_directory=MODIS_cloud_free_directory,
    #                mod_shape_path=MODIS_Shapefile_directory, DWD_temp_parameter="TM5_10")

    # allstations_alldata(mod_directory=MODIS_Datapair_directory, sen_directory=Sentinel_Datapair_directory,
    #                     daytime_S3="",
    #                     sen_shape_path=SENTINEL_Shapefile_directory, mod_shape_path=MODIS_Shapefile_directory,
    #                     daytime_MODIS="")

    # count_all_occurences(satellite="Modis", satellite_directory=MODIS_cloud_free_directory)

    statistics_time = datetime.now()
    print("extract_files-time = ", statistics_time - start_time, "Hr:min:sec")


if __name__ == '__main__':
    main()
    start_time = datetime.now()
