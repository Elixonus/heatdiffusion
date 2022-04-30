from __future__ import annotations


class System:
    elements: list[list[Element]]
    width: int
    height: int

    def __init__(self, width: int, height: int, temperature: float, conductivity: float) -> None:
        self.elements = [[Element(temperature, conductivity) for y in range(height)] for x in range(width)]
        self.width = width
        self.height = height

    def diffuse(self, delta_time: float) -> None:
        for x in range(1, self.width - 1):
            for y in range(1, self.height - 1):



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