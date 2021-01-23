#vigenere.py

# Performs the Vigenère cipher operation
def encode_vigenere(message, secret):
    newmsg = ""
    for i in range(len(message)):
        if(message[i].isupper()):
            number = 65 + (ord(message[i]) + ord(secret[i%len(secret)]) - 2*65) % 26
            newmsg += chr(number)
    return newmsg