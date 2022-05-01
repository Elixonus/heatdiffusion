import matplotlib.pyplot as plt
from heatdiff import System


def render(system_start: System, system_end: System) -> None:
    temperatures_start = [[system_start.elements[x][y].temperature
                           for y in range(system_start.grid[1])]
                          for x in range(system_start.grid[0])]
    temperatures_end = [[system_end.elements[x][y].temperature
                         for y in range(system_end.grid[1])]
                        for x in range(system_end.grid[0])]
    fig, ax = plt.subplots()
    im = ax.imshow(temperatures_end, origin="lower")
    ax.set_title("Map of ending temperatures")
    ax.set_xlabel("Horizontal displacement (meters)")
    ax.set_ylabel("Vertical displacement (meters)")
    cbar = plt.colorbar(im)
    cbar.set_label("Temperature (Kelvin)")
    fig, ax = plt.subplots()
    im = ax.imshow(temperatures_start, origin="lower")
    ax.set_title("Map of starting temperatures")
    ax.set_xlabel("Horizontal displacement (meters)")
    ax.set_ylabel("Vertical displacement (meters)")
    cbar = plt.colorbar(im)
    cbar.set_label("Temperature (Kelvin)")
    plt.show()
