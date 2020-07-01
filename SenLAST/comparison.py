import os
from datetime import date
import shutil
import pandas as pd
from SenLAST.base_information import extract_files_to_list


def extract_SENTINEL_timestamp(sen_directory):
    """
    extracts the acquisition date of SENTINEL scenes sorted earlier on into a new list
    :return:
    """
    SENTINEL_timestamp_list = []

    for filename in os.listdir(sen_directory):
        timestamp = filename[8:18]
        SENTINEL_timestamp_list.append(os.path.join(timestamp))
    return SENTINEL_timestamp_list


def extract_MODIS_timestamp(mod_directory):
    """
    extracts the acquisition date of MODIS scenes into a new list
    ## for more information see: https://stackoverflow.com/questions/2427555/python-question-year-and-day-of-year-to-date
    :return:
    """
    MODIS_timestamp_list = []
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
            MODIS_timestamp_list.append(doy)
    return MODIS_timestamp_list


def compare(mod_directory, sen_directory):
    ## Compare the temporal overlap between SENTINEL and MODIS Data
    ## For more information see: https://stackoverflow.com/questions/52464978/how-do-i-print-elements-of-one-list-that-are-in-another-list
    new_sen_directory = sen_directory + "/selected/cloud_free"
    new_mod_directory = mod_directory + "/cloud_free"

    sentinel_data = extract_SENTINEL_timestamp(sen_directory=new_sen_directory)
    modis_data = extract_MODIS_timestamp(mod_directory=new_mod_directory)

    c = set(sentinel_data) & set(modis_data)
    overlap_list = list(c)
    return overlap_list


def select_SENTINEL_scenes(mod_directory, sen_directory):
    new_sen_directory = sen_directory + "/selected/cloud_free"
    new_list = extract_files_to_list(path_to_folder=new_sen_directory)
    overlap_list = compare(mod_directory=mod_directory, sen_directory=sen_directory)
    final_tifs_selected = new_sen_directory + "/final_sentinel_selected/"
    if os.path.exists(final_tifs_selected):
        shutil.rmtree(final_tifs_selected)
    os.mkdir(new_sen_directory + "/final_sentinel_selected/")
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
