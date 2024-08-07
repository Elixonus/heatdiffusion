try:
    import matplotlib.pyplot as plt
    from heatdiffusion import System

    def render(*, systems: list[System], show_conductivity: bool) -> None:
        if not show_conductivity:
            print("Plotting temperature maps...")
        else:
            print("Plotting temperature and conductivity maps...")
        temperatures = []
        for system in systems:
            temperature = [
                [system.elements[x][y].temperature for x in range(system.grid[0])]
                for y in range(system.grid[1])
            ]
            temperatures.append(temperature)
        temperatures_sort = sorted(
            temperature
            for temperatures_buffer in temperatures[0]
            for temperature in temperatures_buffer
        )
        temperature_low = temperatures_sort[round(0.01 * (len(temperatures_sort) - 1))]
        temperature_high = temperatures_sort[round(0.99 * (len(temperatures_sort) - 1))]

        if show_conductivity:
            system = systems[0]
            conductivity = [
                [system.elements[x][y].conductivity for x in range(system.grid[0])]
                for y in range(system.grid[1])
            ]
            fig, ax = plt.subplots()
            im = ax.imshow(
                conductivity,
                origin="lower",
                extent=(0, system.size[0], 0, system.size[1]),
                cmap="gray_r",
            )
            ax.set_title(f"Map of conductivity coefficients")
            ax.set_xlabel("Horizontal displacement (meters)")
            ax.set_ylabel("Vertical displacement (meters)")
            cbar = plt.colorbar(im)
            cbar.set_label("Conductivity coefficient")

        for t, temperature in reversed(list(enumerate(temperatures))):
            system = systems[t]
            fig, ax = plt.subplots()
            im = ax.imshow(
                temperature,
                origin="lower",
                extent=(0, system.size[0], 0, system.size[1]),
                vmin=temperature_low,
                vmax=temperature_high,
                cmap="inferno",
                interpolation="bicubic",
            )
            ax.set_title(f"Map of temperatures at time t={system.time:.4f} sec")
            ax.set_xlabel("Horizontal displacement (meters)")
            ax.set_ylabel("Vertical displacement (meters)")
            cbar = plt.colorbar(im)
            cbar.set_label("Temperature (Kelvin)")
        print("Done displaying results...")
        plt.show()


    if __name__ == "__main__":
        from time import sleep

        print("Sorry, this is a rendering utility file that does not work on its own.")
        sleep(5)
except KeyboardInterrupt:
    exit()
