from random import SystemRandom

srandom = SystemRandom()
charset = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&* ()_+-=[]{}|;\':",.<>?/'
charset_size = len(charset)
pad_size = 512


def generate_pad(pad_size):
    pad = ''
    for _ in range(pad_size):
        pad += charset[srandom.randrange(charset_size)]
    return pad

no_pads_to_generate = 100

with open(f'pads.txt', 'a') as f:
    # Generate and write the pads to the file
    for i in range(no_pads_to_generate):
        pad = generate_pad(pad_size)
        f.write(f"Pad: {i+1}\n")
        f.write(f"{pad}\n")
        f.write("--------------------------------------------------\n")