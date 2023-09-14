from . import pimodules


pyv = pimodules.pyved_engine
pyv.bootstrap_e()

pygame = pyv.pygame

screen = None
t_last_update = None
world = None
terrain = None

WIDTH = 960
HEIGHT = 720
SCR_SIZE = (WIDTH, HEIGHT)

BLOCKSIZE = 40
BLOCK_SPEED = 100.0
AVATAR_SIZE = 38
AV_SPEED = 330.0
JUMP_POWER = 424.894
JETPACK_RATIO = 0.05
SPEED_CAP = 700.0
SPAWN = -1080, 400
ASSETS_FOLDER = 'cartridge'


gam_assets = dict()


def prepare_game_assets():
    global gam_assets
    gam_assets['bg'] = pygame.transform.scale(pyv.vars.images['background'], (WIDTH, HEIGHT))
    gam_assets['wall'] = pygame.transform.scale(pyv.vars.images['wall_small'], (BLOCKSIZE, BLOCKSIZE))
