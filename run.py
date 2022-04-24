#!/usr/bin/env python3.9
import string
import random
import array
from typing import Any
from passwordd import Credentials, User
def generate_password():
    length = 8
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation
    all = lower + upper + num + symbols
    temp = random.sample(all,length)
    password = "".join(temp)
    return password

def create_user(fname,lname,email,password):
    '''
    Function to create a new user
    '''
    new_user = User(fname,lname,email,password)
    return new_user
def save_user(user):
    '''
    Function to save user
    '''
    user.save_user()
# def generate_password(credential):
#     '''
#     Function to generate password
#     '''
#     credential.generate_password()
# def del_user(user):
#     '''
#     Function to delete a user
#     '''
#     user.delete_user()
def find_user(first_name):
    '''
    Function that finds a user by their fisrt name and returns the user
    '''
    return User.find_by_first_name(first_name)
def check_existing_users(first_name):
    '''
    Function that check if a user exists with that username and return a Boolean
    '''
    return User.user_exist(first_name)
# def display_users():
#     '''
#     Function that returns all the saved users
#     '''
#     return User.display_users()
def create_credentials(accountName,username, password):
    new_credential = Credentials(accountName,username,password)
    return new_credential
def save_credential(credential):
    '''
    Function to save created credentials
    '''
    credential.save_credential()
def save_multiple_credentials(credential):
    '''
    save_multiple_credentials to save more than one credential
    '''
    credential.save_multiple_credentials()
def display_credentials():
    '''
    Function that returns all the saved credentials
    '''
    return Credentials.display_credentials()
def find_credential(account):
    return Credentials.find_by_accountName(account)

#Check existing credential
def credential_exist(account):
    return Credentials.credential_exist(account)

#Display all credentials for a particular user
def delete_credential(credential): 
    '''
    Function to delete credentials that are no longer needed
    '''
    credential.delete_credential()

def main():
    while True:
       
        # print("Hello Welcome to Password Locker. What is your name?")
        # user_name = input()
        print("""Hello esteemed user.Welcome to PassWord Locker .
              Use these short codes to login or create an account with password Locker:
              li -log in, ca -create account""")
        print('\n')
        short_code = input().lower()
        if short_code == 'li':
            first_name = input("Enter your first name as your Username: ").lower()
            password = input("Enter your password: ")
            if check_existing_users(first_name):
                search_user = find_user(first_name)
                
                print('-'*20)
                print(f"Hello , You have been succesfully logged in")
                print("-"*20)
                while True:
                    print("\n")
                    print("Use these short codes : cc - create a new credential, dc - display credentials, fc -find a credential, ex -exit the passWord Locker ")
                    short_code1 = input().lower()
                    if short_code1 == 'cc':
                        print("New account Credentials")
                        print("-" * 20)
                        accountName =input("Enter account whose credentials youu want to store: ".lower())
                        username = input("Enter username you want to use for the account: ")
                        print(f"Use generated password for your {accountName} account or manually generate.Shortcode3: yes or no ")
                        if credential_exist(accountName):
                            search_user = find_user(accountName)
                            print("Account with that account name is already existing,create new account")
                        else:
                            shortcode = input().lower()
                            if shortcode == "yes":
                                password = str(generate_password())
                                print("-"*20)
                            elif shortcode == "no":
                                password = input("Enter your preferred password: ")
                            else:
                                print("Please try again")
                        save_credential(create_credentials(accountName,username,password))
                        print(f"{accountName} credentials have been saved")
                        print("\n")
                    elif short_code1 == "dc":
                        if display_credentials():
                            print(f"{first_name};these are your added credentials")
                            print("\n")
                            for credential in Credentials.credential_List:
                                print(f"{credential.accountName}   {credential.username}  {credential.password}")
                                print("-"*20)
                        else:
                            print("Seems you have not added any credentials yet")
                    elif short_code1 == "fc":
                         search_account = input("Enter account name you are looking for: ").lower()
                         if credential_exist(search_account):
                             find_account =find_credential(search_account)
                             print("-"*20)
                             print(f"{find_account.accountName} { find_account.username} { find_account.password}")
                             print("-"*20)
                         else:
                             print("The credential you are searching for does not exist")
                    elif short_code1 == "ex":
                        input("Bye...")
                        break
                            
                        
                    
            else:
                print('-'*20)
                print("User does not exist")
                print('-'*20)
        elif short_code == 'ca':
            
            print("\n")
            print("Create a new user account")
            print("-" * 20)
            print("Enter your first name")
            first_name = input()
            print('\n')
            print("Enter your last name")
            last_name = input()
            print('\n')
            print("Enter your email address")
            email_address = input()
            print('\n')
            if check_existing_users(first_name):
                search_user = find_user(first_name)
                print("user with that name  already exists,try a different name")
            else:
                    
                    print("Automatically generate a password or create your own? Shortcode3: yes or no")
                    shortcode = input().lower()
                    if shortcode == "yes":
                        password = generate_password()
                        print("-"*20)
                    elif shortcode == "no":
                        password = input("Enter your preferred password: ")
                    else:
                        print("Please try again")
            
            
            save_user(create_user(first_name, last_name,email_address,password ) )
            print("-"*20)
            print(f'Account for {first_name} {last_name} has been successfully created')
            print(f'Your password is : {password}')
            print("-"*20)
            print("\n")
            print("Please proceed to login by typing li")
            
        else:
            print("I really didn't get that. Please use the short codes")
        
                            
                 
            
if __name__ == '__main__':
    main()

    
            
            
           