from datetime import datetime

import fiona
import rasterio as rio
import rasterio.mask
import numpy as np
import csv
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig

list_list = []

start_time = datetime.now()

def mask_raster_test():
    import numpy as np
    shape_list = []

    for h in range(0,19):
        ## Shapefile Marlin:
        # shapefolder = "F:/GEO411_data/Daten_Sandra/new/"
        ## Shapefile Jonas:
        shapefolder = "C:/Users/jz199/Documents/Studium/Master/2. Semester/Vorlesungsmitschriften/GEO411 - Landschaftsmanagement und Fernerkundung/Auszug_Daten_SandraBauer_MA/Auszug_Daten_SandraBauer_MA/"

        inputshape = "Stationen_Thüringen_Umland_3x3box.shp"
        shapefile = fiona.open(shapefolder+inputshape, "r")

        shapes = [feature["geometry"] for feature in shapefile]
        shape_list.append(shapes)
    print(len(shapes))
    print(shape_list)
    print(shape_list[0][0])

    list_means = []

    for i in range(0, len(shape_list)+1):
        ######## SENTINEL ########
        ## TIFF-File Marlin:
        Sentinel_folder = "F:/GEO411_data/MODIS_R_dir/Downloaded_HDFs/GeoTIFF/Thuringia/scaled/MOD11A1.A2018184.h18v03.006_LST_Day_1km_latlon_wgs84_Thuringia_celsius.tif"
        Sentinel_file = ""

        ## TIFF-File Jonas:
        Sentinel_folder = "C:/Users/jz199/Documents/Studium/Master/2. Semester/Vorlesungsmitschriften/GEO411 - Landschaftsmanagement und Fernerkundung/Sentinel 3 Daten Uni Jena/Sentinel 3 Daten Uni Jena/2018/07_2018_Juli/S3A/"
        Sentinel_file = "S3A_LST_2018-07-23_20h54m_371_NIGHT_1km_utm32_etrs89.tif"

        # ------------------------------------------------------------------------------#

        ######## MODIS ########
        ## TIFF-File Marlin:
        Modis_folder = "F:/GEO411_data/MODIS_R_dir/Downloaded_HDFs/GeoTIFF/Thuringia/scaled/MOD11A1.A2018184.h18v03.006_LST_Day_1km_latlon_wgs84_Thuringia_celsius.tif"
        Modis_file = ""

        ## TIFF-File Jonas:
        Modis_folder = "F:/411/LST/GeoTIFF/Thuringia/scaled/"
        Modis_file = "MOD11A1.A2020153.h18v03.006_LST_Day_1km_latlon_wgs84_Thuringia_celsius.tif"

        # ------------------------------------------------------------------------------#

        # Select between MODIS and SENTINEL
        src1 = Sentinel_folder + Sentinel_file
        # src1 = Modis_folder + Modis_file

        # ------------------------------------------------------------------------------#

        src1 = rio.open("C:/Users/jz199/Documents/Studium/Master/2. Semester/Vorlesungsmitschriften/GEO411 - Landschaftsmanagement und Fernerkundung/Sentinel 3 Daten Uni Jena/Sentinel 3 Daten Uni Jena/2018/07_2018_Juli/S3A/S3A_LST_2018-07-23_20h54m_371_NIGHT_1km_utm32_etrs89.tif")
        out_image1, out_transform1 = rasterio.mask.mask(src1, [shape_list[0][i]], all_touched=0, crop=True, nodata= np.nan)
        ras_meta1 = src1.profile
        ras_meta1.update({"driver": "GTiff",
                         "height": out_image1.shape[1],
                         "width": out_image1.shape[2],
                         "transform": out_transform1,
                         "nodata": 0. })

        list_means.append(np.nanmean(out_image1))
        # print(out_image1)

    print(list_means)
    print(len(list_means))

#### activate for testing this file standalone ####
mask_raster_test()

statistics_time = datetime.now()
print("breakpoint-time = ", statistics_time - start_time, "Hr:min:sec")


###---Infos zum Plotten von Graphen---###
# fig, ax1 = plt.subplots()
#
# # color = '#bebebe'
# #plt.title('Edge Detection (VH vs. VV ' + str(i+1) + ')')
# ax1.set_xlabel('No. of values')
# # ax1.plot(original_VH, color=color, linewidth=1)
# #
# # color = 'tab:red'
# # ax1.set_ylabel('median', color=color)  # we already handled the x-label with ax1
# # ax1.plot(median_filter_VH, color=color)
# # ax1.tick_params(axis='y', labelcolor=color)
# #
# # ax3 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
# #
# # color = 'tab:green'
# # ax3.set_ylabel('Edge detection', color=color)  # we already handled the x-label with ax1
# # ax3.plot(sobel_filter_VH, color=color)
# # ax3.tick_params(axis='y', labelcolor=color)
#
# # color = '#bebebe'
# # ax1.set_xlabel('no. of values')
# # ax1.plot(original_VH, color=color, linewidth=1)
# plt.ylim(-30, 60)
# color = 'tab:green'
# ax1.set_ylabel('Edge Detection VH', color=color)  # we already handled the x-label with ax1
# ax1.plot(sobel_filter_VH, color=color)
# ax1.tick_params(axis='y', labelcolor=color)
#
# ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
# plt.ylim(-30, 60)
# color = 'tab:red'
# ax2.set_ylabel('Edge Detection VV', color=color)  # we already handled the x-label with ax1
# ax2.plot(sobel_filter_VV, color=color)
# ax2.tick_params(axis='y', labelcolor=color)
#
# #color = 'tab:blue'
# #ax3.plot(data4, color=color)
#
# #color = '#ffff00'
# #ax3.plot(data5, color=color)
#
# fig.tight_layout()  # otherwise the right y-label is slightly clipped
#
# plt.show()
