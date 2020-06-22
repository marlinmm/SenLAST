import rasterio
from rasterio.mask import mask
import geopandas as gpd
shapefile = gpd.read_file("C:/Users/jz199/Documents/Studium/Master/2. Semester/Vorlesungsmitschriften/GEO411 - Landschaftsmanagement und Fernerkundung/Auszug_Daten_SandraBauer_MA/Auszug_Daten_SandraBauer_MA/Stationen_Thüringen_Umland_3x3box_reprojected.shp")
# extract the geometry in GeoJSON format
geoms = shapefile.geometry.values # list of shapely geometries
geometry = geoms[0] # shapely geometry
# transform to GeJSON format
from shapely.geometry import mapping
geoms = [mapping(geoms[0])]
# extract the raster values values within the polygon
with rasterio.open("F:/411/LST/GeoTIFF/Thuringia/scaled/MOD11A1.A2020153.h18v03.006_LST_Day_1km_latlon_wgs84_Thuringia_celsius.tif") as src:
     out_image, out_transform = mask(src, geoms, crop=True)

print(out_image)
