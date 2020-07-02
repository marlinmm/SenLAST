import os
from datetime import date
import shutil
import pandas as pd
from SenLAST.base_information import extract_files_to_list
import numpy as np

######################## SENTINEL DATE & TIME EXTRACTION ########################

def extract_SENTINEL_date(sen_directory):
    """
    extracts the acquisition date of SENTINEL scenes sorted earlier on into a new list
    :return:
    """
    SENTINEL_date_list = []

    for filename in os.listdir(sen_directory):
        timestamp = filename[8:18]
        SENTINEL_date_list.append(os.path.join(timestamp))
    return SENTINEL_date_list


def extract_SENTINEL_timestamp(sen_directory):
    """
    extracts the acquisition time of SENTINEL scenes sorted earlier on into a new list
    :return:
    """
    SENTINEL_timestamp_list = []

    for filename in os.listdir(sen_directory):
        hour = filename[19:21]
        hour = int(hour)
        hour_in_minutes = hour*60
        minutes = filename[22:24]
        minutes = int(minutes)
        ges_minutes = hour_in_minutes+minutes
        ges_minutes = str(ges_minutes)
        SENTINEL_timestamp_list.append(os.path.join(ges_minutes))
    # print(SENTINEL_timestamp_list)
    return SENTINEL_timestamp_list

######################## MODIS DATE & TIME EXTRACTION ########################

def extract_MODIS_date(mod_directory):
    """
    extracts the acquisition date of MODIS scenes into a new list
    ## for more information see: https://stackoverflow.com/questions/2427555/python-question-year-and-day-of-year-to-date
    :return:
    """
    MODIS_date_list = []
    MODIS_doy_list = []

    # check if final folder already exists:
    final_tifs_selected = mod_directory + "/final_modis_selected"
    if os.path.exists(final_tifs_selected):
        shutil.rmtree(final_tifs_selected)

    years = [2018, 2019, 2020]
    for i, year in enumerate(years):
        for filename in os.listdir(mod_directory):
            timestamp = filename[13:16]
            MODIS_doy_list.append(os.path.join(timestamp))
            for doy in range(len(MODIS_doy_list)):
                doy = date.fromordinal(date(years[i], 1, 1).toordinal() + int(timestamp)-1)
                doy = str(doy)
            MODIS_date_list.append(doy)
    return MODIS_date_list


def extract_MODIS_timestamp(mod_directory):
    """
    extracts the acquisition time of MODIS scenes into a new list
    ## for more information see: https://stackoverflow.com/questions/2427555/python-question-year-and-day-of-year-to-date
    :return:
    """
    MODIS_timestamp_list = []

    for filename in os.listdir(mod_directory):
        hour = filename[35:37]
        hour = int(hour)
        hour_in_minutes = hour * 60
        minutes = filename[37:39]
        minutes = int(minutes)
        ges_minutes = hour_in_minutes + minutes
        ges_minutes = str(ges_minutes)
        MODIS_timestamp_list.append(os.path.join(ges_minutes))
    # print(MODIS_timestamp_list)
    return MODIS_timestamp_list

######################## COMPARISON FUNCTIONS ##########################

def compare_date(mod_directory, sen_directory):
    """
    Compares the temporal (date) overlap between SENTINEL and MODIS Data
    - For more information see: https://stackoverflow.com/questions/52464978/how-do-i-print-elements-of-one-list-that-are-in-another-list
    """
    date_sen_directory = sen_directory + "/selected/cloud_free"
    date_mod_directory = mod_directory + "/cloud_free"

    sentinel_date_data = extract_SENTINEL_date(sen_directory=date_sen_directory)
    modis_date_data = extract_MODIS_date(mod_directory=date_mod_directory)

    c = set(sentinel_date_data) & set(modis_date_data)
    overlap_date_list = list(c)
    print(overlap_date_list)
    # return overlap_date_list

