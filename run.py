#!/usr/bin/env python3.9
from password import Credentials, User
def create_user(account,fname,lname,email):
    '''
    Function to create a new user
    '''
    new_user = User(account,fname,lname,email)
    return new_user
def save_user(user):
    '''
    Function to save user
    '''
    user.save_user()
def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()
def find_user(username):
    '''
    Function that finds a user by username and returns the user
    '''
    return User.find_by_username(username)
def check_existing_users(username):
    '''
    Function that check if a user exists with that username and return a Boolean
    '''
    return User.user_exists(username)
def display_users():
    '''
    Function that returns all the saved users
    '''
    return User.display_users()
def main():
    print("Hello Welcome to Password Locker. What is your name?")
    user_name = input()
    print(f"Hello {user_name}. what would you like to do?")
    print('\n')
    while True:
        print("Use these short codes : cc - create a new credential, dc - display credentials, fc -find a credential, ex -exit the passWord Locker ")
        short_code = input()
        if short_code == 'cc':
            print("New account Credentials")
            print("-" * 10)

            print("Account name ....")
            a_name = input()

            print("Username ...")
            u_name = input()
            print(f'Generate password for{a_name} Enter 1 to accept or 2 to reject')
            answer = print('\n')
            if answer == "1":
               password = str(Credentials.generate_password())
               print(f'Your generated password for{a_name} is{password}\n')
                
            elif answer == "2":
                print(f'Enter password for{a_name}\n')
                password = input('\n' )
            else:
                print('PLease use the given codes')
        
        
            print("New account Credentials have been saved")
            
if __name__ == '__main__':

    main()
            
            
           