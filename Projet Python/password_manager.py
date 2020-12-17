import os, time, getpass
from menu import menu, fill, find_app_password, find_password_for_accounts
from secret import get_master_password


def cls():  # will clear the screen
    cls = os.system('cls')
    return cls

#__main
cls()

secret = get_master_password()
print('Please enter the master password to start using you password manager: ')
userPassword = getpass.getpass("Enter your password: ")

if userPassword == secret:
    cls()
    print('Password verified, welcome! \nPlease wait while we get everything ready :)')
    time.sleep(1)
    cls()
else:
    print('\n!!!   Incorrect password, you will now exit the password manager interface.   !!!\n')
    time.sleep(1)
    cls()
    exit()

choice = menu()
while choice not in ['Q', 'q']:
    if choice == '1':  # Create new password
        fill()
        cls()
    if choice == '2':  # Find a password based on nickname
        find_app_password()
        cls()
    if choice == '3':  # email to find accounts associated
        find_password_for_accounts()
        cls()
    if choice not in ['q', 'Q', '1', '2',
                      '3']:  # required since if we do not put this the choice 3 is stuck on a loop, no idea why
        print('\nError, choice not recognised')
        time.sleep(1)
        cls()
        choice = menu()
    else:
        cls()
        choice = menu()
cls()
exit()
