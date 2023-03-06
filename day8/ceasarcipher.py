def encrypt(message, key):
    message = message.upper()
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for letter in message:
        if letter in alphabets:
            letter_index = (alphabets.find(letter) + key) % 26

            result = result + alphabets[letter_index]
        else:
            result = result + letter

    return result


def decrypt(message, key):
    message = message.upper()
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for letter in message:
        if letter in alphabets:
            letter_index = (alphabets.find(letter) - key) % 26

            result = result + alphabets[letter_index]
        else:
            result = result + letter

    return result


choice = 1
while choice != 0:
    print("Welcome to the Ceasar Cipher encryptor/Decryptor")
    choice = int(input("Press 1 to enter data\nPress 0 to exit\n"))
    if (choice == 1):
        data = input("Enter the string: ")
        shift = int(input("Enter the key shift value\n"))
        choice2 = int(
            input("Enter 1 to encrypt the data\nEnter 2 to decrypt the data\n"))
        if (choice2 == 1):
            print(encrypt(data, shift))
        elif (choice == 2):
            print(decrypt(data, shift))
    elif (choice == 0):
        break
