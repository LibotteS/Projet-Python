import string, random

def random_password(length):
    caracters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(caracters) for i in range(int(length)))
    print(password)
random_password(3)