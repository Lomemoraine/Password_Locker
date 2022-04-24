import unittest
from password import User
class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user = User('Twitter','Lorraine','Chepkemoi','lorraine@gmail.com')
    def test_init(self):
        self.assertEqual(self.new_user.accountName,"Twitter")
        self.assertEqual(self.new_user.first_name,"Lorraine")
        self.assertEqual(self.new_user.last_name,"Chepkemoi")
        self.assertEqual(self.new_user.email,"lorraine@gmail.com")
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_List = []
    def test_save_user(self):
        '''
        save_user method to test if user is being saved to the user_List
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_List),1)
    def test_save_multiple_users(self):
        '''
        test_save_multiple_contact to check if we can save multiple contact
        objects to our contact_list
        '''
        self.new_user.save_user()
        test_user = User("TestAccount","userfirstname","userlastname","test@user.com") # new user
        test_user.save_user()
        self.assertEqual(len(User.user_List),2)
    def test_delete_user(self):
        '''
        test_delete_user method to test if we can remove a user from our user_List
        '''
        self.new_user.save_user()
        test_user = User("TestAccount","userfirstname","userlastname","test@user.com") # new user
        test_user.save_user()
        self.new_user.delete_user()# Deleting a user object
        self.assertEqual(len(User.user_List),1)
    def test_find_user_by_username(self):
        '''
        test to check if we can find a user by their first_name and display information
        '''

        self.new_user.save_user()
        test_user = User("TestAccount","userfirstname","userlastname","test@user.com") # new user
        test_user.save_user()
        found_user = User.find_by_username("userfirstname")
        self.assertEqual(found_user.email,test_user.email)
    
if __name__ == "__main__":
        unittest.main()
