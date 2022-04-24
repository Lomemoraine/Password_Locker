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