import random
from winsound import *
import sys


# dict with samples' addresses
samples = {
    "strumento melodico": {
        "low": "samples\\melodia\\low.wav",
        "high": "samples\\melodia\\high.wav"
    },
    "tamburi": {
        1: "samples\\tamburi\\1.wav"
    }
}

# the main dict of rules according to which notes change
# note that everything may go to hell if some list shell not be sorted
harmony = {
    "basic harmony": {
        "after keys": {
            -4: [-4, -1, 1, 3],
            -3: [-1, 1, 3, 4],
            -2: [-1, 1, 3],
            -1: [-2, 1, 2, 3],
            1: [-1, 1, 3, 4],
            2: [1, 3],
            3: [-2, -1, 1, 2],
            4: [-4, 3, 4]
        },
        "before keys": {
            -4: [-3, 1, 4],
            -3: [-1, ],
            -2: [],
            -1: [],
            1: [],
            2: [],
            3: [],
            4: []
        }
    },
    "advanced harmony": {

    },
    "cool endings": {

    },
    "drum hooks": {

    }
}


class MelodyPattern:
    def __init__(self, timesign, duration):
        self.timesign = timesign
        self.duration = duration
        self.notes = []
        stronginterval = random.choice((-1, 1, 3))
        self.strongnote = random.randint(0, self.timesign - 1)

        for i in range(self.timesign):
            if not i == self.strongnote:
                self.notes.append(0)

            else:
                self.notes.append(stronginterval)

        # stages of the melody
        self.stages = {
            0: "starting",
            1: "first variation",
            2: "second variation",
            3: "ending"
        }
        # initial stage is "starting", then it shell define a current stage
        self.stage = self.stages[0]

    def new_stage(self, name_of_stage):
        if type(name_of_stage) == int:
            self.stage = self.stages[name_of_stage]
        else:
            self.stage = name_of_stage


class Melody (MelodyPattern):
    def __init__(self, timesign, duration=0):
        super().__init__(timesign, duration)
        self.background = []
        for i in range(self.timesign**2 - self.timesign):
            self.background.append(0)

    def var(self, notes):
        """
        building a list of notes` variations by changing some one note
        :param notes: list of notes
        :return: notes` variation
        """
        lenght = len(notes)
        variations = [0 for i in range(lenght)]
        if self.stage == "starting":
            if not notes.count(0):
                for i in range(lenght):
                    var1 = []
                    var2 = []
                    if lenght <= 3:
                        notesMatter = [notes[nt] for nt in notes if not nt == i]
                        var1 = harmony["basic harmony"]["after keys"][notesMatter[0]]
                        var2 = harmony["basic harmony"]["before keys"][notesMatter[1]]

                    else:
                        pass

                    var = [var1[nt] for nt in var1 if var2.count(var1[nt])]
                    for j in var:
                        new_variation = []
                        for k in notes:
                            if not k == i:
                                new_variation.append(notes.key)
                            else:
                                new_variation.append(j)

                        variations.append(new_variation)

            else:
                zeroes = [nt for nt in notes if notes[nt] == 0]
                randzero = random.randint(0, len(zeroes) - 1)
                backnote = notes[randzero - 1]
                fornote = notes[randzero + 1]
                var1 = []
                if backnote:
                    if backnote == 1:
                        pass

        elif self.stage == "first variation":
            pass

        elif self.stage == "second variation":
            pass

        elif self.stage == "ending":
            pass

        return variations

    def relaxation(self):
        if self.stage == "starting":
            pass

        elif self.stage == "variation 1":
            pass

        elif self.stage == "variation 2":
            pass

        elif self.stage == "ending":
            pass


class Beat (MelodyPattern):
    def __init__(self, timesign, duration=0):
        super().__init__(timesign, duration)

    def relaxation(self):
        pass


def updating(mel, beat, set_stage=0):
    if not set_stage:
        mel.relaxation()
        beat.relaxation()

    else:
        mel.new_stage(set_stage)
        beat.new_stage(set_stage)

    return mel.notes, beat.notes


# FIXME: winsound may not work adequately; lib for linux even can not be plugged
def play_melody(gamma, volume, duration, agressive="low"):
    pass