def compare_timestamp(mod_directory, sen_directory):
    """
    Compares the temporal (time) overlap between SENTINEL and MODIS Data
    - For more information see: https://stackoverflow.com/questions/52464978/how-do-i-print-elements-of-one-list-that-are-in-another-list
    """
    time_sen_directory = sen_directory + "/selected/cloud_free"
    time_mod_directory = mod_directory + "/cloud_free"

    sentinel_timestamp_data = extract_SENTINEL_timestamp(sen_directory=time_sen_directory)
    modis_timestamp_data = extract_MODIS_timestamp(mod_directory=time_mod_directory)

    overlap_time_list = []

    for x in sentinel_timestamp_data:
        for y in modis_timestamp_data:
            xa = int(x)+45
            xb = int(x)-45
            y =int(y)

            if y <= xa and y >= xb:
                overlap_time_list.append("True")
            else:
                overlap_time_list.append("False")
    print(overlap_time_list)


# def select_SENTINEL_scenes(mod_directory, sen_directory):
#     new_sen_directory = sen_directory + "/selected/cloud_free"
#     new_list = extract_files_to_list(path_to_folder=new_sen_directory)
#     overlap_date_list = compare_date(mod_directory=mod_directory, sen_directory=sen_directory)
#     final_tifs_selected = new_sen_directory + "/final_sentinel_selected/"
#     if os.path.exists(final_tifs_selected):
#         shutil.rmtree(final_tifs_selected)
#     os.mkdir(new_sen_directory + "/final_sentinel_selected/")
#     for i, element in enumerate(overlap_date_list):
#         for j, tiff in enumerate(new_list):
#             if overlap_date_list[i] in new_list[j]:
#                 shutil.copy(new_list[j], final_tifs_selected)


def select_SENTINEL_scenes(mod_directory, sen_directory):
    new_sen_directory = sen_directory + "/selected/cloud_free"
    new_list = extract_files_to_list(path_to_folder=new_sen_directory)
    overlap_date_list = compare_date(mod_directory=mod_directory, sen_directory=sen_directory)
    overlap_time_list = compare_timestamp(mod_directory=mod_directory, sen_directory=sen_directory)
    final_tifs_selected = new_sen_directory + "/final_sentinel_selected/"
    if os.path.exists(final_tifs_selected):
        shutil.rmtree(final_tifs_selected)
    os.mkdir(new_sen_directory + "/final_sentinel_selected/")
    for i, element in enumerate(overlap_date_list):
        for j, tiff in enumerate(new_list):
            if overlap_date_list[i] in new_list[j]:
                for k, booltime in enumerate(overlap_time_list):
                    if overlap_time_list[k] == True:
                        shutil.copy(new_list[j], final_tifs_selected)

# funktioniert nur für den Fall, wenn overlap_time_list komplett false ist
# funktioniert auch noch nicht wenn es unterschiedliche Tage sind - denk ich zumindest
# ab hier: nachfolgenden MODIS-Funktionen sind noch nicht auf neue Methodik angepasst

def reconversion(mod_directory, sen_directory):
    overlap_date_list = compare_date(mod_directory=mod_directory, sen_directory=sen_directory)
    overlap_doy_list = []
    for a, doy in enumerate(overlap_date_list):
        modis_date = pd.to_datetime(overlap_date_list[a], format='%Y-%m-%d')
        modis_date_year = str(modis_date)[0:4]
        new_year_day = pd.Timestamp(year=int(modis_date_year), month=1, day=1)
        doy_temp = str((modis_date - new_year_day).days + 1)
        if len(doy_temp) == 2:
            doy_temp = "0" + doy_temp
        overlap_doy_list.append(doy_temp)
    return overlap_doy_list


def select_MODIS_scenes(mod_directory, sen_directory):
    new_mod_directory = mod_directory + "/cloud_free"
    new_list = extract_files_to_list(path_to_folder=new_mod_directory)
    final_tifs_selected = new_mod_directory + "/final_modis_selected/"
    overlap_doy_list = reconversion(sen_directory=sen_directory, mod_directory=mod_directory)
    if os.path.exists(final_tifs_selected):
        shutil.rmtree(final_tifs_selected)
    os.mkdir(new_mod_directory+ "/final_modis_selected/")
    for i, element in enumerate(overlap_doy_list):
        for j, tiff in enumerate(new_list):
            if overlap_doy_list[i] in str(new_list[j]):
                ### change index method to find method in string
                shutil.copy(new_list[j], final_tifs_selected)
