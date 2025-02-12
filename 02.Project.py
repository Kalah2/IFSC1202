from math import pi, sin, cos, acos

radius = 6371

x1 = 58
y1 = 21
x2 = 41
y2 = 12

location1 = x1 * (pi / 180) 
location_1 = y1 * (pi / 180)
location2 = x2 * (pi / 180)
location_2 = y2 * (pi / 180)


d=radius*acos(sin(location1)*sin(location2)+cos(location1)*cos(location2)*cos(location_1-location_2))

d_rounded = round(d,2)


print("starting point",location1 )
print("starting point",location_1 )
print("starting point",location2 )
print("starting point",location_2 )
print("The Great Circle Distance is: ",d_rounded )


