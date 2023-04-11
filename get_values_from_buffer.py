from osgeo import gdal
import numpy as np

aeronet_x = 1085503.9991
aeronet_y = 880144.4452
    
# calculate euclidean distance
raster = gdal.Open('tif/mod04.tif', gdal.GA_ReadOnly)

# Raster size
rows = raster.RasterXSize
columns = raster.RasterYSize

# Get Affine Transformation
gt =raster.GetGeoTransform()

x_origin = gt[0]
y_origin = gt[3]
pixel_size_x = gt[1]
pixel_size_y = gt[5]

# print values
print("rows", rows)
print("columns", columns)
print("x_origin", x_origin)
print("y_origin", y_origin)
print("pixel_size_x", pixel_size_x)
print("pixel_size_y", pixel_size_y)

# Get array
arr = np.array(raster.GetRasterBand(1).ReadAsArray())

def distance(x0, y0, x1, y1):
    # initializing points in
    # numpy arrays
    point1 = np.array((x0, y0))
    point2 = np.array((x1, y1))

    # calculating Euclidean distance
    # using linalg.norm()
    dist = np.linalg.norm(point1 - point2)
    
    # printing Euclidean distance
    return dist

# Get values inside the buffer
r = 5000
for i in range(0, arr.shape[1]): # get rows of the array
    for j in range(0, arr.shape[0]): # get columns of the array
    
        # Get x, y point (in the middle of the cell)
        x = x_origin + i * pixel_size_x + pixel_size_x/2
        y = y_origin + j * pixel_size_y + pixel_size_y/2
        
        # Is the point inside the rectangle? (surrounding the circle)
        if abs(x - aeronet_x) < r and abs(y - aeronet_y) < r:
        
            # is the point inside the circle?
            if distance(aeronet_x, aeronet_y, x, y) < r:
                if arr[j, i] != -9999:
                    print(i,j, x, y, arr[j, i])