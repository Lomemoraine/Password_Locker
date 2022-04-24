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
    
if __name__ == "__main__":
        unittest.main()
