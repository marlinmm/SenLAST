import rasterio
from rasterio.mask import mask
import geopandas as gpd

## Jonas Path:
path_to_shape = "C:/Users/jz199/Documents/Studium/Master/2. Semester/Vorlesungsmitschriften/GEO411 - Landschaftsmanagement und Fernerkundung/Auszug_Daten_SandraBauer_MA/Auszug_Daten_SandraBauer_MA/Stationen_Thüringen_Umland_3x3box_reprojected.shp"
path_to_raster = "F:/411/LST/GeoTIFF/Thuringia/scaled/MOD11A1.A2020153.h18v03.006_LST_Day_1km_latlon_wgs84_Thuringia_celsius.tif"

## Marlin Path:
#path_to_shape = "F:/GEO411_data/Daten_Sandra/new/Stationen_Thüringen_Umland_3x3box_reprojected.shp"
#path_to_raster = "F:/GEO411_data/MODIS_R_dir/Downloaded_HDFs/GeoTIFF/Thuringia/scaled/MOD11A1.A2018184.h18v03.006_LST_Day_1km_latlon_wgs84_Thuringia_celsius.tif"

shapefile = gpd.read_file(path_to_shape)
# extract the geometry in GeoJSON format
geoms = shapefile.geometry.values # list of shapely geometries
geometry = geoms[0] # shapely geometry
# transform to GeJSON format
from shapely.geometry import mapping
geoms = [mapping(geoms[0])]
# extract the raster values values within the polygon
with rasterio.open(path_to_raster) as src:
     out_image, out_transform = mask(src, geoms, crop=True)

print(out_image)
