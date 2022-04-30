from __future__ import annotations


class System:
    elements: list[list[Element]]
    grid: tuple[int, int]
    size: tuple[float, float]

    def __init__(self, grid: tuple[int, int], size: tuple[float, float], temperature: float, conductivity: float) -> None:
        self.elements = [[Element(temperature, conductivity) for y in range(grid[0])] for x in range(grid[1])]
        self.grid = grid
        self.size = size

    def diffuse(self, delta_time: float) -> None:
        for x in range(self.grid[0]):
            for y in range(self.grid[1]):
                element = self.elements[x][y]
                if x > 0:
                    element.diffuse(self.elements[x - 1][y],
                                    area=self.size[1] / self.grid[1],
                                    distance=self.size[0] / self.grid[0],
                                    delta_time=delta_time)
                if x < self.grid[0] - 1:
                    element.diffuse(self.elements[x + 1][y],
                                    area=self.size[1] / self.grid[1],
                                    distance=self.size[0] / self.grid[0],
                                    delta_time=delta_time)
                if y > 0:
                    element.diffuse(self.elements[x][y - 1],
                                    area=self.size[0] / self.grid[0],
                                    distance=self.size[1] / self.grid[1],
                                    delta_time=delta_time)
                if y < self.grid[1] - 1:
                    element.diffuse(self.elements[x][y + 1],
                                    area=self.size[0] / self.grid[0],
                                    distance=self.size[1] / self.grid[1],
                                    delta_time=delta_time)


class Element:
    temperature: float
    conductivity: float

    def __init__(self, temperature: float, conductivity: float) -> None:
        self.temperature = temperature
        self.conductivity = conductivity

    def diffuse(self, element: Element, area: float, distance: float, delta_time: float) -> None:
        conductivity = (self.conductivity + element.conductivity) / 2
        temperature_difference = element.temperature - self.temperature
        rate = (conductivity * area * temperature_difference) / distance
        self.temperature += rate * delta_time