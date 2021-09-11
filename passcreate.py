import numpy as np
import os.path

passwords = []
passwords = np.load('passwords.npy')

located = os.path.isfile('passwords.npy')

def loadpass():
    passwords = np.load('passwords.npy')
    return passwords

def passwordCreation():
    passwords = loadpass()
    passw = input("Create a password: ")
    if len(passw) >= 3:
        password = np.append(passwords, passw)
        print('P a s s w o r d  C r e a t e d')
        np.save('passwords.npy', password)
        main()
    else:
        print ('Password did not match criteria, must be 3 or more characters')
        passwordCreation()
    if passw == 'q':
        quit
    elif passw == 'b':
        main()
    else:
        return
    
def login():
    passwords = loadpass()
    passrep = input()
    if passrep in passwords:
        print('Password Approved - Welcome to the Database')
        logged()
    elif passrep == 'b':
        main()
    elif passrep == 'q':
        quit
    else:
        print('Incorrect Password')
        login()
    

def main():
    if not located:
        np.save('passwords.npy', passwords)

    print("Would you like to\n1 - Create New Password\n2 - Login\n3 - List Passwords\n4 - Quit")
    ifstatement()

def ifstatement():
    passwords = loadpass()
    rep1 = input()
    if rep1 == '1':
        passwordCreation()
    elif rep1 == '2':
        print("Type password, then press ENTER")
        login()
    elif rep1 == '3':
        print(passwords)
        ifstatement()
    elif rep1 == '4' or rep1 == 'q':
        quit
    else:
        print("ERROR|Try Again")
        main()

def logged():
    rep2 = input()
    if rep2 == 'q':
        quit
    elif rep2 == 'b':
        main()
    else:
        print("ERROR|Try Again")
        logged()

main()