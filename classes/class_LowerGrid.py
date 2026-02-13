from ursina import Entity, Grid, color, Vec3

class LowerGrid(Entity):
    def __init__(self, width, height, **kwargs):
        super().__init__(
            model=Grid(
                width=width,
                height=height,
                thickness=3
            ),
            scale=width,
            color=color.rgba(0, 0, 0, .1),
            rotation=Vec3(90, 0, 0),
            position=Vec3(-.515, -.002, .515),
            collider='box',
        )

        self.grid_width = width
        self.grid_height = height