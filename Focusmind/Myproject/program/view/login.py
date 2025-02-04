import os
import sys


#from program.view.sign_up import UI_signup_window
#from Myproject.PROGRAM.view.MainWindow import UI_main_window(from)
#from program.view.MainWindow import UI_main_window(to)
#from Myproject.PROGRAM.controller.controller import Controller
# self.Ui_main_window.signal_object.connect(self, show)
#self.UI_singup_window = UI_signup_window(self)
#Ibl_signup









sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..','..')))

from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
#from Myproject.program.view.login import UI_signup_window
#from program.view.signup import UI_signup_window  # Adjust to correct location
from program.view.sign_up import UI_signup_window

#from Myproject.PROGRAM.view.MainWindow import UI_main_window
#from program.view.MainWindow import UI_main_window(from)
from program.view.main_window import UI_main_window #(to)

from program.controller.controller import Controller #(to)
#from Myproject.PROGRAM.controller.controller import Controller(from)



class UI_login_window(QMainWindow):
    def __init__(self, parent =None):
        super(UI_login_window, self).__init__(parent)
        uic.loadUi(os.path.join(os.path.dirname(__file__), "ui_files", "login_page.ui"), self)
        self.controller= Controller()
        
        self.btn_login = self.findChild(QPushButton, "btn_login")
        self.txt_user_id = self.findChild(QLineEdit, "line_edit_user_name")
        self.txt_password = self.findChild(QLineEdit, "line_edit_password")
        self.lbl_wrong_input = self.findChild(QLabel, "lbl_wrong_credentials")
        self.Ibl_signup = self.findChild(QLabel, "Ibl_signup")

        self.btn_login.clicked.connect(self.btn_login_clicked)
        #self.lbl_signup.mousePressEvent = self.1bl_signup_clicked
        self.Ibl_signup.mousePressEvent = self.lbl_signup_clicked  # Correct method name


        self.show()
    
    def btn_login_clicked(self):
        self.wrong_inputs = False
        self.check_input()
        if not self.wrong_inputs: 
            self.UI_main_window = UI_main_window(self, self.user_id) 
            self.Ui_main_window.signal_object.connect(self,show)
            # self.Ui_main_window.signal_object.connect(self, show)(from)
            self.UI_main_window.signal_object.connect(self.show) # (to)
 
            self.clear_window() 
            self.close() 
            self.UI_main_window.show()

 

   
    def check_input(self):
        self.get_window_values() 
        forbidden_symbols = ["'" ,'"', ";" ,"--", "/*", "*/", "#"] 
        if any(symbol in self.user_id for symbol in forbidden_symbols): 
            self.lbl_wrong_input.setText("No injection symbols allowed") 
            self.wrong_inputs = True 
        elif any(symbol in self.password for symbol in forbidden_symbols): 
            self.lbl_wrong_input.setText("No injection symbols allowed") 
            self.wrong_inputs = True 
        if not self.controller.authenticate_user(self.user_id, self.password): 
            self.lbl_wrong_input.setText("Wrong credentials") 
            self.wrong_inputs = True 

    def get_window_values(self):
        self.user_id = self.txt_user_id.text()
        self.password = self.txt_password.text()
        

    def clear_window(self): 
        self.txt_user_id.clear() 
        self.txt_password.clear() 
        self.lbl_wrong_input.setText("")

    def lbl_signup_clicked(self, event=None): # Accept event for mousePressEvent 
        #self.UI_singup_window = UI_signup_window(self)
        self.UI_signup_window = UI_signup_window(self)
 
        self.UI_singup_window.signal_object.connect(self.show) 
        self.clear_window() 
        self.close() 
        self.UI_singup_window.show()

    
    