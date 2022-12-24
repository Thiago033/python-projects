def caeser(startText, shiftAmount, cipherDirection):
    endText = ""
    
    if cipherDirection == "decode":
        shiftAmount *= -1
    
    for char in startText:
        
        if char in alphabet:
            position = alphabet.index(char)
            newPosition = position + shiftAmount 
            endText += alphabet[newPosition]
        else:
            endText += char
    
    print(f"The {cipherDirection} text is {endText}")
        
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

shift = shift % 26

if direction == "encode" or direction == "decode":
    caeser(text, shift, direction)
else:
    print("invalid option!")