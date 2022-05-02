from heatdiff import System
from render import render

system = System(grid=(50, 50), size=(1, 1), temperature=300, conductivity=80)
system.donut(center=(0.5, 0.5), radius_outer=0.2, radius_inner=0.1, temperature=1000)
system.rectangle(center=(0.3, 0.3), size=(0.1, 0.1), temperature=700, conductivity=None)
# system.donut(center=(0.3, 0.3), radius_outer=0.3, radius_inner=0.1, temperature=700, conductivity=80)
system_start = system.save()


system.diffusions(steps=50, delta_time=0.01)


render(systems=[system_start, system],
       show_conductivity=False)