import os, string, random
from cryptography.fernet import Fernet


# encryption

def generate_key():
    key = Fernet.generate_key()
    with open('secret.key', 'wb') as key_file:  # write binary
        key_file.write(key)

def load_key():
    if os.stat("secret.key").st_size == 0:
        generate_key()
    return open('secret.key', 'rb').read()  # read binary

def encrypt_password(password):
    key = load_key()
    encoded_password = password.encode()
    f = Fernet(key)
    encrypted_password = f.encrypt(encoded_password)
    print(encrypted_password)
    return encrypted_password


def decrypt_password(encrypted_password):
    key = load_key()
    f = Fernet(key)
    decrypted_password = f.decrypt(encrypted_password)
    return decrypted_password


if __name__ == '__main__':
    encrypt_password('encrypt this password')


# generating password


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

# length = x  complexity 1-3
# dictionnaire
# 1. entrer mdp
# 2. entrer mdp et complexifier
# 3. random

# if mot[i] == 'a'

# cpx = 3 > random password
# min length = 8
# gestion erreur utilisateur choisis longeur 6 et cpx 3 > erreur please .... > complexity first
