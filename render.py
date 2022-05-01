import matplotlib.pyplot as plt
from heatdiff import System


def render(*, system_start: System, system_end: System, show_temperature_start: bool, show_conductivity_start: bool) -> None:
    temperature_start = [[system_start.elements[x][y].temperature
                          for y in range(system_start.grid[1])]
                         for x in range(system_start.grid[0])]
    conductivity_start = [[system_start.elements[x][y].conductivity
                           for y in range(system_start.grid[1])]
                          for x in range(system_start.grid[0])]
    temperature_end = [[system_end.elements[x][y].temperature
                        for y in range(system_end.grid[1])]
                       for x in range(system_end.grid[0])]
    conductivity_end = [[system_start.elements[x][y].conductivity
                         for y in range(system_start.grid[1])]
                        for x in range(system_start.grid[0])]

    if not show_conductivity_start:
        fig, ax = plt.subplots()
        im = ax.imshow(conductivity_start, origin="lower")
        ax.set_title("Map of conductivity coefficients")
        ax.set_xlabel("Horizontal displacement (meters)")
        ax.set_ylabel("Vertical displacement (meters)")
        cbar = plt.colorbar(im)
        cbar.set_label("Conductivity coefficient")
    else:
        fig, ax = plt.subplots()
        im = ax.imshow(conductivity_end, origin="lower")
        ax.set_title("Map of ending conductivity coefficients")
        ax.set_xlabel("Horizontal displacement (meters)")
        ax.set_ylabel("Vertical displacement (meters)")
        cbar = plt.colorbar(im)
        cbar.set_label("Conductivity coefficient")

        fig, ax = plt.subplots()
        im = ax.imshow(conductivity_start, origin="lower")
        ax.set_title("Map of starting conductivity coefficients")
        ax.set_xlabel("Horizontal displacement (meters)")
        ax.set_ylabel("Vertical displacement (meters)")
        cbar = plt.colorbar(im)
        cbar.set_label("Conductivity coefficient")

    if not show_temperature_start:
        fig, ax = plt.subplots()
        im = ax.imshow(temperature_end, origin="lower")
        ax.set_title("Map of temperatures")
        ax.set_xlabel("Horizontal displacement (meters)")
        ax.set_ylabel("Vertical displacement (meters)")
        cbar = plt.colorbar(im)
        cbar.set_label("Temperature (Kelvin)")
    else:
        fig, ax = plt.subplots()
        im = ax.imshow(temperature_end, origin="lower")
        ax.set_title("Map of ending temperatures")
        ax.set_xlabel("Horizontal displacement (meters)")
        ax.set_ylabel("Vertical displacement (meters)")
        cbar = plt.colorbar(im)
        cbar.set_label("Temperature (Kelvin)")

        fig, ax = plt.subplots()
        im = ax.imshow(temperature_start, origin="lower")
        ax.set_title("Map of starting temperatures")
        ax.set_xlabel("Horizontal displacement (meters)")
        ax.set_ylabel("Vertical displacement (meters)")
        cbar = plt.colorbar(im)
        cbar.set_label("Temperature (Kelvin)")

    plt.show()
