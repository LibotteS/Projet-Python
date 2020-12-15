import string, random


def encrypt_password(pwd):
    pass

def random_password_cpx3(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(int(length)))

def random_password_cpx2(length):
    pass

def random_password_cpx1(length):
    pass
# length = x  complexity 1-3
# dictionnaire
    # 1. entrer mdp
    # 2. entrer mdp et complexifier
    # 3. random

    #if mot[i] == 'a'

    # cpx = 3 > random password
        # min length = 8
        #gestion erreur utilisateur choisis longeur 6 et cpx 3 > erreur please .... > complexity first