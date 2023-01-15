# heatdiffusion 🥵

Heat transfer/diffusion simulation with conduction through uniform 2D mesh.

![Fourier's Law](gallery/equation.png)

## Usage

```
pip install -r requirements.txt
```
```
python heatdiffusion/<hd_example>
```
where `<hd_example>` is the remainder file name of the program you want to run.

## Description

A rectangle of conducting material of size (x, y) meters diffuses and temperature fluctuates based on the initial setup and extra conditions.

The system is subdivided into a grid of (m, n) sub-rectangles where each sub-rectangle is approximated as if its temperature is uniform and interacts with its four adjacent neighbors.

Outside the rectangle of material(s) is void, so the system does not lose or gain energy except when a boundary condition is set.

Each element of the mesh (m, n) is assigned an initial temperature, conductivity constant and the simulation is run in time with a constant step integration.

Temperature may be modified from outside the system by the program but this will mean that energy is added or removed from the system.

## Gallery

### Cooling Bars

Two bars given the same uniform temperature cool down with respect to time.

![Cooling Bars 1](gallery/cooling_bars/1.png)
![Cooling Bars 2](gallery/cooling_bars/2.png)
![Cooling Bars 3](gallery/cooling_bars/3.png)
![Cooling Bars 4](gallery/cooling_bars/4.png)

### Source Rings

Concentric rings are given exactly enough energy such that the temperature remains constant with respect to time.

![Source Rings Inside 1](gallery/source_rings_inside/1.png)
![Source Rings Inside 2](gallery/source_rings_inside/2.png)
![Source Rings Inside 3](gallery/source_rings_inside/3.png)
