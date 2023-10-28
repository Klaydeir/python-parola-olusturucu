import random
import string

def generate_password(length, level, output=[]):
    chars = string.ascii_letters
    if level > 1:
        chars = "{}{}".format(chars, string.digits)
    if level > 2:
        chars = "{}{}".format(chars, string.punctuation)
    
    for i in range(length):
        output.append(random.choice(chars))
    
    return "".join(output)

print(("-" * 30) + "\n Parola Oluşturucu\n" + ("-" * 30))

password_length = int(input("Uzunluk: "))
password_level = int(input("Seviye: "))

password = generate_password(password_length, password_level)
print("\nSenin Parolan: {}".format(password))
