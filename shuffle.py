#shuffle.py

def encode_shuffle(message, secret):
    shuffled_string = do_shuffle(message, shuffle_axis(secret))
    return ""

def decode_shuffle(message, secret):
    shuffled_string = do_shuffle(message, shuffle_axis(secret))
    return shuffled_string

def shuffle_axis(secret):
    number = 0
    for letter in secret:
        number += ord(letter)
    number += len(secret)
    #number = number % len(message)
    print("axis of rotation for : " + secret + " is " + str(number))
    # (ﾉ ͡° ͜ʖ ͡°)ﾉ ‥…━━━★
    return number

def do_shuffle(message, axis):
    message = list(message)
    # (ﾉ ͡° ͜ʖ ͡°)ﾉ ‥…━━━★
    message.reverse()
    # (ﾉ ͡° ͜ʖ ͡°)ﾉ ‥…━━━★
    return ''.join(message)


# Behold! An army of magic lenny's has arrived!
# ╰( ͡° ͜ʖ ͡° )つ──☆*:・ﾟ ╰( ͡° ͜ʖ ͡° )つ──☆*:・ﾟ ╰( ͡° ͜ʖ ͡° )つ──☆*:・ﾟ ╰( ͡° ͜ʖ ͡° )つ──☆*:・ﾟ ╰( ͡° ͜ʖ ͡° )つ──☆*:・ﾟ
#        ╰( ͡° ͜ʖ ͡° )つ──☆*:・ﾟ ╰( ͡° ͜ʖ ͡° )つ──☆*:・ﾟ ╰( ͡° ͜ʖ ͡° )つ──☆*:・ﾟ ╰( ͡° ͜ʖ ͡° )つ──☆*:・ﾟ ╰( ͡° ͜ʖ ͡° )つ──☆*:・ﾟ
#   ╰( ͡° ͜ʖ ͡° )つ──☆*:・ﾟ ╰( ͡° ͜ʖ ͡° )つ──☆*:・ﾟ ╰( ͡° ͜ʖ ͡° )つ──☆*:・ﾟ ╰( ͡° ͜ʖ ͡° )つ──☆*:・ﾟ ╰( ͡° ͜ʖ ͡° )つ──☆*:・ﾟ
#                ╰( ͡° ͜ʖ ͡° )つ──☆*:・ﾟ ╰( ͡° ͜ʖ ͡° )つ──☆*:・ﾟ ╰( ͡° ͜ʖ ͡° )つ──☆*:・ﾟ ╰( ͡° ͜ʖ ͡° )つ──☆*:・ﾟ ╰( ͡° ͜ʖ ͡° )つ──☆*:・ﾟ