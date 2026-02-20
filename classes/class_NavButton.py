from ursina import Button, color

class NavButton(Button):
    def __init__(
        self,
        text='Click',
        position=(0, .4, 0),
        scale=.1,
        color=color.blue,
        **kwargs
    ):

        super().__init__(
            text=text,
            position=position,
            scale=scale,
            color=color,
            **kwargs
        )

        self.change_position = False
        self.on_click = self.change_value

    def change_value(self):
        self.change_position = not self.change_position