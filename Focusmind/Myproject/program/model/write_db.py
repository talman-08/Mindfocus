import os 
import sys 

sys.path. insert(0, os.path.abspath(os. path.join(os.path.dirname(__file__), '..','..', '..')))
import pyrebase



class Write_db:
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

    def insert_new_user(self, user_id, password, admin): 
        user_info = {"password" : password, " Admin": admin}
        self.database.child("Users").child(user_id).set(user_info)

    def change_usor_id(self, old_user_id, new_user_id): 
        user_data = self.database.child("users").child(old_user_id).get() 
        if user_data.val() is not None: 
            self.database.child("Users").child(new_user_id).set(user_data.val()) 
            self.database.child("Users").child(old_user_id).remove()

    def change_password (self, user_id, password):
        self.database.child("Users").child(user_id).update({"Password":password})