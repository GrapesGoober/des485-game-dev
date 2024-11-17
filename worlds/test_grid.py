from lib import World
from src.camera_controller import CameraController
from src.tests.movable_box import MovableBox
from src.tests.static_box import StaticBox

def load(world: World):
    world.add(
        CameraController(),
        MovableBox((2, 2)),
        StaticBox((2, 3)),
    )