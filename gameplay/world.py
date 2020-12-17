class World(object):
    def __init__(self, wight_of_screen, height_of_screen):
        self.weight = wight_of_screen
        self.height = height_of_screen
        self.active_things = []
        self.passive_things = []

        self.active_things_uniorder = {
            0: "delta_x",
            1: "delta_y",
            2: "attack",
            3: "interaction"
        }

    def update(self, time):
        for thing in self.active_things:
            hitbox = thing.hitbox   # x_left, y_up, len_x, len_y
            coords = thing.coords
            params = thing.deltas   # universal order expected
            drawing_mode = thing.parameter
            for param_number in range(len(params)):
                if self.active_things_uniorder[param_number] == "delta_x":
                    delta_x = params[param_number]
                    x = coords[0]
                    x_new = x + delta_x
                    x_left_new = x_new + hitbox[0]
                    x_right_new = x_new + hitbox[2]

                    if x_left_new < 0:
                        x_new = 0 - hitbox[0]

                    if x_right_new > self.weight:
                        x_new = self.weight - hitbox[2]

                    thing.coords[0] = x_new
                    thing.deltas[0] = 0

                elif self.active_things_uniorder[param_number] == "delta_y":
                    delta_y = params[param_number]
                    y = coords[1]
                    y_new = y + delta_y
                    y_left_new = y_new + hitbox[1]
                    y_right_new = y_new + hitbox[3]

                    if y_left_new < 0:
                        y_new = 0 - hitbox[1]

                    if y_right_new > self.height:
                        y_new = self.height - hitbox[3]

                    thing.coords[1] = y_new
                    thing.deltas[1] = 0

                elif self.active_things_uniorder[param_number] == "attack":
                    pass

                elif self.active_things_uniorder[param_number] == "interaction":
                    pass

        for thing in self.active_things:
            thing.image_self(drawing_mode, x_new, y_new)

        for thing in self.passive_things:
            thing.image_self()
