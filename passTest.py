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
        self.new_user.save_user()
        self.assertEqual(len(User.user_List),1)
    
if __name__ == "__main__":
        unittest.main()
