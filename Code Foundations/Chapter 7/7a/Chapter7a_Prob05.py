import os
import pickle


#----CODE STARTS HERE------

def choice():
    user_input = 0
    while user_input == 0:
        print('1. Add Record')
        print('2. Display Record')
        print('3. Search a Record')
        print('4. Exit')
        user_input = input('Enter choice(1-4): ')
        if user_input != '1' and user_input != '2' and user_input != '3' and user_input != '4':
            os.system('cls||clear')
            print('Please enter valid choice\n')
            user_input = 0
    return user_input

def book_append():
    if os.path.exists('book.dat'):
        book = open('book.dat', 'ab')
    else:
        book = open('book.dat', 'xb')
        book = open('book.dat', 'ab')
    return book

def book_read():
    if os.path.exists('book.dat'):
        book = open('book.dat', 'rb')
    else:
        book = open('book.dat', 'xb')
        book = open('book.dat', 'rb')
    return book

def add_record():
    book = book_append()

    book_data = {}
    bookID = int(input('Enter book ID: '))
    bookTitle = input('Enter book title: ')
    category = input('Enter category: ')
    author = input('Enter author: ')

    book_data['bookID'] = bookID
    book_data['bookTitle'] = bookTitle
    book_data['category'] = category
    book_data['author'] = author

    pickle.dump(book_data, book)
    book.close()

def display_records():
    book = book_read()

    while True:
        try:
            content = pickle.load(book)
            print('ID:', content['bookID'])
            print('Book Title:', content['bookTitle'])
            print('Category:', content['category'])
            print('Author:', content['author'])
            print()
        except:
            break
    book.close()

def search_record():
    book = book_read()
    choice = ''
    while choice == '':
        print('1. Search via ID')
        print('2. Search via Book Title')
        choice = input('Enter choice(1 or 2):')
        isTrue = False
        if choice == '1':
            search = input('Enter book ID: ')
            # pass
            while True:
                try:
                    content = pickle.load(book)
                    if content['bookID'] == int(search):
                        print('\nID:', content['bookID'])
                        print('Book Title:', content['bookTitle'])
                        print('Category:', content['category'])
                        print('Author:', content['author'])
                        print()
                        isTrue = True
                except:
                    if not isTrue:
                        print('Record not Found')
                    break
        elif choice == '2':
            # pass
            search = input('Enter book Title: ')
            while True:
                try:
                    content = pickle.load(book)
                    if content['bookTitle'] == search:
                        print('\nID:', content['bookID'])
                        print('Book Title:', content['bookTitle'])
                        print('Category:', content['category'])
                        print('Author:', content['author'])
                        print()
                        isTrue = True
                except:
                    if not isTrue:
                        print('Record not Found')
                    break
        else:
            choice = ''
            os.system('cls||clear')
            print('Please enter valid choice\n')
    book.close()

def start():
    os.system('cls')
    pick = choice()
    if pick == '1':
        add_record()
    elif pick == '2':
        display_records()
    elif pick == '3':
        search_record()
    elif pick == '4':
        return 0
    repeat = ''
    while repeat == '':
        repeat = input('Do you want to Run the program again? [Y/N] \nEnter your choice: ').upper()
        if repeat == 'Y':
            start()
        elif repeat == 'N':
            return 0
        else:
            os.system('cls||clear')
            print('Please enter valid input\n')
            repeat = ''
# Start the program
start()