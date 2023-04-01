from heatdiffusion import System
from render import render
from time import sleep

print(
    "This script will simulate the heat transfer of two bars connected by a bridge of higher conductivity."
)
sleep(3)
print("Solving heat conduction equation...")
system = System(grid=(100, 100), size=(1, 1), temperature=300, conductivity=80)
system.rectangle(center=(0.5, 0.3), size=(0.3, 0.1), temperature=1000)
system.rectangle(center=(0.5, 0.7), size=(0.4, 0.1), temperature=700)
system.rectangle(center=(0.5, 0.5), size=(0.1, 0.3), conductivity=300)
system_0 = system.save()
system.diffuses(time=0.03, steps=200)
system_1 = system.save()
system.diffuses(time=0.03, steps=200)
system_2 = system.save()
system.diffuses(time=0.2, steps=800)
render(systems=[system_0, system_1, system_2, system], show_conductivity=True)
