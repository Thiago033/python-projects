# Dictionary representing the morse code chart
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}


def encrypt(message):
    morse_code = ''

    for letter in message:
        if letter == ' ':
            morse_code += '/ '
        else:
            morse_code += MORSE_CODE_DICT[letter.upper()] + ' '

    return morse_code


def decrypt(message):
    # extra space added at the end to access the last morse code
    message += ' '
    decipher = ''
    citext = ''
    jump = False
    
    for letter in message:
        if (letter != ' ' and letter != '/'):
            i = 0
            citext += letter
            
        else:
            i += 1
            
            if i == 2 :
                decipher += ' '
                
                #don't read the next space
                jump = True
            else:
                if not jump:
                    decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)]
                    citext = ''
                jump = False
    return decipher


#User input
option = int(input("to encrypt a message type (1)\n to decrypt a message type (2)\n"))
message = input("Type a text to convert: ")

if option == 1:
    result = encrypt(message)
else:
    result = decrypt(message)
    
print(result)
