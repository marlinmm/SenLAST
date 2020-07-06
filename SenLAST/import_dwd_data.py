import numpy as np
import csv
from SenLAST.comparison import extract_SENTINEL_date, extract_SENTINEL_timestamp, extract_MODIS_date, extract_MODIS_timestamp
from SenLAST.base_information import import_polygons

#satellite_data = "C:/Users/marli/Google Drive/Studium/Master/2.Semester/GEO411/Praxis/Datenpaare/All/"
csv_folder = "C:/Users/marli/Google Drive/Studium/Master/2.Semester/GEO411/Praxis/DWD_Daten/379_Bad_Berka/Historisch/"

MODIS_directory = "F:/GEO411_data/test/small/mod"
Sentinel_directory = "F:/GEO411_data/test/small/sen"

sen_date = extract_SENTINEL_date(sen_directory=Sentinel_directory)
sen_time = extract_SENTINEL_timestamp(sen_directory=Sentinel_directory)

mod_date = extract_MODIS_date(mod_directory=MODIS_directory)
mod_time = extract_MODIS_timestamp(mod_directory=MODIS_directory)

print(sen_date)
print(sen_time)

print(mod_date)
print(mod_time)



# station_list = []
#
# with open(csv_folder + "produkt_zehn_min_tu_20170901_20191231_00379.csv", newline='') as csvfile:
#     spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
#     for row in spamreader:
#         station_list.append(', '.join(row))
#     print(station_list[2][0:20])
#     print(len(station_list[2]))
#
# Sentinel_shapefile = "F:/GEO411_data/Daten_Sandra/new/Stationen_Thüringen_Umland_3x3box.shp"
# print(import_polygons(shape_path=Sentinel_shapefile))
#
