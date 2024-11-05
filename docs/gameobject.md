# Creating `GameObject`
This docs is to explain the concepts and to show a template code for `GameObject`. Any sugestions are very much preferred so put ideas in comments in issue #23.

## Description
A `GameObject` is a building block of a game. It represents a self contained gamestate encapsulation of resources (sprites, sounds, or physics stuff) and logic (input controls and updates). It's a base class, or "interface", to write your own object for a game. They can be added to or removed from a `World`. The `World` will automatically update, render, and simulate physics for us. For more information about its attributes, check docstring.

## Constructor `__init__`
You define your variables in the constructor method `__init__`. The constructor can take arguments, either positional or keyword arguments, which can be passed by the caller or (more importantly) be defined in the world file inside `metadata` field (for more information, check `world.md` under `metadata`).

## Lifecycle Methods
Each and every `GameObject` would follow a lifecycle, managed by `World`. These lifecycles are represented as class methods, where they're called at a certain point in time. You overwrite these methods with your code.

- `on_create` is called once and only once when the `GameObject` is added to world. Here, you add your resources: sprites, physics, handlers, or even other `GameObject` to `World`. 
- `on_remove` is opposite of `on_create`. It is called once (and last) when the object is requested to be removed from `World`. Here, you are asked to clean resources you've added via `on_create`, or any resources accumulated over your object's lifetime.
- `on_update` is called once every frame. Here, you put your game logic: movement, inputs, game states etc. Here, you're given `Frame` dataclass that encapsulates `events` and `dt` for your use.

Note that these methods are optional. If you omit to write code for any of these methods, your `GameObject` simply ignores that functionality.

## Sprite
`lib.Sprite` is a subclass of `pygame.sprite.Sprite`. It provides additional features on top of base class: 
- _**world position**_ using `sprite.x` and `sprite.y`, you can position the sprite one the world coordinates, separate of screen coordinates. It'll automatically update its screen coordinates for you.
- _**rotation**_ using `sprite.angles` you can rotate it around its center 
- _**physics body**_ using `sprite.body` you can have the sprite update its position and rotation from the physics body. 

Adding a sprite to `World` will automatically render it on screen every frame. For more information about its attributes, check docstring.

## Template Code For `GameObject`
In this example, we have a dynamic physics box. The box will turn red when pressed up arrow.
- `__init__` this is constructor method is used to initialize variables. All your variables goes here. 
- `on_create` this method is to add resources to game world: body, shapes, sprites. If you need other resources such as sounds, handlers, or any other objects, initialize them here.
- `on_remove` is removes resources from game world.
- `on_update` runs every frame: checks for input key, and change sprite color.
```
class MyObject(GameObject):

    # Initialize your resources and attributes
    def __init__(self) -> None:
        self.body = pymunk.Body()
        self.shape = pymunk.Poly.create_box(self.body, (50,50))

        self.sprite = Sprite()
        self.sprite.src_image = pygame.Surface((50,50))
        self.sprite.body = self.body

    # Called when creating sprites and physics to game world.
    def on_create(self, world: World) -> None:
        world.sprites.add(self.sprite)
        world.space.add(self.body, self.shape)

    # Called when removing sprites and physics from game world.
    def on_remove(self, world: World) -> None:
        world.sprites.remove(self.sprite)
        world.space.remove(self.body, self.shape)

    # Called every frame; handle states and inputs here.
    def on_update(self, world: World, frame: Frame) -> None:
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_up]: 
            self.sprite.src_image.fill((255, 0, 0))
        else: 
            self.sprite.src_image.fill((255, 255, 255))
```
