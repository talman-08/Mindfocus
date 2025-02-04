import os 
import sys 

sys.path. insert(0, os.path.abspath(os. path.join(os.path.dirname(__file__), '..','..','..')))
import pyrebase


class Read_db:
    def __init__(self):
        config= {  "apiKey": "AIzaSyBM1PLSe5YPR8Ma2NsxMWCdY5tgC8evRew",
                   "authDomain": "myproject-c16a2.firebaseapp.com",
                   "databaseURL": "https://myproject-c16a2-default-rtdb.europe-west1.firebasedatabase.app",
                   "projectId": "myproject-c16a2",
                   "storageBucket": "myproject-c16a2.firebasestorage.app",
                  " messagingSenderId": "921771611395",
                   "appId": "1:921771611395:web:83c75569b3719405e60536",
                  " measurementId": "G-TB0ETKG4LY"}
        firebase = pyrebase.initialize_app(config)
        self.datgbase = firebase.database()

    def authenticate_user(self, user_id, password): 
        users = self.database.child("Users").get() 
        if users.val() is not None: 
            for uid, user_info in users.val().items(): 
                if uid == user_id: 
                    if user_info["Password"] == password : 
                        return True 
        return False 

    def get_user_id(self, user_id): 
        users = self.database.child("Users").get() 
        if users.val() is not None:  
            for uid, user_info in users.val().items(): 
                if uid == user_id: 
                    return uid, user_info 
        return None
    
    def get_password(self, user_id): 
        user_data = self.database.child("Users").child(user_id).get() 
        if user_data.val() is not None: 
           return user_data.val().get("Password") 
        return None
    