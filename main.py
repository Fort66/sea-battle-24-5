from ursina import *

from icecream import ic

from string import ascii_letters

from classes.class_SeaPlane import SeaPlane
from classes.class_GridOverlay import GridOverlay
from classes.class_LowerGrid import LowerGrid
from classes.class_SceneText import SceneText


sea_plane = SeaPlane()
grid_overlay = GridOverlay(10, 10)
lower_grid = LowerGrid(11, 11)

letters_list = [ascii_letters[i] for i in range(10)]


letters = [
    SceneText(
        text=symbol,
        position=Vec3(-.75, 0, 0),
        rotation=Vec3(35, 30, 0),
        # origin=Vec3(0.5, 0.5),
        scale=2,
    ) for symbol in letters_list
]


if __name__ == "__main__":
    window.vsync = False

    app = Ursina()



    AmbientLight(color=color.white)

    EditorCamera()
    camera.position = Vec3(0, 15, 0)
    camera.rotation = Vec3(35, 0, 0)
    camera.fov=60


    app.run()