from random import randint, choice


class Note:

    def __init__(self, hubble_const, historical_dates):
        self.track = 0
        self.channel = 0
        self.time = 0
        self.duration = 2
        self.tempo = 90
        self.volume = randint(35, 127)
        self.degrees = rand_notes(hubble_const, historical_dates)

    def print(self):
        print(self.track, self.channel, self.time, self.duration, self.tempo, self.volume, self.degrees)


class History:
    def __init__(self, date, description, person_list):
        self.date = date
        self. description = description
        self.persont_list = person_list

    def print(self):
        print(self.date, "; ", self.description, "; ", self.persont_list)


def rand_notes(hubble_const, historical_dates):
    degrees = []
    # we'll rand the first node in a serie, following ones' tunes will be between 0.7x and 1.3x, where x stands for previous tune
    x = rand_begin_note(hubble_const, historical_dates)
    for i in range(0, 10):
        if randint(0, 1):
            x = randint(x, int(1.3*float(x)))
            if x > 127:
                x = 127
        else:
            x = randint(int(0.7 * float(x)), x)
            if x < 0:
                x = 0
        degrees.append(x)
    return degrees


def rand_begin_note(hubble_const, historical_dates):
    # firstly, we count up lines of "Zen of Python"
    with open("zen.txt", 'r') as f:
        lines = f.readlines()
        lines_amount = len(lines)

    var_list = []
    # then we create 4 variables
    for x in range(0, 4):
        # we choose one number from hubble_const and one from the dates
        var1 = choice(hubble_const)
        var2 = choice(historical_dates)
        # var1 will tell as the line number
        var1 %= lines_amount
        # var2 will be an offset
        var2 %= len(lines[var1])
        # thanks to var1 and var2 we get a sign. Than we convert it to int and append
        var_list.append(ord(lines[var1][var2]))
    # we sum all the values and make modulo 128, because midi tunes range is (0, 127)
    return sum(var_list) % 128
