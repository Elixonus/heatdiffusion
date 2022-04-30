from math import hypot
import matplotlib.pyplot as plt
from heatdiff import System, Element

system = System(grid=(100, 100), size=(1, 1), temperature=300, conductivity=80)

for gx in range(system.grid[0]):
    for gy in range(system.grid[1]):
        element = system.elements[gx][gy]
        rx = gx / (system.grid[0] - 1)
        ry = gy / (system.grid[1] - 1)
        r = hypot(rx - 0.5, ry - 0.5)
        if 0.1 < r < 0.2:
            element.temperature = 500
for gx in range(system.grid[0]):
    for gy in range(system.grid[1]):
        element = system.elements[gx][gy]
        rx = gx / (system.grid[0] - 1)
        ry = gy / (system.grid[1] - 1)
        if 0.2 < rx < 0.3 and 0.3 < ry < 0.4:
            element.temperature = 700

for i in range(100):
    system.diffuse(delta_time=0.001)



temperatures = [[system.elements[x][y].temperature for y in range(system.grid[1])] for x in range(system.grid[0])]
fig, ax = plt.subplots()
ax.imshow(temperatures, origin="lower")
plt.show()