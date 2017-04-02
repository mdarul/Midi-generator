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
    historical_list.append(History(1423, "Statut warcki - znaczne zwiększenie możliwości gospodarczych szlachty, prawo do wykupu ziem 'krnąbrnych i nieużytecznych' sołtysów oraz ograniczenie ich praw.", "Władysław II Jagiełło"))
    historical_list.append(History(1573, "Konfederacja warszawska - swoboda wyznania dla szlachty, równouprawnienie innowierców", "sejm konwokacyjny, szlachta"))
    historical_list.append(History(1668, "Sejmowy zakaz porzucania katolicyzmu", "Sejm"))
    historical_list.append(History(1658, "Wygnanie arian z RP", "Jan II Kazimierz Waza"))
    historical_list.append(History(1718, "Wykluczenie posłów protestanckich z grona sejmowego.", "Sejm"))
    historical_list.append(History(1768, "Zniesienie większości ustaw dyskryminujących innowierców", "Stanisław August Poniatowski"))
    historical_list.append(History(1569, "Unia lubelska - unia realna, wspólny monarcha, sejm, waluta, polityka zagraniczna i obronna", "Zygmunt II August"))
    historical_list.append(History(1364, "Założenie Studium Generale, późniejszego Uniwersytetu Jagiellońskiego", "Kazimierz II Wielki"))
    historical_list.append(History(1773, "Powołanie Komisji Edukacji Narodowej", "Stanisław August Poniatowski"))
    historical_list.append(History(1610, "Podbicie moskwy przez wojska polskie podczas wojny polsko-rosyjskiej 1609-1618", "Stanisław Żółkiewski"))
    historical_list.append(History(1918, "Prawa wyborcze dla kobiet", "Józef Piłsudski"))
    historical_list.append(History(1920, "Bunt Żeligowskiego - operacja wojskowa w wyniku której Litwa środkowa wraz z Wilnem została przyłączona do Polski", "Lucjan Żeligowski, Józef Piłsudski"))

    for x in historical_list:
        historical_dates.append(x.date)

    print("Algorithm that generates pitches for midi notes uses two list of variables - observed values of Hubble")
    print("constant from the earliest (2016) to the oldest (1929) and year dates of some historical events of polish")
    print("history. Would you like to print the events? (y/n)")
    tmp = ''
    while tmp != 'y' and tmp != 'n':
        tmp = input()
        if tmp == 'y':
            for object in historical_list:
                object.print()
        elif tmp == 'n':
            break
        else:
            print("Incorrect value, please write it again.")

    print("\nWould you like to add an event? (y/n)")
    tmp = ''
    while tmp != 'y' and tmp != 'n':
        tmp = input()
        if tmp == 'y':
            print("Enter year date:")
            tmp1 = int(input())
            print("Write short description")
            tmp2 = str(input())
            print("Write a person or people that are connected with it")
            tmp3 = str(input())
            historical_list.append(History(tmp1, tmp2, tmp3))
            historical_dates.append(tmp1)
            print("Added event: ")
            historical_list[-1].print()
        elif tmp == 'n':
            break
        else:
            print("Incorrect value, please write it again.")

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
