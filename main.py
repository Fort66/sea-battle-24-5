from ursina import *

from icecream import ic

from classes.create_objects import grid_overlay, sea_plane




if __name__ == "__main__":
    window.vsync = False

    app = Ursina()



    AmbientLight(color=color.white)

    EditorCamera()
    camera.position = Vec3(0, 15, 0)
    camera.rotation = Vec3(35, 0, 0)
    camera.fov=60


    app.run()