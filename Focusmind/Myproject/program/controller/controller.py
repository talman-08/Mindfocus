import os
import sys
#from program.model.write_db import Write_db(to)
#from Myproject.PROGRAM.model.read_db import Read_db (from)


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),'..', '..','..')))


#from Myproject.PROGRAM.model.write_db import Write_db
from program.model.write_db import Write_db

#from Myproject.PROGRAM.model.read_db import Read_db
from program.model.read_db import Read_db




class Controller:
    def __init__(self)-> None:
        self.write_db = Write_db()
        self.read_db = Read_db()

    def authenticate_user(self, user_id, password): 
        return self.read_db.authenticate_user(user_id, password)
    def get_user_id(self, user_id):
        return self.read_db.get_user_id(user_id)
    def get_password(self, user_id): 
        return self.read_db.get_password(user_id)
    
    def insert_new_user(self, user_id, password, admin =False): 
        self.write_db.insert_new_user(user_id, password, admin)
    def change_user_id(self, user_id, user_id_new):
        self.write_db.change_user_id(user_id, user_id_new)
    def change_password(self, user_id, password):
        self.write_db.change_password(user_id, password)
        