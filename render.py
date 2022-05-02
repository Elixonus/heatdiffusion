import matplotlib.pyplot as plt
from heatdiff import System


def render(*, systems: list[System], show_conductivity: bool) -> None:
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

    if show_conductivity:
        for t, conductivity in reversed(list(enumerate(conductivities))):
            system = systems[t]
            fig, ax = plt.subplots()
            im = ax.imshow(conductivity, origin="lower", extent=(0, system.size[0], 0, system.size[1]), interpolation="bicubic")
            ax.set_title(f"Map of conductivity coefficients at time t={system.time:.4f} sec")
            ax.set_xlabel("Horizontal displacement (meters)")
            ax.set_ylabel("Vertical displacement (meters)")
            cbar = plt.colorbar(im)
            cbar.set_label("Conductivity coefficient")
    for t, temperature in reversed(list(enumerate(temperatures))):
        system = systems[t]
        fig, ax = plt.subplots()
        im = ax.imshow(temperature, origin="lower", extent=(0, system.size[0], 0, system.size[1]), cmap="inferno", interpolation="bicubic")
        ax.set_title(f"Map of temperatures at time t={system.time:.4f} sec")
        ax.set_xlabel("Horizontal displacement (meters)")
        ax.set_ylabel("Vertical displacement (meters)")
        cbar = plt.colorbar(im)
        cbar.set_label("Temperature (Kelvin)")
    plt.show()
