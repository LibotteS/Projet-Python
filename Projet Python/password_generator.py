import string, random


def encrypt_password(pwd):
    pass

def random_password_cpx3():

    print('please enter the length : ')
    length = input('\n Users => ')
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(int(length)))

def random_password_cpx2():

    print('please enter your password: ')
    password = input('\nUsers =>')
    new_password = ''
    for i in range(len(password)):
        if password[i] == 'a':
            new_password = new_password+'@'
        else:
            new_password = new_password+password[i]

    print(new_password)

def random_password_cpx1():

    print('please enter your password: ')
    password = input('\nUsers =>')

# length = x  complexity 1-3
# dictionnaire
    # 1. entrer mdp
    # 2. entrer mdp et complexifier
    # 3. random

    #if mot[i] == 'a'

    # cpx = 3 > random password
        # min length = 8
        #gestion erreur utilisateur choisis longeur 6 et cpx 3 > erreur please .... > complexity first

