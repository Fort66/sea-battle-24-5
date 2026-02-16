from ursina import Vec3, color, Text

from string import ascii_letters

from .class_SeaPlane import SeaPlane
from .class_GridOverlay import GridOverlay
from .class_CoordinateText import CoordinateText


sea_plane = SeaPlane()
grid_overlay = GridOverlay(10, 10, color=color.black, position=Vec3(0, .002, 0))
lower_grid = GridOverlay(12, 12, color=color.rgba(0, 0, 0, 0.1), position=Vec3(0, -.002, 0))

letters_list = [ascii_letters[i] for i in range(10)]
digits_list = [str(i) for i in range(1, 11)]


for i in range(1, 11):

    CoordinateText(
        model=Text(
            text=letters_list[i - 1]
        ),
        scale=20,
        rotation=Vec3(90, 0, 0)
    ).position = lower_grid.map_position_cells[(i, 11)]

    CoordinateText(
        model=Text(
            text=letters_list[i - 1]
        ),
        scale=20,
        rotation=Vec3(90, 0, 0)
    ).position = lower_grid.map_position_cells[(i, 0)]

    CoordinateText(
        model=Text(
            text=digits_list[i - 1]
        ),
        scale=20,
        rotation=Vec3(90, 0, 0)
    ). position = lower_grid.map_position_cells[(0, i)]

    CoordinateText(
        model=Text(
            text=digits_list[i - 1]
        ),
        scale=20,
        rotation=Vec3(90, 0, 0)
    ). position = lower_grid.map_position_cells[(11, i)]