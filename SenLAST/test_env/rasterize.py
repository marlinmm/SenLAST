# All this stuff is sourced from here:
# https://gist.github.com/perrygeo/721040f8545272832a42#file-pctcover-png
### more info:
### https://github.com/mapbox/rasterio/issues/232


import rasterio
import fiona
import numpy as np
from rasterio import features
from affine import Affine
from shapely.geometry import shape, box

def _rasterize_geom(geom, shape, affinetrans, all_touched):
    indata = [(geom, 1)]
    rv_array = features.rasterize(
        indata,
        out_shape=shape,
        transform=affinetrans,
        fill=0,
        all_touched=all_touched)
    return rv_array


def rasterize_pctcover(geom, atrans, shape):
    alltouched = _rasterize_geom(geom, shape, atrans, all_touched=True)
    exterior = _rasterize_geom(geom.exterior, shape, atrans, all_touched=True)

    # Create percent cover grid as the difference between them
    # at this point all cells are known 100% coverage,
    # we'll update this array for exterior points
    pctcover = (alltouched - exterior) * 100

    # loop through indicies of all exterior cells
    for r, c in zip(*np.where(exterior == 1)):

        # Find cell bounds, from rasterio DatasetReader.window_bounds
        window = ((r, r+1), (c, c+1))
        ((row_min, row_max), (col_min, col_max)) = window
        x_min, y_min = (col_min, row_max) * atrans
        x_max, y_max = (col_max, row_min) * atrans
        bounds = (x_min, y_min, x_max, y_max)

        # Construct shapely geometry of cell
        cell = box(*bounds)

        # Intersect with original shape
        cell_overlap = cell.intersection(geom)

        # update pctcover with percentage based on area proportion
        coverage = cell_overlap.area / cell.area
        pctcover[r, c] = int(coverage * 100)

    return pctcover


if __name__ == "__main__":
    with fiona.open("test.geojson") as src:
        geom = shape(next(src)['geometry'])  # take first feature's shapely geometry

    scale = 20
    atrans = Affine(1.0 / scale, 0.0, 0.0, 0.0, -1.0 / scale, 5.0)
    shape = (5 * scale, 5 * scale)
    profile = {
        'affine': atrans,
        'height': shape[0],
        'width': shape[1],
        'count': 1,
        'crs': {},
        'driver': 'GTiff',
        'dtype': 'uint8',
        'nodata': None,
        'tiled': False}

    pctcover = rasterize_pctcover(geom, atrans=atrans, shape=shape)
    with rasterio.open('percent_cover.tif', 'w', **profile) as dst:
        dst.write(pctcover, 1)