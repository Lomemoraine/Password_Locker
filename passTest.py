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
if __name__ == "__main__":
        unittest.main()
