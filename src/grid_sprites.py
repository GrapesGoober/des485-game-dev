from lib import Sprite

GRID_SIZE = 100, 100

class GridSprites:

    def __init__(self, grid_position: tuple[int, int], *sprites: Sprite) -> None:
        self.__grid_x, self.__grid_y = grid_position
        self.sprites = sprites

    @property
    def grid_x(self) -> int: return self.__grid_x
    @property
    def grid_y(self) -> int: return self.__grid_y

    @grid_x.setter
    def grid_x(self, val: int): 
        delta = val - self.__grid_x
        for s in self.sprites:
            s.x += delta * GRID_SIZE[0]
    @grid_y.setter
    def grid_y(self, val: int): 
        delta = val - self.__grid_y
        for s in self.sprites:
            s.y += delta * GRID_SIZE[1]

    @property
    def grid_position(self) -> tuple[int, int]:
        return self.grid_x, self.grid_y
    @grid_position.setter
    def grid_position(self, val: tuple[int, int]):
        self.grid_x, self.grid_y = val