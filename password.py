#users class
import random
import string

import pyperclip


class User:
    '''
    class that generates new instances of users
    
    '''
    user_List =[]
    def __init__(self,first_name,last_name,email,password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
    def save_user(self):
        '''
        save_user method that saves users into user_List
        
        '''
        User.user_List.append(self)
    def delete_user(self):

        '''
        delete_user method deletes a saved user from the user_List
        '''
        
        User.user_List.remove(self)
    @classmethod
    def find_by_username(cls, username):
        '''
        Method that takes in a username and returns a user that matches that username.

        Args:
            username: name to search for
        Returns :
            first name of user that matches that username.
        '''

        for user in cls.user_List:
            if user.first_name == username:
                return user
    @classmethod
    def user_exist(cls,username):
        '''
        Method that checks if a user exists from the user_List.
        Args:
            username: name to search for
        Returns :
            Boolean: True or false depending if the user exists
        '''
        for user in cls.user_List:
            if user.first_name == username:
                    return True

        return False
    @classmethod
    def display_users(cls):
        '''
        method that returns the user_List
        '''
        return cls.user_List
    
#credentials class
class Credentials:
    '''
    class that generate new instances of credentials
    '''
    credential_List = []
    def __init__(self,accountName,username,password):
        self.accountName = accountName
        self.username = username
        self.password = password
#method to generate password using the random module and string module
    def generate_password(self, size=8, char=string.ascii_uppercase+string.ascii_lowercase+string.digits):
            """
            generate_password function to generate passwords
            """

            generate_pass = ''.join(random.choice(char)for _ in range(size))#convert elements of an iterable into a string
            return generate_pass
    def save_credential(self):
        '''
        save_credential method that saves credentials into credential_List
        
        '''
        Credentials.credential_List.append(self)
    def delete_credential(self):

        '''
        delete_credential method deletes a saved credential from the credential_List
        '''
        
        Credentials.credential_List.remove(self)
    @classmethod
    def find_by_accountName(cls, account):
        '''
        Method that takes in an account and returns account credentials that matches that account.

        Args:
            account: account to search for
        Returns :
            accountName of credentials that matches that account.
        '''

        for credentials in cls.credential_List:
            if credentials.accountName == account:
                return credentials
    @classmethod
    def credential_exist(cls, account):
        '''
        Method that checks if an account's credntials exists from the credential_List.
        Args:
            account: accountName to search for
        Returns :
            Boolean: True or false depending if the account exists
        '''
        for credentials in cls.credential_List:
            if credentials.accountName == account:
                    return True

        return False
    @classmethod
    def display_accounts(cls):
        '''
        method that returns the credentials_List
        '''
        return cls.credential_List
    
    @classmethod
    def copy_credentials(cls, account):
        '''
        method that copies returned account's credentials to clipboard
        '''
        found_account = Credentials.find_by_accountName(account)
        pyperclip.copy(found_account.password)
    