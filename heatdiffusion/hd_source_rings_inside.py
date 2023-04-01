from heatdiffusion import System
from render import render


def apply_boundary(time: float) -> None:
    for n in range(5):
        ratio = n / (5 - 1)
        system.ring(
            center=(0.5, 0.5),
            radius_center=(0.35 * ratio + 0.1),
            thickness=0.02,
            temperature=800,
        )


print("Solving heat conduction equation...")
system = System(grid=(100, 100), size=(1, 1), temperature=300, conductivity=80)
apply_boundary(0)
system_0 = system.save()
system.diffuses(time=0.03, steps=50, do_every_step=apply_boundary)
system_1 = system.save()
system.diffuses(time=0.03, steps=50, do_every_step=apply_boundary)
render(systems=[system_0, system_1, system], show_conductivity=False)
