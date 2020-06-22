import fiona
import rasterio as rio
import rasterio.mask
import numpy as np
import csv
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig

list_list = []


def mask_raster_test():
    import numpy as np
    shape_list = []

    for h in range(0,19):
        ## Shapefile Marlin:
        # shapefile = fiona.open("F:/GEO411_data/Daten_Sandra/new/Stationen_Thüringen_Umland_3x3box_reprojected.shp", "r")
        ## Shapefile Jonas:
        shapefile = fiona.open("C:/Users/jz199/Documents/Studium/Master/2. Semester/Vorlesungsmitschriften/GEO411 - Landschaftsmanagement und Fernerkundung/Auszug_Daten_SandraBauer_MA/Auszug_Daten_SandraBauer_MA/Stationen_Thüringen_Umland_3x3box_reprojected.shp")

        shapes = [feature["geometry"] for feature in shapefile]
        shape_list.append(shapes)
    print(len(shapes))
    print(shape_list)
    print(shape_list[0][0])

    list_means = []

    for i in range(0, len(shape_list)):
        ## Tiff-File Marlin:
        # src1 = rio.open("F:/GEO411_data/MODIS_R_dir/Downloaded_HDFs/GeoTIFF/Thuringia/scaled/MOD11A1.A2018184.h18v03.006_LST_Day_1km_latlon_wgs84_Thuringia_celsius.tif")
        ## Tiff-File Jonas:
        src1 = rio.open("F:/411/LST/GeoTIFF/Thuringia/scaled/MOD11A1.A2020153.h18v03.006_LST_Day_1km_latlon_wgs84_Thuringia_celsius.tif")
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

#### activate for testing this file standalone ####
mask_raster_test()




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
