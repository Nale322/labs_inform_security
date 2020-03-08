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
    return encrypted

f1 = open('alo.txt', 'r')
text = "".join(f1)
gg = encryption(text)
f2 = open('poka.txt', 'w')
f2.writelines(gg)
f2.close()
