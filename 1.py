def encryption(fock):
    encrypt = fock
    encrypt = encrypt.lower()
    key = 3
    alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    encrypted = ""
    for letter in encrypt:
        position = alphabet.find(letter)
        newPosition = position + key
        if letter in alphabet:
            encrypted = encrypted + alphabet[newPosition]
        else:
            encrypted = encrypted + letter
    print(encrypted)

f = open('alo.txt', 'r')
text = "".join(f)
print(text)
encryption(text)
