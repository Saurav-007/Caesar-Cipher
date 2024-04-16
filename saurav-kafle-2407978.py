import os

ALPHABETS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Welcome Message
def welcome():
    '''
        Prints welcome message for the ceasar cipher program.
    ''' 
    print("Welcome to the Caesar Cipher.")
    print("This program encrypts and decrypts text with the Caesar Cipher.")


# Take mode from user
def enter_message():
    '''
        Takes input from user
    '''
    while True:
        mode = input("Would you like to encrypt (e) or decrypt (d)?: ").lower()
        if mode in ['e', 'd']:
            break
        else:
            print("Invalid Mode")

    while True:
        source = input("Do you want to process messages using console or file? (c or f): ").lower()
        if source in ['c', 'f']:
            break
        else:
            print("Invalid Source")

    if source == 'c':
        message = input(f"What message would you like to {("encrypt" if mode == 'e' else "decrypt")}: ")
        shift = int(input("What is the shift number: "))
        return mode, message.upper(), None, shift
    else:
        while True:
            file_name = input("Enter file name with its extension: ")
            if os.path.exists(file_name):
                break
            else:
                print("File not found.")

        shift = int(input("What is the shift number: "))
        return mode, None, file_name, shift
    

# Function to encrypt the message using caesar Cipher and Returns the encrypted message
def encrypt(message, shift):
    '''
    Encrypts the message using the caesar cipher
    '''
    encrypted_message = ""
    for char in message:
        char = char.upper()
        if char in ('', ' ', '\n'):
            encrypted_message += char
        elif char.isalpha():
            index = ALPHABETS.index(char) + shift
            encrypted_char = ALPHABETS[index]
            encrypted_message += encrypted_char
        else:
            encrypted_message += char
    return encrypted_message.upper()


# Function to decrypt the message carsar Cipher and Returns the decrypted message
def decrypt(message, shift):
    '''
    Decrypt the message using the casesir cipher
    '''
    return encrypt(message, -int(shift))


# processes the file and read line by line and encrypt or decrypt it based on mode and store it in a list
def process_file(file_name, shift, mode):
    '''
    Text file processes it
    
    '''
    with open(file_name, 'r') as file:
        if mode == "e":
            messages = [encrypt(line.strip(), shift) for line in file]
        else:
            messages = [decrypt(line.strip(), shift) for line in file]
            
    return messages


# Write encrypted/decrypted message to a new file
def write_result(messages):
    '''
    writes the list of messages to a file called results.txt
    '''
    with open('results.txt', 'w') as file:
        for msg in messages:
            file.write(msg + '\n')


# Main function to start the program and also print the output
def main():
    
# Printing the welcome message
    welcome()

    while True:
        mode, message, file_name, shift = enter_message()

        if message:
            
            if mode == "e":
                result = encrypt(message, shift)
                print(result)
                write_result([result])
            else:
                result = decrypt(message, shift)
                print(result)
                write_result([result])                
        
        else:
            messages = process_file(file_name, shift, mode)
            for msg in messages:
                print(msg)
            print("Action completed successfully.")
            write_result(messages)

        another_message = input("Would you like to encrypt or decrypt another message? (y/n): ").lower()
        if another_message != 'y':
            print("Thanks for using the program, goodbye!")
            break


#  Start
main()





