from lib import Frame, GameObject, World
import pygame

class CameraController(GameObject):
    def on_update(self, world: World, frame: Frame) -> None:
        speed = 100 * frame.dt
        keystates = pygame.key.get_pressed()
        if keystates[pygame.K_UP]:      world.camera_position[1] -= speed
        if keystates[pygame.K_DOWN]:    world.camera_position[1] += speed
        if keystates[pygame.K_LEFT]:    world.camera_position[0] -= speed
        if keystates[pygame.K_RIGHT]:   world.camera_position[0] += speed