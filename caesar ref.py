# Coursework Assessment 1
# Name:GURJEET SINGH 
# Student No:2116898

# A Caesar Cipher Program
import os.path
import string

alphabet = string.ascii_letters # "abcdefghijklmnopqrstuvwxyz"
def welcome():
    # add your code here
    print("Welcome to the Caesar Cipher\nThis program encrypts and decrypts text with the Caesar Cipher.\n")
    return
    return


def enter_message():
    mode = ''
    message = ''
    shift = 0
    # add your code here
    mode = input("Would you like to encrypt (e) or decrypt (d): ")
    
    if mode == "e":
       
        encrypt ()
    elif mode =="d":
        
        decrypt(message,shift)
    else: 
        print('Invalid mode entered\n')
        enter_message()
        
        print()
    
    return(mode, message,shift)

def encryptWithParams(message, key):
    encrypted_message = ""
    if  message is not None:

        for c in message:
        

            if c in alphabet:
                position = alphabet.find(c)
                new_position = (position + key) % 26
                new_character = alphabet[new_position]
                encrypted_message += new_character
            else:
                encrypted_message += c
        return encrypted_message
   

def encrypt():
    source = input("Would you like to read from the file(f) of the console(c)")
    if source == "f":
        file1 = open(input('Enter a file name'))
        message1 = file1.read().lower()
        print()
        file1.close()
    else:
        message1 = input("Type a message you would like to encrypt: ").lower()
        print()
    shift1 = int(input("Enter your cypher step: "))
     
    encrypted_message = encryptWithParams(message1,shift1)

    print("Your encrypted message is:\n")
    print(encrypted_message)
    response = input("Would you like to encrypt another message y/n?")
    if response =="y":
        encrypt()
    else:
        exit()




def decrypt(message,shift):
    # add your code here
    
    print("Welcome to Caesar Cipher Decryption.\n")
    encrypted_message = input("What message would you like to decrypt: ").strip().lower()
    print()
    print()
    shift = int(input("Enter key to decrypt: "))
    
    decrypted_message = ""

    for c in encrypted_message:

        if c in alphabet:
            position = alphabet.find(c)
            new_position = (position - shift) % 26
            new_character = alphabet[new_position]
            decrypted_message += new_character
        else:
            decrypted_message += c
    print("Your decrypted message is:\n")
    print(decrypted_message)
    response = input("Would you like to decrypt another message y/n?")
    if response =="y":
        decrypt(message, shift)
    else:
        exit()
    return decrypted_message


        

def process_file(filename, mode,shift):
    list_messages = []
    # add your code here
    return list_messages


def write_messages(lines):
    # add your code here
   
    return


def is_file(filename):
    return False


def message_or_file():
    mode = ''
    filename = None
    message = None
    shift = 0
    # add your code here

    return (mode, message, filename, shift)
    
"""
MAIN DRIVER FUNCTION
----------------------------------------------------------------------------------------------
Requirements:
    • Prompt users to select a mode: encrypt (e) or decrypt (d).
    • Check if the mode the user entered is valid.
    If not, continue to prompt the user until a valid mode is selected.
    • Prompt the user for the message they would like to encrypt/decrypt.
    • encrypt/decrypt the message as appropriate and print the output.
    • Prompt the user whether they would like to encrypt/decrypt another message.
        • Check if the user has entered a valid input (y/n).
          If not, continue to prompt the user until they enter a valid response.
          Depending upon the response you should either:
            • End the program if the user selects no.
            • Proceed directly to step 2 if the user says yes.
    • Your program should be as close as possible to the example shown in the assessment specification.
"""
def main():
    # add your code 
    welcome()
    enter_message()
    return


# Program execution begins here
if __name__ == '__main__':
    main()
