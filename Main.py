from Functions import parser, get_file_name, generate_data, generate_notes, create_midi

length = parser()
file_name = get_file_name()
print("Entered file name - ", file_name)

hubble_const, historical_dates = generate_data()

notes = generate_notes(length, hubble_const, historical_dates)
create_midi(notes, length, file_name)
