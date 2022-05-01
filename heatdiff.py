from __future__ import annotations
from math import hypot


class System:
    elements: list[list[Element]]
    grid: tuple[int, int]
    size: tuple[float, float]

    def __init__(self, grid: tuple[int, int], size: tuple[float, float], temperature: float,
                 conductivity: float) -> None:
        self.elements = [[Element(temperature, conductivity) for gy in range(grid[1])] for gx in range(grid[0])]
        self.grid = grid
        self.size = size

    def diffuse(self, delta_time: float) -> None:
        diffusions = [[0 for gy in range(self.grid[1])] for gx in range(self.grid[0])]
        for gx in range(self.grid[0]):
            for gy in range(self.grid[1]):
                element = self.elements[gx][gy]
                if gx > 0:
                    diffusion = element.get_diffusion(
                        self.elements[gx - 1][gy],
                        area=self.size[1] / self.grid[1],
                        distance=self.size[0] / self.grid[0],
                        delta_time=delta_time
                    )
                    diffusions[gx][gy] += diffusion
                    diffusions[gx - 1][gy] -= diffusion
                if gx < self.grid[0] - 1:
                    diffusion = element.get_diffusion(
                        self.elements[gx + 1][gy],
                        area=self.size[1] / self.grid[1],
                        distance=self.size[0] / self.grid[0],
                        delta_time=delta_time
                    )
                    diffusions[gx][gy] += diffusion
                    diffusions[gx + 1][gy] -= diffusion
                if gy > 0:
                    diffusion = element.get_diffusion(
                        self.elements[gx][gy - 1],
                        area=self.size[0] / self.grid[0],
                        distance=self.size[1] / self.grid[1],
                        delta_time=delta_time
                    )
                    diffusions[gx][gy] += diffusion
                    diffusions[gx][gy - 1] -= diffusion
                if gy < self.grid[1] - 1:
                    diffusion = element.get_diffusion(
                        self.elements[gx][gy + 1],
                        area=self.size[0] / self.grid[0],
                        distance=self.size[1] / self.grid[1],
                        delta_time=delta_time
                    )
                    diffusions[gx][gy] += diffusion
                    diffusions[gx][gy + 1] -= diffusion
        for gx in range(self.grid[0]):
            for gy in range(self.grid[1]):
                self.elements[gx][gy].temperature += diffusions[gx][gy]

    def square(self, center: tuple[float, float], size: float, temperature: float = None, conductivity: float = None) -> None:
        self.rectangle(center, (size, size), temperature, conductivity)

    def rectangle(self, center: tuple[float, float], size: tuple[float, float], temperature: float = None, conductivity: float = None) -> None:
        left = center[0] - size[0] / 2
        right = center[0] + size[0] / 2
        down = center[1] - size[1] / 2
        up = center[1] + size[1] / 2
        for gx in range(self.grid[0]):
            for gy in range(self.grid[1]):
                x = self.size[0] * (gx / (self.grid[0] - 1))
                y = self.size[1] * (gy / (self.grid[1] - 1))
                if left < x < right and down < y < up:
                    element = self.elements[gx][gy]
                    if temperature is not None:
                        element.temperature = temperature
                    if conductivity is not None:
                        element.conductivity = conductivity

    def circle(self, center: tuple[float, float], radius: float, temperature: float = None, conductivity: float = None) -> None:
        self.donut(center, radius, 0, temperature, conductivity)

    def donut(self, center: tuple[float, float], radius_outer: float, radius_inner: float, temperature: float = None, conductivity: float = None) -> None:
        for gx in range(self.grid[0]):
            for gy in range(self.grid[1]):
                x = self.size[0] * (gx / (self.grid[0] - 1))
                y = self.size[1] * (gy / (self.grid[1] - 1))
                radius = hypot(x - center[0], y - center[1])
                if radius_inner < radius < radius_outer:
                    element = self.elements[gx][gy]
                    if temperature is not None:
                        element.temperature = temperature
                    if conductivity is not None:
                        element.conductivity = conductivity


class Element:
    temperature: float
    conductivity: float

    def __init__(self, temperature: float, conductivity: float) -> None:
        self.temperature = temperature
        self.conductivity = conductivity

    def get_diffusion(self, element: Element, area: float, distance: float, delta_time: float) -> float:
        temperature_difference = element.temperature - self.temperature
        conductivity = (self.conductivity + element.conductivity) / 2
        rate = (conductivity * area * temperature_difference) / distance
        return rate * delta_time