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

A rectangle of conducting material of size (x, y) in meters diffuses and temperature fluctuates based on the initial setup.

The rectangle is subdivided into a grid of (m, n) where each sub-rectangle is assumed as isothermal and is interacting with its four neighbors.

Outside the material is void, so the material does not interact with the outside.

Each element of the mesh (m, n) is assigned an initial temperature and conductivity and is simulated in time with a constant step to observe the effects.

Temperature may be modified from outside the system by the user but this will mean the energy of the system changes.

## Gallery

### Cooling Bars

Two bars filled in with the same temperature cool down with time.

![Cooling Bars 1](gallery/cooling_bars/1.png)
![Cooling Bars 2](gallery/cooling_bars/2.png)
![Cooling Bars 3](gallery/cooling_bars/3.png)
![Cooling Bars 4](gallery/cooling_bars/4.png)

### Source Rings

Concentric rings are given a temperature that remains constant as the simulation moves on.

![Source Rings Inside 1](gallery/source_rings_inside/1.png)
![Source Rings Inside 2](gallery/source_rings_inside/2.png)
![Source Rings Inside 3](gallery/source_rings_inside/3.png)
