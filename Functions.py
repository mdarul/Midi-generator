import argparse
from midiutil import MIDIFile
from os.path import exists
from Classes import Note, History
from random import randint, choice


def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("len", type=int, help="length of the music")
    args = parser.parse_args()
    length = args.len
    return length


def generate_data():

    # all 18 observed values of Hubble constant, from the earliest (2016) to the oldest (1929)
    hubble_const = [72, 68, 73, 68, 68, 69, 70, 71, 70, 72, 70, 78, 72, 50, 55, 75, 180, 500]
    historical_dates = []
    historical_list = []

    historical_list.append(History(1996, "my birth", "Michał Darul"))
    historical_list.append(History(1997, "not my birth", "not Michał Darul"))
    historical_list.append(History(1998, "not my birth1", "not Michał Darul1"))
    historical_list.append(History(1999, "not my birth2", "not Michał Darul2"))
    historical_list.append(History(2000, "not my birth3", "not Michał Darul3"))

    for x in historical_list:
        historical_dates.append(x.date)

    return hubble_const, historical_dates


def generate_notes(length, hubble_const, historical_dates):
    notes = [Note(hubble_const, historical_dates) for i in range(length)]

    time = 0
    for note in notes:
        note.time = time
        time += 10

    return notes


def get_file_name():
    print("Please enter a name of the file and its path. If you want file to be in the same directory,")
    print("do not write path, just a name. It is not necessary to end the name with '.mid'.")
    flag = False
    tmp = ''
    while flag != True:
        if tmp == 'n':
            print("Please enter file name (optionally with path) again:")
        file_name = input()
        if file_name[-4:] == ".mid":
            pass
        else:
            file_name += ".mid"

        if exists(file_name):
            print("File already exist.")
            print("If you want to overwrite it, type 'y'")
            print("If you want to write path once again, type 'n'")
            tmp = ''
            while tmp != 'y' and tmp != 'n':
                tmp = input()
                if tmp == 'y':
                    flag = True
                elif tmp == 'n':
                    break
                else:
                    print("Incorrect value, please write it again.")

        else:
            flag = True
    return file_name


def create_midi(notes, length, file_name):
    MyMIDI = MIDIFile(length)
    for object in notes:
        MyMIDI.addTempo(object.track, object.time, object.tempo)

        for i, pitch in enumerate(object.degrees):
            MyMIDI.addNote(object.track, object.channel, pitch, object.time + i, object.duration, object.volume)

    with open(file_name, "wb") as output_file:
        MyMIDI.writeFile(output_file)
