from osgeo import gdal
from pathlib import Path
from Raster import Raster
from Buffer import Buffer
from Area import Area
import os

# PARAMETERS

# Aeronet coordinates
center = (1085503.9991, 880144.4452)

# Radius (meters)
radius = 5000

# Input directory
input_dir = Path("AEROSOL_3K_TIF")

# Influence area polygon
area_path = "area\\area.shp"

# Output file
output_filename = "output.txt"

# MAIN

# Create worspace directory (if doesnt exist)
workspace = "tmp"
if not os.path.exists(workspace):
    print("Creating directory", workspace)
    os.makedirs(workspace)

# read influence area
area = Area(area_path)

# read files from directory
files = [file for file in input_dir.rglob('*.tif')]    
    
for file in files:

    # reproject file    
    input_raster = gdal.Open(str(file))    
    output_raster = os.path.join(workspace, file.name)
    warp = gdal.Warp(output_raster, input_raster, dstSRS='EPSG:3115')
    warp = None # Closes the file
    
    # Get raster
    raster = Raster(output_raster)
    
    # Get buffer
    buffer = Buffer(center, radius)
    
    # Get AOD values
    aod_str = buffer.get_inner_values(raster, area).strip()
    
    # Write values
    output_str = file.name + " " + aod_str + "\n"
    output_file = open(output_filename, "a")    
    output_file.write(output_str)
    output_file.close()
