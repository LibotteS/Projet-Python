import string, random
from cryptography.fernet import Fernet


def generate_key():
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    """
    Load the previously generated key
    """
    return open("secret.key", "rb").read()

def encrypt_message(message):
    """
    Encrypts a message
    """
    key = load_key()
    encoded_message = message.encode()
    f = Fernet(key)
    encrypted_message = f.encrypt(encoded_message)

    print(encrypted_message)

if __name__ == "__main__":
    encrypt_message("encrypt this message")


def random_password_cpx3(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(int(length)))


def random_password_cpx2(user_password):
    pwd = list(user_password)
    for i in range(len(pwd)):
        if pwd[i] == 'a':
            pwd[i] = '@'
        if pwd[i] == 'i':
            pwd[i] = '!'
        if pwd[i] == 's':
            pwd[i] = '$'
        if pwd[i] == 'e':
            pwd[i] = '3'
        if pwd[i] == 'o':
            pwd[i] = '0'
        if pwd[i] == 'u':
            pwd[i] = 'µ'
        if pwd[i] == 'l':
            pwd[i] = '1'
        if pwd[i] == 'b':
            pwd[i] = 'B'
        if pwd[i] == 'p':
            pwd[i] = 'P'
        if pwd[i] == 't':
            pwd[i] = 'T'

    return "".join(pwd)


Fernet.generate_key()

# length = x  complexity 1-3
# dictionnaire
# 1. entrer mdp
# 2. entrer mdp et complexifier
# 3. random

# if mot[i] == 'a'

# cpx = 3 > random password
# min length = 8
# gestion erreur utilisateur choisis longeur 6 et cpx 3 > erreur please .... > complexity first
