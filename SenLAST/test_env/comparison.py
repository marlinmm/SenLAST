from datetime import datetime
import os
from datetime import date


start_time = datetime.now()

### ----- TIFF Data ----- ###
## Jonas Folder:
# directory = "F:/Sentinel_3/S3_Daten-20200622T143538Z-001/S3_Daten"
#directory1 = "C:/Users/jz199/Documents/Studium/Master/2. Semester/Vorlesungsmitschriften/GEO411 - Landschaftsmanagement und Fernerkundung/Sentinel 3 Daten Uni Jena/Sentinel 3 Daten Uni Jena/2019/06_2019_Juni/S3A"
#directory2 = "F:/411/LST/GeoTIFF/Thuringia/scaled/cloud_free"
## Marlin Folder:
directory1 = "F:/GEO411_data/Sentinel_Daten/selected/cloud_free"
directory2 = "F:/GEO411_data/MODIS_Daten/MODIS_download/cloud_free"

SENTINEL_timestamp_list = []
MODIS_doy_list = []
MODIS_timestamp_list = []

def extract_SENTINEL_timestamp(directory1):
    """
    extracts the acquisition date of SENTINEL scenes into a new list
    :return:
    """

    for filename in os.listdir(directory1):
        timestamp = filename[8:18]
        SENTINEL_timestamp_list.append(os.path.join(timestamp))

    print(SENTINEL_timestamp_list)

extract_SENTINEL_timestamp(directory1)


def extract_MODIS_timestamp(directory2, year):
    """
    extracts the acquisition date of MODIS scenes into a new list
    ## for more information see: https://stackoverflow.com/questions/2427555/python-question-year-and-day-of-year-to-date
    :return:
    """

    for filename in os.listdir(directory2):
        timestamp = filename[13:16]
        MODIS_doy_list.append(os.path.join(timestamp))
        for doy in range(len(MODIS_doy_list)):
            doy = date.fromordinal(date(year, 1, 1).toordinal() + int(timestamp)-1)
            doy = str(doy)
        # print(str(doy))
        MODIS_timestamp_list.append(doy)

    # print(MODIS_doy_list)
    print(MODIS_timestamp_list)


#extract_MODIS_timestamp(directory2, 2020)


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
    print(MODIS_timestamp_list)


extract_MODIS_timestamp_all_years(directory2)

## Compare the temporal overlap between SENTINEL and MODIS Data
## For more information see: https://stackoverflow.com/questions/52464978/how-do-i-print-elements-of-one-list-that-are-in-another-list
c = set(SENTINEL_timestamp_list) & set(MODIS_timestamp_list)
overlap_list = []
print("SENTINEL/MODIS SCENES WITH TEMPORAL OVERLAP:")
print('\n'.join(str(i) for i in c))
