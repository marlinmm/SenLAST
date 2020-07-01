##############################     IMPORT OF REQUIRED MODULES    ###################################
from datetime import datetime
from SenLAST.data_preprocessing import eliminate_MODIS_cloudy_data, eliminate_SENTINEL_cloudy_data


start_time = datetime.now()

def main():
    ###################################     INPUT    ########################################

    #### ----- TIFF Data ----- ####
    ### Jonas base Folder:
    ## MODIS:
    # MODIS_directory = "F:/411/LST/GeoTIFF/Thuringia/scaled"
    ## Sentinel:
    # Sentinel_directory = ""

    ### Shapefiles:
    ## MODIS Shapefile:
    # MODIS_shapefile = "C:/Users/jz199/Documents/Studium/Master/2. Semester/Vorlesungsmitschriften/GEO411 - Landschaftsmanagement und Fernerkundung/Auszug_Daten_SandraBauer_MA/Auszug_Daten_SandraBauer_MA/Stationen_Thüringen_Umland_3x3box_reprojected.shp"
    ## Sentinel Shapefile:
    # Sentinel_shapefile = "C:/Users/jz199/Documents/Studium/Master/2. Semester/Vorlesungsmitschriften/GEO411 - Landschaftsmanagement und Fernerkundung/Auszug_Daten_SandraBauer_MA/Auszug_Daten_SandraBauer_MA/Stationen_Thüringen_Umland_3x3box.shp"


    ### Marlin base Folder:
    ## MODIS:
    MODIS_directory = "F:/GEO411_data/MODIS_Daten/MODIS_download"
    ## Sentinel:
    Sentinel_directory = "F:/GEO411_data/Sentinel_Daten"

    ### Shapefiles:
    ## MODIS Shapefile:
    MODIS_shapefile = "F:/GEO411_data/Daten_Sandra/new/Stationen_Thüringen_Umland_3x3box_reprojected.shp"
    ## Sentinel Shapefile:
    Sentinel_shapefile = "F:/GEO411_data/Daten_Sandra/new/Stationen_Thüringen_Umland_3x3box.shp"

    ####################### USER-DEPENDENT FILTER-FUNCTIONS TO BE USED #######################

    eliminate_MODIS_cloudy_data(directory=MODIS_directory, shape_path=MODIS_shapefile)
    eliminate_SENTINEL_cloudy_data(directory=Sentinel_directory, shape_path=Sentinel_shapefile)

    statistics_time = datetime.now()
    print("extract_files-time = ", statistics_time - start_time, "Hr:min:sec")


if __name__ == '__main__':
    main()
    start_time = datetime.now()
