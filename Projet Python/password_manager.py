import os, time
from menu import menu, fill, retrieve_app_password, find_password_for_accounts
from secret import get_master_password

def cls(): #will clear the screen
    cls = os.system('cls')
    return cls

cls()

secret = get_master_password()
print('Please enter the master password to start using you password manager: ')
userPassword = input('User => ')

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
while choice != 'Q':
    if choice == '1':  # Create new password
        fill()
    if choice == '2':  # Find all sites and apps connected to an email
        find_password_for_accounts()
    if choice == '3':  # Find a password for a site or app
        retrieve_app_password()
    else:
        choice = menu()
cls()
exit()
