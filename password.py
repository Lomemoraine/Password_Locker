class User:
    '''
    class that generates new instances of users
    
    '''
    user_List =[]
    def __init__(self,first_name,last_name,phone_number,email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email