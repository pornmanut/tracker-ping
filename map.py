import os
import sys
from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt


args = sys.argv
if len(args) <= 1:
    print("need more arugment")
    sys.exit()
target = args[1]

location = []
if os.path.exists(target):
    with open(target) as fo:
        print("reading from "+fo.name)
        for line in fo:
            line = line.strip().split()
            # brutforce
            line[0] = float(line[0])
            line[1] = float(line[1])
            location.append(line)

fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
# m = Basemap(llcrnrlon=100., llcrnrlat=13.75,
#             urcrnrlon=145., urcrnrlat=-37.98,
#             rsphere=(6378137.00, 6356752.3142),
#             resolution='l', projection='merc',
#             lat_ts=20.)
m = Basemap(resolution='l', projection='mill', lat_ts=20.)

prev_lat = location[0][0]
prev_lon = location[0][1]

for lat, lon in location[1:]:
    m.drawgreatcircle(prev_lon, prev_lat, lon, lat, linewidth=2, color='b')
    prev_lat = lat
    prev_lon = lon

m.drawcoastlines()
m.fillcontinents(color='coral', lake_color='aqua')
# draw parallels and meridians.
m.drawparallels(np.arange(-90, 90, 20), labels=[1, 1, 0, 1])
# draw meridians
m.drawmeridians(np.arange(-180, 180, 30), labels=[1, 1, 0, 1])
m.drawmapboundary(fill_color='aqua')

section = target.split('/')
path = section[0]+'/'+section[1]+'/map.png'
print('saving fig to '+path)
plt.savefig(path)
