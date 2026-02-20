from ursina import Vec3
from .class_Ships import Ships



class ShipsCreator:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls, *args, **kwargs)
        return cls.__instance

    def __init__(self, water=None):
        self.water = water
        self.create_ship_command = False
        self.deck_count = 0
        self.model = None
        self.texture = None
        self.scale = None
        # self.position = None
        self.rotation = None
        self.ships = []

    def update(self):
        if self.create_ship_command:
            self.ships.append(
                Ships(
                    model=self.model,
                    texture=self.texture,
                    scale=self.scale,
                    position=Vec3(0, 0, 0),
                    rotation=self.rotation,
                    deck_amount=0,
                )
            )

            self.create_ship_command = False
            self.deck_count = 0
            self.model = None
            self.texture = None
            self.scale = None
            self.rotation = None