try:
    from heatdiffusion import System
    from render import render

    print("Solving heat conduction equation...")
    system = System(grid=(100, 100), size=(1, 1), temperature=300, conductivity=80)
    system.circle(center=(0.5, 0.5), radius=0.2, temperature=700)
    system_0 = system.save()
    system.diffuses(time=0.1, steps=100)
    render(systems=[system_0, system], show_conductivity=False)
except KeyboardInterrupt:
    exit()
