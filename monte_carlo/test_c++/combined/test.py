import sss_cpp
a = sss_cpp.Box()
a.box_dims = [3,3,3]
a.coordinates = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]

print(a.coord_wrap())
print(a.minimum_image_dist(1))
