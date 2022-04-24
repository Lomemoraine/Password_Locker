class User:
    '''
    class that generates new instances of users
    
    '''
    user_List =[]
    def __init__(self,accountName,first_name,last_name,email):
        self.accountName = accountName
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
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