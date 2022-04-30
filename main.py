import matplotlib.pyplot as plt
from heatdiff import System, Element

system = System(grid=(100, 100), size=(1, 1), temperature=300, conductivity=80)

for gx in range(system.grid[0]):
    for gy in range(system.grid[1]):
        element = system.elements[gx][gy]
        if 40 <= gx <= 60 and 40 <= gy <= 60:
            element.temperature = 500

for i in range(10):
    system.diffuse(delta_time=0.001)



temperatures = [[system.elements[x][y].temperature for y in range(system.grid[1])] for x in range(system.grid[0])]
fig, ax = plt.subplots()
ax.imshow(temperatures, origin="lower")
plt.show()