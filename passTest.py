import unittest
from password import User
class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user = User('Twitter','Lorraine','Chepkemoi','lorraine@gmail.com')