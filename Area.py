from osgeo import ogr
import pdb

class Area:

    def __init__(self, filename):    
        self.filename = str(filename)        
        self.shapefile = ogr.Open(self.filename)        
        
    def contains(self, x, y):

        point = ogr.Geometry(ogr.wkbPoint)
        point.AddPoint(x, y)

        # Loop all over the polygons
        layer = self.shapefile.GetLayer(0)
        for feature in layer:
            polygon = feature.GetGeometryRef()
            if polygon.Contains(point):
                return True
        return False
    