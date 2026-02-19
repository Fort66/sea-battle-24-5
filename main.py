from ursina import *

from icecream import ic

from classes.create_objects import my_water_area, enemy_water_area, nav_button

# ic(grid_overlay.map_position_cells)


if __name__ == "__main__":
    window.vsync = False

    app = Ursina()



    AmbientLight(color=color.white)

    # EditorCamera()
    # camera.position = Vec3(0, 15, 0)
    # camera.rotation = Vec3(35, 0, 0)
    # camera.fov=60

    camera.position = Vec3(0, 15, -22)
    camera.rotation = Vec3(35, 0, 0)

    def update():
        if nav_button.change_position:
            if camera.position.x > enemy_water_area.position.x:
                camera.position -= Vec3(20, 0, 0) * time.dt
        else:
            if camera.position.x < my_water_area.position.x:
                camera.position += Vec3(20, 0, 0) * time.dt

    app.run()