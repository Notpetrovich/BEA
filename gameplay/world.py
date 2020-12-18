def intersection_assignment(box1, box2):
    """
    принимает два кортежа с координатами диагонально противоположных углов двух прямоугольных
    областей в порядке слева направо и проверяет их на взаимное пересечение
    :param box1: (x_1_1, y_1_1, x_1_2, y_1_2)
    :param box2: (x_2_1, y_2_1, x_2_2, y_2_2)
    :return: True, если пересекаются, и False иначе
    """
    len1_x = box1[2] - box1[0]
    len1_y = box1[3] - box1[1]

    len2_x = box2[2] - box2[0]
    len2_y = box2[3] - box2[1]

    first_check = abs(box1[0] - box2[0])
    second_check = abs(box1[1] - box2[1])
    if first_check < len1_x or first_check < len2_x:
        if second_check < len1_y or second_check < len2_y:
            return True

    return False


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
            for param_number in range(len(params)):    # check for moving request:
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
# check for attack:
                elif self.active_things_uniorder[param_number] == "attack":
                    x = coords[0]
                    y = coords[1]
                    for another_thing in self.active_things:
                        another_hitbox = another_thing.hitbox
                        another_x = another_thing.coords[0]
                        another_y = another_thing.coords[1]
                        hit = self.hitbox_check(
                            x, y,
                            another_x, another_y,
                            thing.damage_hitbox, another_hitbox
                        )
                        if hit:
                            if another_thing.health_points > thing.damage:
                                another_thing.health_points -= thing.damage
                            else:
                                if another_thing.tag == "player":
                                    self.death_screen()
                                else:
                                    thing.experience_points += another_thing.exp_plus
# check for interaction:
                elif self.active_things_uniorder[param_number] == "interaction":
                    if self.active_things_uniorder[param_number]:
                        x = coords[0]
                        y = coords[1]
                        for another_thing in self.passive_things:
                            another_hitbox = another_thing.hitbox
                            another_x = another_thing.coords[0]
                            another_y = another_thing.coords[1]
                            interaction = self.hitbox_check(
                                x, y,
                                another_x, another_y,
                                hitbox, another_hitbox
                            )
                            if interaction:
                                another_thing.mode += 1
# drawing with changes:
        for thing in self.active_things:
            thing.image_self()

        for thing in self.passive_things:
            thing.image_self()
# end of main part

    def death_screen(self):
        pass

    def hitbox_check(self, x, y, another_x, another_y, hitbox, another_hitbox):
        """
        принимает положения верхних левых вершин двух хитбоксов,
        а также сами хитбоксы, и проверяет их пересечение
        :param x: тут координаты вершины первого
        :param y: тут координаты вершины первого
        :param another_x: тут второго
        :param another_y: тут второго
        :param hitbox: первый хитбокс (здесь и далее форматный ввод)
        :param another_hitbox: второй хитбокс
        :return:
        """
        delta_x = another_x - x
        delta_y = another_y - y
        box1_coords = (
            hitbox[0],
            hitbox[1],
            hitbox[0] + hitbox[2],
            hitbox[1] + hitbox[3]
        )
        box2_coords = (
            another_hitbox[0] + delta_x,
            another_hitbox[1] + delta_y,
            another_hitbox[0] + another_hitbox[2] + delta_x,
            another_hitbox[1] + another_hitbox[3] + delta_y
        )
        return intersection_assignment(box1_coords, box2_coords)
