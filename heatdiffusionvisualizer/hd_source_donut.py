try:
    from heatdiffusion import System
    from render import render
    def apply_boundary(time: float) -> None:
        system.donut(center=(0.5, 0.5), radius_outer=0.2, radius_inner=0.1, temperature=700)

    print("Solving heat conduction equation...")
    system = System(grid=(100, 100), size=(1, 1), temperature=300, conductivity=80)
    apply_boundary(0)
    system_0 = system.save()
    system.diffuses(time=0.05, steps=50, do_every_step=apply_boundary)
    system_1 = system.save()
    system.diffuses(time=0.1, steps=100, do_every_step=apply_boundary)
    render(systems=[system_0, system_1, system], show_conductivity=False)
except KeyboardInterrupt:
    exit()
