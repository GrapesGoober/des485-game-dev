# Using `World` Object & World File
This docs is to explain and to show a template code for `World`. Any sugestions are very much preferred so put ideas in comments in issue #23.

## Description
A `World` object is a collection of game objects and its resources. It can update its game objects logic, physics simulation, and draw itself onto a surface. Its gameobjects can be defined in a world file `.json` format, which can be loaded during runtime. For more information about its attributes, check docstring. 

## Features
- _**Adding & Removing Resources**_ You can add resources to `World` using these methods: 
    - For sprites, use `world.sprites.add( *sprites )` and `world.sprites.remove( *sprites )`
    - For physics, use `world.space.add( *body|shape|constraints )` and `world.space.remove( *body|shape|constraints )`
    - For game objects, use `world.add( gameobj )` and `world.remove( gameobj )`
    - Define your gameobjects using a world file and load it using `world.load_from_file`
- _**Attributes**_ There are some useful attributes you might want to use: 
    - `global_states` a dictionary to access world-level data as gameobjects using a _**key**_ (see more in _**world file**_).
    - `camera_position` X and Y coordinates of camera. Will offset sprites world coordinates into screen coordinates upon `draw`
    - `background` optional surface to draw as background. You can use this for static or parallax background.
- _**Updating & Drawing**_ A `World` can update and draw is gameobjects and resources. This is normally done in `main.py`, but if you want to use your own world object, you can use these methods: `world.update` using events and dt, and `world.draw` onto surface.

## World File
A world file contains a list of game objects to add to a world. It can be added to a world via `world.load_from_file`. Each game object within this list is defined as a json object with 3 properties
- _**key**_ a nullable unique identifier for the game object. This is to be retrieved by `global_states`. Useful for the player, inventory, or enemy manager. A general rule of thumb is to keep the key as `null` for most objects, and camelcase `ClassName` in case you need it.
- _**location**_ the python module directory to the class that you want to add. This is a python style imports: snake_case for module names, CamelCase for class names, separated by dots. For example: `my_module.enemy_zombie.EnemyZombie`
- _**metadata**_ json-serializable arguments to be passed to the object's constructor. This is always treated as keyword arguments. Note that the object's constructor `__init__` must support these arguments.

Example: a world file containing a bouncy ball and a wall.
```
[
    {
        "key": "Ball",
        "location": "my_module.ball.Ball",
        "metadata": {
            "position": [100, 200],
            "velocity": [300, 400]
        }
    },
    {
        "key": "Wall",
        "location": "my_module.wall.Wall",
        "metadata": {
            "position": [600, 200],
            "size": [10, 400]
        }
    }
]
```