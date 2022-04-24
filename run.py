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