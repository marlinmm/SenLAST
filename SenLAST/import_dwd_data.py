import numpy as np
import csv
from SenLAST.comparison import *
from SenLAST.base_information import import_polygons

#satellite_data = "C:/Users/marli/Google Drive/Studium/Master/2.Semester/GEO411/Praxis/Datenpaare/All/"
csv_folder = "F:/GEO411_data/DWD_result_all/"

MODIS_directory = "F:/GEO411_data/MODIS_Daten/MODIS_download/final_modis_selected"
Sentinel_directory = "F:/GEO411_data/test/small/sen"

sen_date = extract_SENTINEL_date(sen_directory=Sentinel_directory)
sen_time = extract_SENTINEL_timestamp(sen_directory=Sentinel_directory)

mod_date = extract_MODIS_date(mod_directory=MODIS_directory)
mod_time = extract_MODIS_timestamp_new(mod_directory=MODIS_directory)

print(sen_date)
print(sen_time)

print(mod_date)
print(mod_time)



station_list = []

with open(csv_folder + "combined__2750_Kronach.csv", newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
    for row in spamreader:
        station_list.append(', '.join(row))
    print(station_list[416])
    print(len(station_list[2]))

# Sentinel_shapefile = "F:/GEO411_data/Daten_Sandra/new/Stationen_Thüringen_Umland_3x3box.shp"
# print(import_polygons(shape_path=Sentinel_shapefile))
#
