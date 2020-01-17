FILE_TO_OPEN = 'token'

with open(FILE_TO_OPEN, 'rb') as fd:
    toDecrypt = fd.read()
    decryption = ''
    for index, value in enumerate(toDecrypt):
        calculatedValue = value - index;
        decryption += str(chr(calculatedValue)) if calculatedValue > 0 else '\0'
    print(decryption)

