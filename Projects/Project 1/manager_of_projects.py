def interface():
    print('Greetings, my Lord! We praise thee.')
    while True:
        print('''What do you want me to do?
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
    pass



def delete():
    pass



def search():
    pass



def close():
    pass



def view():
    pass