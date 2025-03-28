from random import SystemRandom

srandom = SystemRandom()
charset = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&* ()_+-=[]{}|;\':",.<>?/'
charset_size = len(charset)
pad_size = 512
indexed_charset = {}

for i in range(charset_size):
    indexed_charset[charset[i]] = i

def encrypt_message(message, pad):
    if len(message) > len(pad):
        raise ValueError('Message is longer than pad.') 
    encrypted_message = ''
    for i in range(len(pad)):
        if i >= len(message):
            # Padding the message with random characters from the charset
            # to make the encrypted message the same length as the pad
            character = indexed_charset.get(charset[srandom.randrange(charset_size)])
        else:
            character = indexed_charset.get(message[i])
        pad_char = indexed_charset.get(pad[i])
        encrypted_message += charset[(character + pad_char) % charset_size]
    return encrypted_message