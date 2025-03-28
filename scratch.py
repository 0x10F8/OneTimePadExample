from random import SystemRandom

srandom = SystemRandom()
charset = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&* ()_+-=[]{}|;\':",.<>?/'
charset_size = len(charset)
pad_size = 512
indexed_charset = {}
for i in range(charset_size):
    indexed_charset[charset[i]] = i

def generate_pad(pad_size):
    pad = ''
    for i in range(pad_size):
        pad += charset[srandom.randrange(charset_size)]
    return pad

def print_pad(pad, cols=16):
    for i in range(len(pad)):
        if i % cols == 0 and i != 0:
            print()
        print(pad[i], end=' ')
    print()

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

def decrypt_message(encrypted_message, pad):
    decrypted_message = ''
    for i in range(len(encrypted_message)):
        decrypted_message += charset[(indexed_charset[encrypted_message[i]] - indexed_charset[pad[i]]) % charset_size]
    return decrypted_message

pad = generate_pad(pad_size)

message = 'This is an example of a long message that contains various characters in the set, including [] these! The message can also contain numbers 123.'
encrypted_message = encrypt_message(message, pad)
decrypted_message = decrypt_message(encrypted_message, pad)

print('Charset:')
print(charset)

print('Message:', message)

print('Pad:')  
print_pad(pad)

print('Encrypted message:')
print_pad(encrypted_message)

print('Decrypted message:')
print_pad(decrypted_message)