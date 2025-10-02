def interface():
    print('Greetings, my Lord! We praise you.')
    while True:
        print('''What do you want us to do?
                 1. Create a new note
                 2. Delete your note
                 3. Search for a note
                 4. Close the current note
                 5. View the note''')
        answer = input()
        match answer:
            case '1':
                create()
            case '2':
                delete()
            case '3':
                search()
            case '4':
                close()
            case '5':
                view()
            case _:
                print('You should choose a number from the list.')
                continue



def create():
    note = input('Type a new note: ')
    with open('notes.txt', 'a', encoding = 'UTF-8') as file:
        file.write(note + '\n')
    print('Your note was successfully created! \n')



def delete():
    with open('notes.txt', 'r', encoding = 'UTF-8') as file:
        notes = file.readlines()
    if not notes:
        print('You have not created any notes yet. \n')
        return None
    
    print('List of your notes: ')
    for i, n in enumerate(notes, 1):
        print(f'{i}. {n}')
    note_index = int(input('Which note do you want to delete? — '))
    if note_index > 0 and len(notes) >= note_index:
        notes_except_deleted = []
        for i in range(len(notes)):
            if note_index != i+1:
                notes_except_deleted.append(notes[i])
        with open('notes.txt', 'w', encoding = 'UTF-8') as file:
            file.writelines(notes_except_deleted)
        print('Your note was successfully deleted! \n')
        return None
    print(f'There is no note with number "{note_index}". \n')



def search():
    pass



def close():
    pass



def view():
    pass