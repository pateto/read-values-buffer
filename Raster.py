from osgeo import gdal
import numpy as np

class Raster:

    def __init__(self, filename):
    
        self.filename = str(filename)
        
        # calculate euclidean distance
        raster = gdal.Open(self.filename, gdal.GA_ReadOnly)

        # Raster size
        self.rows = raster.RasterXSize
        self.columns = raster.RasterYSize

        # Get Affine Transformation
        gt = raster.GetGeoTransform()

        self.x_origin = gt[0]
        self.y_origin = gt[3]
        self.pixel_size_x = gt[1]
        self.pixel_size_y = gt[5]
        
        # Get array
        self.arr = np.array(raster.GetRasterBand(1).ReadAsArray())
        
    def __str__(self):        
        print("rows", self.rows)
        print("columns", self.columns)
        print("x_origin", self.x_origin)
        print("y_origin", self.y_origin)
        print("pixel_size_x", self.pixel_size_x)
        print("pixel_size_y", self.pixel_size_y)
        return self.filename