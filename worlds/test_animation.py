from lib import World
from src.camera_controller import CameraController
from src.tests.animable_object import AnimableObject

def load(world: World):
    world.add(
        CameraController(),
        AnimableObject(),
    )