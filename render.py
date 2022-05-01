import matplotlib.pyplot as plt
from heatdiff import System


def render(*, systems: list[System], times: list[float]) -> None:
    temperatures = []
    for system in systems:
        temperature = [[system.elements[x][y].temperature
                        for y in range(system.grid[1])]
                       for x in range(system.grid[0])]
        temperatures.append(temperature)
    conductivities = []
    for system in systems:
        conductivity = [[system.elements[x][y].conductivity
                         for y in range(system.grid[1])]
                        for x in range(system.grid[0])]
        conductivities.append(conductivity)

    for t, conductivity in reversed(list(enumerate(conductivities))):
        fig, ax = plt.subplots()
        im = ax.imshow(conductivity, origin="lower")
        ax.set_title(f"Map of conductivity coefficients at time t={times[t]:.4f} sec")
        ax.set_xlabel("Horizontal displacement (meters)")
        ax.set_ylabel("Vertical displacement (meters)")
        cbar = plt.colorbar(im)
        cbar.set_label("Conductivity coefficient")
    for t, temperature in reversed(list(enumerate(temperatures))):
        fig, ax = plt.subplots()
        im = ax.imshow(temperature, origin="lower")
        ax.set_title(f"Map of temperatures at time t={times[t]:.4f} sec")
        ax.set_xlabel("Horizontal displacement (meters)")
        ax.set_ylabel("Vertical displacement (meters)")
        cbar = plt.colorbar(im)
        cbar.set_label("Temperature (Kelvin)")
    plt.show()
