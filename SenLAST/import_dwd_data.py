import numpy as np
import csv
from SenLAST.comparison import *
from SenLAST.base_information import *


def import_DWD_data_Sentinel(sen_directory, csv_directory):
    sen_date = extract_SENTINEL_date_forDWD(sen_directory=sen_directory)
    print(sen_date)
    sen_date.sort()
    print(sen_date)
    sen_time = extract_SENTINEL_timestamp_forDWD(sen_directory=sen_directory)
    sen_date_time = []
    csv_file_list = extract_files_to_list(path_to_folder=csv_directory, datatype=".csv")

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

    for j, file in enumerate(csv_file_list):
        station_list = []
        with open(file, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
            value_list = []
            for row in spamreader:
                station_list.append(', '.join(row))
            for date in sen_date_time:
                matching = [s for s in station_list if date in s]
                value_list.append(matching)
        with open(file[0:len(file)-4] + "-3A" + ".csv", "w", newline='') as new_csvfile:
            wt = csv.writer(new_csvfile, quoting=csv.QUOTE_ALL)
            wt.writerows(value_list)


def import_DWD_data_MODIS(mod_directory, csv_directory):
    mod_date = extract_MODIS_date(mod_directory=mod_directory)
    mod_time = extract_MODIS_timestamp(mod_directory=mod_directory)
    mod_date_time = []
    csv_file_list = extract_files_to_list(path_to_folder=csv_directory, datatype=".csv")

    for i, elem in enumerate(mod_date):
        year = mod_date[i][0:4]
        month = mod_date[i][5:7]
        day = mod_date[i][8:10]
        hour = int(mod_time[i]) // 60
        minute = round(int(mod_time[i]) % 60, -1)
        if minute == 60:
            hour = int(hour) + 1
            minute = "00"
        if hour < 10:
            hour = "0" + str(hour)
        mod_date_time.append(year + month + day + str(hour) + str(minute))
    for j, file in enumerate(csv_file_list):
        station_list = []
        with open(file, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
            value_list = []
            for row in spamreader:
                station_list.append(', '.join(row))
            for date in mod_date_time:
                matching = [s for s in station_list if date in s]
                value_list.append(matching)
        with open(file[0:len(file)-4] + "_MODIS" + ".csv", "w", newline='') as new_csvfile:
            wt = csv.writer(new_csvfile, quoting=csv.QUOTE_ALL)
            wt.writerows(value_list)