from heatdiffusion import System
from render import render

print("Solving heat conduction equation...")
system = System(grid=(100, 100), size=(1, 1), temperature=300, conductivity=80)
system.donut(center=(0.5, 0.5), radius_outer=0.2, radius_inner=0.1, temperature=700)
system_0 = system.save()
system.diffuses(time=0.05, steps=50)
system_1 = system.save()
system.diffuses(time=0.1, steps=100)
render(systems=[system_0, system_1, system],
       show_conductivity=False)