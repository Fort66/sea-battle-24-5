from ursina import Entity, color, Vec3
from ursina.shaders import lit_with_shadows_shader

class SeaPlane(Entity):
    def __init__(self):
        super().__init__(
            model='plane',
            texture='white_cube',
            scale=10,
            color=color.blue,
            rotation=Vec3(0, 0, 0),
            position=Vec3(0, 0, 0),
            collider="box",
            shader=lit_with_shadows_shader
            )