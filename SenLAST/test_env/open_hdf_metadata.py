import os
import sys
import rasterio as rio

directory = "F:/GEO411_data/MODIS_Daten/hdf_test/"



def extract_files_to_list(path_to_folder):
    """
    finds all .tif-files in the corresponding directory
    :return:
    """
    new_list = []

    for filename in os.listdir(path_to_folder):
        if filename.endswith(".hdf"):
            new_list.append(os.path.join(path_to_folder, filename))
        else:
            continue
    return new_list


def open_hdf_metadata():
    select_hdfs = extract_files_to_list(path_to_folder=directory)
    for i, hdf in enumerate(select_hdfs):
        src1 = rio.open(select_hdfs[i])
        hdf_meta = src1.meta
        print(hdf_meta)

open_hdf_metadata()