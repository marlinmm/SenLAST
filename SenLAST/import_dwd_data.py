import numpy as np
import csv
from SenLAST.comparison import *
from SenLAST.base_information import import_polygons

#satellite_data = "C:/Users/marli/Google Drive/Studium/Master/2.Semester/GEO411/Praxis/Datenpaare/All/"
csv_folder = "F:/GEO411_data/DWD_result_all/"

MODIS_directory = "F:/GEO411_data/MODIS_Daten/hour_match"
Sentinel_directory = "F:/GEO411_data/Sentinel_Daten/hour_match"

def import_DWD_data():
    sen_date = extract_SENTINEL_date(sen_directory=Sentinel_directory)
    sen_time = extract_SENTINEL_timestamp(sen_directory=Sentinel_directory)

    mod_date = extract_MODIS_date(mod_directory=MODIS_directory)
    mod_time = extract_MODIS_timestamp_new(mod_directory=MODIS_directory)

    #print(sen_date)
    #print(sen_time)

    #print("  ")

    #print(mod_date)
    #print(mod_time)

    station_list = []
    sen_date_time = []
    mod_date_time = []

    for i, elem in enumerate(sen_date):
        year = sen_date[i][0:4]
        month = sen_date[i][5:7]
        day = sen_date[i][8:10]

        hour = int(sen_time[i]) // 60
        if hour < 10:
            hour = "0" + str(hour)
        minute = round(int(sen_time[i]) % 60, -1)
        if minute == 60:
            hour = hour + 1
            minute = "00"
        sen_date_time.append(year + month + day + str(hour) + str(minute))
    print(sen_date_time)


    with open(csv_folder + "combined__2750_Kronach.csv", newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        for row in spamreader:
            station_list.append(', '.join(row))
        for j, date in enumerate(sen_date_time):
            matching = [s for s in station_list if date in s]
            print(matching)

        print(len(station_list))
        print(station_list[288 + 127])
        print(len(station_list[2]))

    # Sentinel_shapefile = "F:/GEO411_data/Daten_Sandra/new/Stationen_Thüringen_Umland_3x3box.shp"
    # print(import_polygons(shape_path=Sentinel_shapefile))
    #
import_DWD_data()