from datetime import datetime
import os
import rasterio as rio
import rasterio.mask
import numpy as np
import fiona
import shutil

start_time = datetime.now()

## Jonas Folder:
# directory = "F:/Sentinel_3/S3_Daten-20200622T143538Z-001/S3_Daten"

## Marlin Folder:
directory = "F:/GEO411_data/Sentinel_Daten"

def extract_files_to_list(path_to_folder):
    """
    finds all .tif-files in the corresponding directory
    :return:
    """
    new_list = []

    for filename in os.listdir(path_to_folder):
        if filename.endswith(".tif"):
            new_list.append(os.path.join(path_to_folder, filename))
        else:
            continue
    return new_list

### this function needs to be generalized ###
def import_polygons():
    """
    imports the 3x3km polygons of the DWD weather stations
    :return:
    """
    shape_list = []

    for h in range(0,19):
        ## Shapefile Marlin:
        shapefolder = "F:/GEO411_data/Daten_Sandra/new/"
        ## Shapefile Jonas:
        # shapefolder = "C:/Users/jz199/Documents/Studium/Master/2. Semester/Vorlesungsmitschriften/GEO411 - Landschaftsmanagement und Fernerkundung/Auszug_Daten_SandraBauer_MA/Auszug_Daten_SandraBauer_MA/"

        inputshape = "Stationen_Thüringen_Umland_3x3box.shp"
        shapefile = fiona.open(shapefolder+inputshape, "r")

        shapes = [feature["geometry"] for feature in shapefile]
        shape_list.append(shapes)
    return shape_list


def eliminate_nanoverlap():
    """
    eliminates the scenes which would'nt match with all weather stations
    :return:
    """
    import_list = import_polygons()
    file_list = extract_files_to_list(path_to_folder=directory)
    tifs_selected = directory + "/selected"
    if os.path.exists(tifs_selected):
        shutil.rmtree(tifs_selected)
    os.mkdir(directory + "/selected")

    for i in range(0, len(file_list)):
        # Select between MODIS and SENTINEL
        src1 = rio.open(file_list[i])
        # src1 = rio.open(Modis_folder + Modis_file)
        try:
            for j in range(0, len(import_list)+1):
                out_image1, out_transform1 = rio.mask.mask(src1, [import_list[0][j]], all_touched=0, crop=True,
                                                           nodata=np.nan)
            shutil.copy(file_list[i], tifs_selected)
        except ValueError:
            pass

eliminate_nanoverlap()


def eliminate_cloudy_data():
    """
    eliminates the scenes which are not cloud_free
    :return:
    """
    # create new cloud_free directory, overwrite if already exits
    cloud_free = directory + "/selected/cloud_free"
    if os.path.exists(cloud_free):
        shutil.rmtree(cloud_free)
    os.mkdir(directory + "/selected/cloud_free")
    selected_tifs = extract_files_to_list(path_to_folder=directory + "/selected")

    # import polygons from shapefile
    import_list = import_polygons()

    # loop through all .tif files in folder
    for tif in range(0, len(selected_tifs)):
        src1 = rio.open(selected_tifs[tif])
        bool_list = []
        flag = 0   #set boolean flag to 0

        # loop through all weatherstations for each .tif file
        for polygons in range(0, len(import_list)+1):
            out_image1, out_transform1 = rio.mask.mask(src1, [import_list[0][polygons]], all_touched=1, crop=True,
                                                       nodata=np.nan)

            # extract minimal temperature at all stations for each .tif file to eliminate error values
            min_temp = np.min(out_image1[0])

            # create boolean values for error values and store in list
            if min_temp < -40:
                bool_list.append(False)
            else:
                bool_list.append(True)

        # check the list for flags of error values and only save tif files without any error values at station locations
        for boolean in bool_list:
            if boolean == False:
                flag = 1
                break
        if flag == 0:
            shutil.copy(selected_tifs[tif], cloud_free)

eliminate_cloudy_data()

statistics_time = datetime.now()
print("extract_files-time = ", statistics_time - start_time, "Hr:min:sec")

