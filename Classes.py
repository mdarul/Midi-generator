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
        print(self.date, self.description, self.persont_list)


def rand_notes(hubble_const, historical_dates):
    degrees = []
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
    with open("zen.txt", 'r') as f:
        lines = f.readlines()
        lines_amount = len(lines)

    var_list = []
    for x in range(0, 4):
        var1 = choice(hubble_const)
        var2 = choice(historical_dates)
        var1 %= lines_amount
        var2 %= len(lines[var1])
        var_list.append(ord(lines[var1][var2]))
    return sum(var_list) % 128
