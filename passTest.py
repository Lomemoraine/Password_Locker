import unittest

import pyperclip
from password import Credentials, User
class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user = User('account','Lorraine','Chepkemoi','lorraine@gmail.com')
        self.new_credential = Credentials('Twitter','gift','1234')
    def test_init(self):
        self.assertEqual(self.new_user.accountName,"account")
        self.assertEqual(self.new_user.first_name,"Lorraine")
        self.assertEqual(self.new_user.last_name,"Chepkemoi")
        self.assertEqual(self.new_user.email,"lorraine@gmail.com")
    def test_init(self):
        self.assertEqual(self.new_credential.accountName,"Twitter")
        self.assertEqual(self.new_credential.username,"gift")
        self.assertEqual(self.new_credential.password,"1234")
       
        
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_List = []
        Credentials.credential_List = []
    def test_save_user(self):
        '''
        save_user method to test if user is being saved to the user_List
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_List),1)
    def test_save_credential(self):
        '''
        save_credential method to test if credential is being saved to the credential_List
        '''
        self.new_credential.save_credential()
        self.assertEqual(len(Credentials.credential_List),1)
    def test_save_multiple_users(self):
        '''
        test_save_multiple_users to check if we can save multiple users
        objects to our user_List
        '''
        self.new_user.save_user()
        test_user = User("TestAccount","userfirstname","userlastname","test@user.com") # new user
        test_user.save_user()
        self.assertEqual(len(User.user_List),2)
#method to enbale users save more than one account's credentials
    def test_save_multiple_credentials(self):
        '''
        test_save_multiple_credentials to check if we can save multiple credentials
        objects to our credential_List
        '''
        self.new_credential.save_credential()
        test_credential = Credentials("TestAccount","username","1234",) # new credentials
        test_credential.save_credential()
        self.assertEqual(len(Credentials.credential_List),2)
    def test_delete_user(self):
        '''
        test_delete_user method to test if we can remove a user from our user_List
        '''
        self.new_user.save_user()
        test_user = User("TestAccount","userfirstname","userlastname","test@user.com") # new user
        test_user.save_user()
        self.new_user.delete_user()# Deleting a user object
        self.assertEqual(len(User.user_List),1)
#method to delete account credentials 
    def test_delete_credential(self):
        '''
        test_delete_credential method to test if we can remove account's credentials from our credential_List
        '''
        self.new_credential.save_credential()
        test_credential = Credentials("TestAccount","username","1234",) # new credentials
        test_credential.save_credential()
        self.new_credential.delete_credential()# Deleting a account's  credentials object
        self.assertEqual(len(Credentials.credential_List),1)
    def test_find_user_by_username(self):
        '''
        test to check if we can find a user by their first_name and display information
        '''

        self.new_user.save_user()
        test_user = User("TestAccount","userfirstname","userlastname","test@user.com") # new user
        test_user.save_user()
        found_user = User.find_by_username("userfirstname")
        self.assertEqual(found_user.email,test_user.email)
    def test_find_acountcredentials_by_accountName(self):
        '''
        test to check if we can find an account by their accountName and display credentials
        '''

        self.new_credential.save_credential()
        test_credential = Credentials("TestAccount","username","1234",) # new credentials
        test_credential.save_credential()
        found_account = Credentials.find_by_accountName("TestAccount")
        self.assertEqual(found_account.password,test_credential.password)
    def test_user_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the user.
        '''

        self.new_user.save_user()
        test_user = User("TestAccount","userfirstname","userlastname","test@user.com") # new user
        test_user.save_user()
        user_exists = User.user_exist("userfirstname")
        self.assertTrue(user_exists)
    def test_account_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the account's credentials.
        '''

        self.new_credential.save_credential()
        test_credential = Credentials("TestAccount","username","1234",) # new credentials
        test_credential.save_credential()
        account_exists = Credentials.credential_exist("TestAccount")
        self.assertTrue(account_exists)
    def test_display_all_users(self):
        '''
        method that returns a list of all users saved
        '''

        self.assertEqual(User.display_users(),User.user_List)
    def test_display_all_accounts(self):
        '''
        method that returns a list of all account's credentials saved
        '''

        self.assertEqual(Credentials.display_accounts(),Credentials.credential_List)
    # def test_copy_credentials(self):
    #     '''
    #     Test to confirm that we are copying credentials from a found account
    #     '''
    #     self.new_credential.save_credential() 
    #     Credentials.copy_credentials("Twitter")
    #     self.assertEqual(self.new_credential.username,self.new_credential.password, pyperclip.paste())
    
if __name__ == "__main__":
        unittest.main()
