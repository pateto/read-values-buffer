import numpy as np

class Buffer:

    def __init__(self, center, radius):        
        self.radius = radius
        self.center_x = center[0]
        self.center_y = center[1]
        

    def distance(self, x0, y0, x1, y1):
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
    def get_inner_values(self, raster):
    
        output_str = ""
        
        for i in range(0, raster.arr.shape[1]): # get rows of the array
            for j in range(0, raster.arr.shape[0]): # get columns of the array
            
                # Get x, y point (in the middle of the cell)
                x = raster.x_origin + i * raster.pixel_size_x + raster.pixel_size_x/2
                y = raster.y_origin + j * raster.pixel_size_y + raster.pixel_size_y/2
                
                # Is the point inside the rectangle? (surrounding the circle)
                if abs(x - self.center_x) < self.radius and abs(y - self.center_y) < self.radius:
                
                    # is the point inside the circle?
                    if self.distance(self.center_x, self.center_y, x, y) < self.radius:
                        if raster.arr[j, i] != -9999:
                            #print(i,j, x, y, raster.arr[j, i])
                            output_str += " " + str(raster.arr[j, i])
        
        return output_str