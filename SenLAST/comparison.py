from datetime import datetime
import os
from datetime import date
import shutil
import pandas as pd


start_time = datetime.now()

### ----- TIFF Data ----- ###
## Jonas Folder:
directory1 = "F:/Sentinel_3/S3_Daten-20200622T143538Z-001/S3_Daten/selected/cloud_free"
# directory2 = "F:/411/LST/GeoTIFF/Thuringia/scaled/cloud_free"
directory2 = "F:/Modis/MODIS_all/cloud_free"

## Marlin Folder:
# directory1 = "F:/GEO411_data/Sentinel_Daten/selected/cloud_free"
# directory2 = "F:/GEO411_data/MODIS_Daten/MODIS_download/cloud_free"

### ----- TIFF Data ----- ###
## Jonas Folder:
# directory = "F:/Sentinel_3/S3_Daten-20200622T143538Z-001/S3_Daten"
# directory = "F:/411/LST/GeoTIFF/Thuringia/scaled/cloud_free"
directory = "F:/Modis/MODIS_all/cloud_free"
## Marlin Folder:
#directory = "F:/GEO411_data/Sentinel_Daten/selected/cloud_free/"
# directory = "F:/GEO411_data/MODIS_Daten/MODIS_download/cloud_free/"

SENTINEL_timestamp_list = []
MODIS_doy_list = []
MODIS_timestamp_list = []
overlap_doy_list = []

def extract_SENTINEL_timestamp(directory1):
    """
    extracts the acquisition date of SENTINEL scenes sorted earlier on into a new list
    :return:
    """

    for filename in os.listdir(directory1):
        timestamp = filename[8:18]
        SENTINEL_timestamp_list.append(os.path.join(timestamp))

    print("Sentinel_list:")
    print(SENTINEL_timestamp_list)

extract_SENTINEL_timestamp(directory1)


def extract_MODIS_timestamp_all_years(directory2):
    """
    extracts the acquisition date of MODIS scenes into a new list
    ## for more information see: https://stackoverflow.com/questions/2427555/python-question-year-and-day-of-year-to-date
    :return:
    """
    years = [2018, 2019, 2020]
    for i, year in enumerate (years):
        for filename in os.listdir(directory2):
            timestamp = filename[13:16]
            MODIS_doy_list.append(os.path.join(timestamp))
            for doy in range(len(MODIS_doy_list)):
                doy = date.fromordinal(date(years[i], 1, 1).toordinal() + int(timestamp)-1)
                doy = str(doy)
            # print(str(doy))
            MODIS_timestamp_list.append(doy)

    # print(MODIS_doy_list)
    print("Modis_list:")
    print(MODIS_timestamp_list)

extract_MODIS_timestamp_all_years(directory2)

## Compare the temporal overlap between SENTINEL and MODIS Data
## For more information see: https://stackoverflow.com/questions/52464978/how-do-i-print-elements-of-one-list-that-are-in-another-list
c = set(SENTINEL_timestamp_list) & set(MODIS_timestamp_list)
overlap_list = list(c)
print("SENTINEL/MODIS SCENES WITH TEMPORAL OVERLAP:")
print(overlap_list)
print(len(overlap_list))


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


def select_SENTINEL_scenes():
    new_list = extract_files_to_list(path_to_folder=directory)
    final_tifs_selected = directory + "/final_sentinel_selected"
    if os.path.exists(final_tifs_selected):
        shutil.rmtree(final_tifs_selected)
    os.mkdir(directory + "/final_sentinel_selected")
    for i, element in enumerate(overlap_list):
        for j, tiff in enumerate(new_list):
            if overlap_list[i] in new_list[j]:
                print(new_list[j])
                shutil.copy(new_list[j], final_tifs_selected)

# select_SENTINEL_scenes()

def reconversion():
    year_list = [2018, 2019, 2020]
    for a, doy in enumerate(overlap_list):
        modis_date = pd.to_datetime(overlap_list[a], format='%Y-%m-%d')
        modis_date_year = str(modis_date)[0:4]
        new_year_day = pd.Timestamp(year=int(modis_date_year), month=1, day=1)
        doy_temp = str((modis_date - new_year_day).days + 1)
        if len(doy_temp) == 2:
            doy_temp = "0" + doy_temp
        overlap_doy_list.append(doy_temp)

    return overlap_doy_list

# reconversion()

def select_MODIS_scenes():
    new_list = extract_files_to_list(path_to_folder=directory)
    final_tifs_selected = directory + "/final_modis_selected"
    if os.path.exists(final_tifs_selected):
        shutil.rmtree(final_tifs_selected)
    os.mkdir(directory + "/final_modis_selected")
    overlap_doy_list = reconversion()
    print(overlap_doy_list)
    for i, element in enumerate(overlap_doy_list):
        for j, tiff in enumerate(new_list):
            #print(overlap_doy_list[i])
            if overlap_doy_list[i] in str(new_list[j]):
                # print(overlap_doy_list[i])
                ### change index method to find method in string
                # print(str(new_list[j] [32:35]))
                shutil.copy(new_list[j], final_tifs_selected)


select_MODIS_scenes()
