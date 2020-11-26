import random


class MelodyPattern:
    def __init__(self, timesign, duration):
        self.timesign = timesign
        self.duration = duration
        self.notes = []
        self.stronginterval = random.choice((1, 2, 3))
        self.strongnote = random.randint(0, self.timesign - 1)

        for i in range(self.timesign):
            if not i == self.strongnote:
                self.notes += [0]

            else:
                self.notes += [self.stronginterval]


class Melody (MelodyPattern):
    def check(self, place, note):
        pass

    def relaxation(self):
        pass


class Bit (MelodyPattern):
    def relaxation(self):
        pass


def updating(mel, bit):
    mel.relaxation()
    bit.relaxation()
    return mel.notes, bit.notes