import string, random
from database_manager import store_passwords, retrieve_app_password, retrieve_password_for_account, verify_app_name

minimum_length = 6


def menu():
    print('_' * 50)
    print((' ' * 23) + 'Menu' + (' ' * 23))
    print('_' * 50)
    print('Welcome in your password manager. You want to : ')
    print('1. Store login info')
    print('2. Find a password for a site or app')
    print('3. Find all sites and apps connected to an email')
    print('Q. Exit')
    print('_' * 50)
    return input('User => ')


def fill():
    print(
        'Please enter a nickname by which you will recognise the saved site/app (note: this nickname must be unique) : ')
    app_name = input('\nUser => ')
    # verify that the nickname is not already in use > create in database_manager.py > verify_app_name(app_name)
    is_taken = False
    while not is_taken:
        if verify_app_name(app_name):
            print(
                'The given nickname > ', app_name,
                ' < already exists. It MUST be UNIQUE, please enter another nickname : ')
            app_name = input('\nUser => ')
        else:
            is_taken = True
    print('_' * 50)
    print('\nPlease make a choice, would you rather : ')
    print('1. Enter your own password')
    print('2. Use the random password generator')
    print('3. Use the word complexifier')
    answer = input('\nUser => ')

    password = ''
    choice = False
    while choice != True:
        if answer == '1':
            print(
                'Please provide your password for this site (minimum 6 characters, we recommend at least 10 characters): ')
            password = input('\nUser => ')
            while len(password) < minimum_length:
                print('Password is too short, please enter a password with at least ', minimum_length, ' characters : ')
                password = input('\nUser => ')
            choice = True
        if answer == '2':
            print('Choose the length ( minimum 6) : (for a strong password we recommend a length between 8 and 16)')
            length = input('\nUser => ')
            while len(password) < minimum_length:
                print('Password is too short, please enter a password with at least ', minimum_length, ' characters : ')
                password = input('\nUser => ')
            caracters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(caracters) for i in range(int(length)))
            choice = True

    print('_' * 50)
    print(' ')
    print('Your password has been added to the database')
    print(' ')
    print('_' * 50)
    print('Please provide a user email for this app or site\n')
    user_mail = input('User => ')
    print('Please provide a username for this app or site (if applicable)\n')
    username = input('User => ')
    if username == None:
        username = ''
    print('Please paste the url to the site that you are creating the password for\n')
    url = input('User => ')
    store_passwords(password, user_mail, username, url, app_name)


def find_app_password():
    print('Please enter the name of the app you wish to find a password for: \n')
    app_name = input('User => ')
    retrieve_app_password(app_name)
    input('Press ENTER to return to the main menu...')
    # cls()


def find_password_for_accounts():
    print('Please enter the email to find accounts associated with it: \n')
    user_email = input('User => ')
    retrieve_password_for_account(user_email)
    input('Press ENTER to return to the main menu...')
    # cls()
