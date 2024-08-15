#function parameters & caesar cipher

from Caesar_cipher_art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)

def caesar(t, s, d): # t = text, s = shift, d = direction
    empty_string = ""
    if d == 'encode':
        for char in t:
            if char in alphabet:
                position = alphabet.index(char)
                new_position = position + s
                empty_string += alphabet[new_position]
            else:
                empty_string += char
        print(f"Here's the encoded result: {empty_string}")
    elif d == 'decode':
        for char in t:
            if char in alphabet:
                position = alphabet.index(char)
                new_position = position - s
                empty_string += alphabet[new_position]
            else:
                empty_string += char
        print(f"Here's the decoded result: {empty_string}")

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
    text = input("Type your message: \n").lower()
    shift = int(input("Type the shift number: \n"))
    shift = shift % 26
    caesar(text, shift, direction)
    choice = input("Type 'Yes' if you want to go again. Otherwise type 'No': \n").lower()
    if choice == 'no':
        should_continue = False
        print("Goodbye")