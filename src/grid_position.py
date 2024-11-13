from lib import GameObject, World

# using this data pool to check/find neighbours
POOL: dict[World, list['GridPosition']] = {}

class GridPosition(GameObject):
    """
        A game object that represents a grid position coordinate. Can be added to world.
        Can be used to for grid collision checking at the world level.

        Attributes:
            `grid_x`, `grid_y`  Grid integer position of the object.
            `grid_position`     Grid tuple integer position of the object.
            `parent_object`     Optional parent GameObject that this GridObject belongs to
        
        Static Method:
            `get_objects`       Get list of all objects in a world.
            `get_objects_at`    Generator to get objects in a world within `manhat_dist` of `grid_position`.
            `is_occupied`       Boolean check whether a `manhat_dist` around `grid_position` is occupied.
    """

    def __init__(self, grid_position: tuple[int, int]) -> None:
        self.grid_x, self.grid_y = grid_position
        self.parent_object: GameObject = None

    @property
    def grid_position(self) -> tuple[int, int]:
        return self.grid_x, self.grid_y
    @grid_position.setter
    def grid_position(self, val: tuple[int, int]):
        self.grid_x, self.grid_y = val

    def on_create(self, world: World) -> None:
        if world not in POOL:
            POOL[world] = []
        POOL[world].append(self)

    def on_remove(self, world: World) -> None:
        if world in POOL:
            POOL[world].remove(self)

    def get_neighbours(self, world, manhat_dist: int = 0):
        for o in GridPosition.get_objects_at(world, (self.grid_x, self.grid_y), manhat_dist):
            if o != self: yield o

    @staticmethod
    def get_objects(world: World) -> list['GridPosition']:
        return POOL[world]

    @staticmethod
    def get_objects_at(world: World, at: tuple[int, int], manhat_dist: int = 0):
        for o in GridPosition.get_objects(world):
            if abs(o.grid_x - at[0]) + abs(o.grid_y - at[1]) <= manhat_dist:
                yield o

    @staticmethod
    def has_objects_at(world: World, at: tuple[int, int], manhat_dist: int = 0) -> bool:
        for _ in GridPosition.get_objects_at(world, at, manhat_dist):
            return True
        return False