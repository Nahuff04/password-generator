import random
from werkzeug.security import generate_password_hash

minus = "abcdefghijklmnopqrstuvwxyz"
mayus = minus.upper()
num = "0123456789"
simb = "/*+-_$&%."

base = minus+mayus+num+simb
longitud = 15

for _ in range(100):
        muestra = random.sample(base, longitud)
        password ="".join(muestra)
        password_encr = generate_password_hash(password)
        print("{} -> {}".format(password, password_encr))
