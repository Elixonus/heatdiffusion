try:
    from heatdiffusion import System
    from render import render

    print("Solving heat conduction equation...")
    system = System(grid=(100, 100), size=(1, 1), temperature=300, conductivity=80)
    system.ring(center=(0.3, 0.5), radius_center=0.2, thickness=0.02, temperature=800)
    system.ring(center=(0.5, 0.5), radius_center=0.2, thickness=0.02, temperature=800)
    system.ring(center=(0.7, 0.5), radius_center=0.2, thickness=0.02, temperature=800)
    system_0 = system.save()
    system.diffuses(time=0.03, steps=50)
    system_1 = system.save()
    system.diffuses(time=0.03, steps=50)
    system_2 = system.save()
    system.diffuses(time=0.1, steps=100)
    render(systems=[system_0, system_1, system_2, system], show_conductivity=False)
except KeyboardInterrupt:
    exit()
