import os

from . import pimodules
from . import shared
from . import systems
from .World import World
from .classes import Camera


pyv = pimodules.pyved_engine
pyv.bootstrap_e()
pygame = pyv.pygame
ts_prev_frame = None


@pyv.declare_begin
def troid_init(vms=None):
    pyv.init()

    screen = pygame.display.set_mode(shared.SCR_SIZE)
    shared.screen = screen
    pyv.define_archetype('player', (
        'speed', 'accel_y', 'gravity', 'lower_block', 'jetpack', 'body', 'camera', 'controls'
    ))
    pyv.define_archetype('block', ['body', ])
    pyv.define_archetype('mob_block', ['body', 'speed', 'bounds', 'horz_flag', ])

    world = World(2128.0, 1255.0)
    world.load_map(os.path.join(shared.ASSETS_FOLDER, 'my_map.csv'))
    shared.world = world
    world.add_game_obj(
        {'key': 'origin'}
    )
    camera = Camera([-280, -280], world)

    world.create_avatar(camera)
    pyv.bulk_add_systems(systems)


@pyv.declare_update
def troid_update(timeinfo):
    global ts_prev_frame
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            shared.terrain.game_over = True

    pyv.systems_proc()
    pyv.flip()


@pyv.declare_end
def troid_exit(vms=None):
    pyv.quit()


pyv.run_game()
