# Coursework Assessment 1
# Name:Riya Riya
# Student No: 2044706

# A Caesar Cipher Program
import os.path
import string

alphabet = string.ascii_letters # "abcdefghijklmnopqrstuvwxyz"

def welcome():
    # add your code here
    print("Welcome to the Caesar Cipher")
    print("This program encrypts and decrypts text with the Caesar Cipher.")
    return


def enter_message():
    mode = ''
    message = ''
    shift = 0
    # add your code here
    while True:
        mode = input("Would you like to encrypt (e) or decrypt (d)?: ")
        if mode == "e":
            message = input("Enter the message to be encrypted: ").upper()
            break
            
        elif mode == "d":
            message = input("Enter the message to be decrypted: ").upper()

            break
        else:
            print("Invalid mode. Please try again.")
            
    
    while True:
        try:
            shift = int(input("Enter the shift (0-25): "))
            if shift >= 0 and shift <= 25:
                break
            else:
                print("Invalid shift. Please try again.")
        except ValueError:
            print("Invalid shift. Please enter a valid number.")

    return (mode, message, shift)


def encrypt(message,shift):
    # add your code here
    """Encrypts the given text using the Caesar Cipher method.

  message: string -- the text to be encrypted
  shift: int -- the number of positions to shift the text

  returns: string -- the encrypted text"""
    encrypted_message = ""
    if message is not None:
        for ch in message:
            if ch.isalpha():
                position = alphabet.find(ch)
                new_position = (position + shift) % 26
                new_character = alphabet[new_position]
                encrypted_message += new_character
        else:
            encrypted_message = encrypted_message.upper()
    return encrypted_message
    


def decrypt(message,shift):
    # add your code here
    decrypted_message = ""
    if message is not None:
        for ch in message:
            if ch.isalpha():
                position = alphabet.find(ch)
                new_position = (position - shift) % 26
                new_character = alphabet[new_position]
                decrypted_message += new_character
            else:
                decrypted_message = decrypted_message.upper()
    return decrypted_message
        

def process_file(filename, mode,shift):
    list_messages = []
    # add your code here
    with open(filename, "r") as f:
        for line in f:
            parts = line.split("\n")
            # shift = parts[0]
            message = parts[0]
            if mode == "e":
                list_messages.append(encrypt(message, shift))
            else:
                list_messages.append(decrypt(message, shift))
    return list_messages


def write_messages(list_messages):
    # add your code here
    with open("results.txt", "w") as f:
        for message in list_messages:
            f.write(message + "\n")
    return


def is_file(filename):
    return True


def message_or_file():
    mode = ''
    filename = None
    message = None
    shift = 0
    # add your code here
    while True:
        mode = input("Enter the mode of conversion e for encrypt, d for decrypt): ")
        if mode == "e" or mode == "d":
            break
        else:
            print("Invalid mode. Please try again.")
    while True:
        media = input("Would you like to read from a file (f) or the console (c)?").lower()
        if media == "c":

            message = input("Enter the message: ")
            while True:
                try:
                    shift = int(input("Enter the shift:"))
                    if 0 <= shift <= 25:
                        return (mode, message, shift, None)
                    else:
                        print("Invalid shift. Please enter a number between 0 and 25.")
                except ValueError:
                    print("Invalid shift. Please enter a number between 0 and 25.")
        elif media == "f":
            while True:
                filename = input("Enter the name of the file: ")

                if is_file(filename):
                    
                   
                    while True:
                        try:
                            shift = int(input("Enter the shift: "))
                            if 0 <= shift <= 25:
                                return (mode, None, shift, filename)
                                
                            else:
                                print("Invalid shift. Please enter a number between 0 and 25.")
                        except ValueError:
                            print("Invalid shift. Please enter a number between 0 and 25.")

        else:
            print("Invalid source. Please enter a valid source.")

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
    # add your code here
    welcome()
    

    while True:
        # mode, message, shift = enter_message()
        mode, message, shift, filename= message_or_file()
        if message:
            if mode == "e":
                encrypted_message = encrypt(message, shift)
                print(f"Your encrypted message is: {encrypted_message}")
                # response = input("Would you like to decrypt another message y/n?")
                # if response =="y":
                #     mode, message, shift = enter_message()
                # else:
                #     exit()

            else:
                decrypted_message = decrypt(message, shift)
                print(f"Your decrypted message is: {decrypted_message}")
                # response = input("Would you like to encrypt another message y/n?")
                # if response =="y":
                #     mode, message, shift = enter_message()
                    
                # else:
                #     exit()
        elif filename:
            messages = process_file(filename, mode, shift)
            write_messages(messages)
            print("Messages processed and written to results.txt.")
        else:
             print("Invalid input. Please try again.")


        while True:
            another = input("Would you like to encrypt/decrypt another message (y/n)? ").lower()
            if another == "y":
                break
            elif another == "n":
                print("Goodbye!")
                return
            

            
            else:
                print("Invalid input. Please enter a valid response.")
        
            


# Program execution begins here
if __name__ == '__main__':
    main()
