from pymunk import Body
from lib import Sprite

GRID_SIZE = 100, 100

class GridSprite(Sprite):

    def __init__(self, body: Body = None) -> None:
        super().__init__(body)
        self.offset = 0, 0
    
    @property
    def grid_x(self) -> int: return self.x // GRID_SIZE[0]
    @property
    def grid_y(self) -> int: return self.y // GRID_SIZE[1]

    @grid_x.setter
    def grid_x(self, val: int): self.x = val * GRID_SIZE[0] + self.offset[0]
    @grid_y.setter
    def grid_y(self, val: int): self.y = val * GRID_SIZE[1] + self.offset[1]

    @property
    def grid_position(self) -> tuple[int, int]:
        return self.x, self.y
    @grid_position.setter
    def grid_position(self, val: tuple[int, int]):
        self.grid_x, self.grid_y = val