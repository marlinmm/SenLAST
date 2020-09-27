import os
from datetime import date
import shutil
import pandas as pd
from SenLAST.base_information import extract_files_to_list


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
    # SENTINEL_date_list.sort()
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
        hour_in_minutes = hour * 60
        minutes = filename[22:24]
        minutes = int(minutes)
        ges_minutes = hour_in_minutes + minutes
        ges_minutes = str(ges_minutes)
        SENTINEL_timestamp_list.append(os.path.join(ges_minutes))
    # print(SENTINEL_timestamp_list)
    return SENTINEL_timestamp_list


######################## MODIS DATE & TIME EXTRACTION ########################

def extract_MODIS_date(mod_directory):
    """
    extracts the acquisition date of MODIS scenes into a new list
    for more information see: https://stackoverflow.com/questions/2427555/python-question-year-and-day-of-year-to-date
    :return:
    """
    MODIS_date_list = []
    MODIS_doy_list = []

    # check if final folder already exists:
    # final_tifs_selected = mod_directory + "/final_modis_selected"
    # if os.path.exists(final_tifs_selected):
    #     shutil.rmtree(final_tifs_selected)

    for filename in os.listdir(mod_directory):
        year = filename[9:13]
        timestamp = filename[13:16]
        MODIS_doy_list.append(os.path.join(timestamp))
        for doy in range(len(MODIS_doy_list)):
            doy = date.fromordinal(date(int(year), 1, 1).toordinal() + int(timestamp) - 1)
            doy = str(doy)
        MODIS_date_list.append(doy)
    return MODIS_date_list


def extract_MODIS_timestamp(mod_directory):
    """
    extracts the acquisition time of MODIS scenes into a new list
    for more information see: https://stackoverflow.com/questions/2427555/python-question-year-and-day-of-year-to-date
    :return:
    """
    MODIS_timestamp_list = []

    for filename in os.listdir(mod_directory):
        hour = filename[54:56]
        hour = int(hour)
        hour_in_minutes = hour * 60
        minutes = filename[57:59]
        minutes = int(minutes)
        ges_minutes = hour_in_minutes + minutes
        ges_minutes = str(ges_minutes)
        MODIS_timestamp_list.append(os.path.join(ges_minutes))
    # print(MODIS_timestamp_list)
    return MODIS_timestamp_list


def extract_MODIS_timestamp_new(mod_directory):
    """
    extracts the acquisition time of MODIS scenes into a new list
    for more information see: https://stackoverflow.com/questions/2427555/python-question-year-and-day-of-year-to-date
    :return:
    """
    MODIS_timestamp_list = []

    for filename in os.listdir(mod_directory):
        hour = filename[35:37]

        hour = int(hour)
        hour_in_minutes = hour * 60
        minutes = filename[38:40]
        minutes = int(minutes)
        ges_minutes = hour_in_minutes + minutes
        ges_minutes = str(ges_minutes)
        MODIS_timestamp_list.append(os.path.join(ges_minutes))
    # print(MODIS_timestamp_list)
    return MODIS_timestamp_list


######################## COMPARISON FUNCTIONS - OLD AND WORKING ##########################

def compare(mod_directory, sen_directory):
    ## Compare the temporal overlap between SENTINEL and MODIS Data
    ## For more information see: https://stackoverflow.com/questions/52464978/how-do-i-print-elements-of-one-list-that-are-in-another-list
    new_sen_directory = sen_directory + "/selected/cloud_free"
    new_mod_directory = mod_directory + "/cloud_free"

    sentinel_data = extract_SENTINEL_date(sen_directory=new_sen_directory)
    modis_data = extract_MODIS_date(mod_directory=new_mod_directory)

    c = set(sentinel_data) & set(modis_data)
    overlap_list = list(c)
    return overlap_list


def select_SENTINEL_scenes(mod_directory, sen_directory):
    new_sen_directory = sen_directory + "/selected/cloud_free"
    new_list = extract_files_to_list(path_to_folder=new_sen_directory, datatype=".tif")
    overlap_list = compare(mod_directory=mod_directory, sen_directory=sen_directory)
    final_tifs_selected = sen_directory + "/final_sentinel_selected/"
    if os.path.exists(final_tifs_selected):
        shutil.rmtree(final_tifs_selected)
    os.mkdir(sen_directory + "/final_sentinel_selected/")
    for i, element in enumerate(overlap_list):
        for j, tiff in enumerate(new_list):
            if overlap_list[i] in new_list[j]:
                shutil.copy(new_list[j], final_tifs_selected)


def reconversion(mod_directory, sen_directory):
    overlap_list = compare(mod_directory=mod_directory, sen_directory=sen_directory)
    overlap_doy_list = []
    for a, doy in enumerate(overlap_list):
        modis_date = pd.to_datetime(overlap_list[a], format='%Y-%m-%d')
        modis_date_year = str(modis_date)[0:4]
        new_year_day = pd.Timestamp(year=int(modis_date_year), month=1, day=1)
        doy_temp = str((modis_date - new_year_day).days + 1)
        if len(doy_temp) == 2:
            doy_temp = "0" + doy_temp
        overlap_doy_list.append(doy_temp)
    return overlap_doy_list


def select_MODIS_data_scenes(mod_directory, sen_directory):
    new_mod_directory = mod_directory + "/cloud_free"
    new_list = extract_files_to_list(path_to_folder=new_mod_directory, datatype=".tif")
    final_tifs_selected = mod_directory + "/final_modis_selected/"
    overlap_doy_list = reconversion(sen_directory=sen_directory, mod_directory=mod_directory)
    if os.path.exists(final_tifs_selected):
        shutil.rmtree(final_tifs_selected)
    os.mkdir(mod_directory + "/final_modis_selected/")
    for i, element in enumerate(overlap_doy_list):
        for j, tiff in enumerate(new_list):
            if "Day" in str(new_list[j]):
                if overlap_doy_list[i][::-1] in str(new_list[j][-61:-64:-1]):
                    shutil.copy(new_list[j], final_tifs_selected)
            if "Night" in str(new_list[j]):
                if overlap_doy_list[i][::-1] in str(new_list[j][-63:-66:-1]):
                    shutil.copy(new_list[j], final_tifs_selected)


def select_MODIS_time_scenes(mod_time_directory, sen_directory):
    new_mod_directory = mod_time_directory + "/cloud_free"
    new_list = extract_files_to_list(path_to_folder=new_mod_directory, datatype=".tif")
    final_tifs_selected = mod_time_directory + "/final_modis_selected/"
    overlap_doy_list = reconversion(sen_directory=sen_directory, mod_directory=mod_time_directory)
    if os.path.exists(final_tifs_selected):
        shutil.rmtree(final_tifs_selected)
    os.mkdir(mod_time_directory + "/final_modis_selected/")
    for i, element in enumerate(overlap_doy_list):
        for j, tiff in enumerate(new_list):
            if "Day" in str(new_list[j]):
                if overlap_doy_list[i][::-1] in str(new_list[j][-55:-58:-1]):
                    shutil.copy(new_list[j], final_tifs_selected)
            if "Night" in str(new_list[j]):
                if overlap_doy_list[i][::-1] in str(new_list[j][-57:-60:-1]):
                    shutil.copy(new_list[j], final_tifs_selected)

