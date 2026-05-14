import time

class User:
    def __init__(self, id, username):  
        print("Creating new user...")
        time.sleep(3)      
        self.id = id
        self.username = username
        print(f"{self.username} has been created as user {self.id}")

user_1 = User("001","Angela")

user_2 = User("002", "Pedro")




