# import sys 
# import os 
# sys.path. insert(0, os.path.abspath(os. path.join(os.path.dirname(__file__), '..','..')))
# from PyQt5.QtWidgets import *
# from PyQt5 import uic 
# from PyQt5.QtCore import *
# from Myproject.program.controller.controller import Controller

# class UI_signup_window(QMainWindow): 
#     signal_object = pyqtSignal()
#     def __init__(self, parent=None): 
#         super(UI_signup_window, self).__init__(parent) 
#         uic.loadUi(os.path.join(os.path.dirname(__file__), "ui_files" ,"signup_page.ui"), self)
        
#         self.controller = Controller()
#         self.btn_cancel = self.findChild(QPushButton, "btn_cancel") 
#         self.btn_signup = self.findChild(QPushButton, "btn_signup") 
#         self.txt_user_id =self.findChild(QLineEdit, "txt user_id") 
#         self.txt_password= self.findChild(QLineEdit, "txt_password") 
#         self.txt_admin_code =self.findChild(QLineEdit, "txt_admin_code") 
#         self.lbl_unavailable_user_id = self.findChild(QLabel, "lbl_unavailable user_id") 
#         self.lbl_unauthorized_password = self.findChild(QLabel, "1bl_unauthorized_password") 
#         self.lbl_wrong_admin_code = self.findChild(QLabel, "lbl. wrong_admin_code") 
#         self.btn_cancel.clicked.connect(self.btn_cancel_clicked) 
#         self.btn_signup.clicked.connect(self.btn_signup_clicked)



#     def btn_cancel_clicked(self):
#         self.clear_window() 
#         self.signal_object.emit() 
#         self.close() 
        
#     def btn_signup_clicked(self): 
#         self.wrong_inputs = False 
#         self.check_input() 
#         if not self.wrong_inputs: 
#             if self.admin_code.strip() != '': 
#              self.controller.insert_new_user(self.user_id, self.password, self.admin_code)
#             else:
#                 self.controller.insert_new_user(self.user_id, self.password)
#             self.clear_window() 
#             self.signal_object.emit() 
#             self.close()

#     def get_window_values(self): 
#         self.user_id = self.txt_user_id.text () 
#         self.password = self.txt_password.text() 
#         self.admin_code = self.txt_admin_code.text()

#     def check_input (self): 
#         self.get_window_valves() 
#         forbidden_symbols = ["'", '"', ";", ";", "/*", "*/", "#"] 
#         if any(symbol in self.user_id for symbol in forbidden_symbols): 
#             self.lbl_unavailable_user_id.setText("No injection symbols allowed") 
#             self.wrong_inputs = True 
#         if any(symbol in self.password for symbol in forbidden_symbols): 
#             self.lbl_unauthorized_password.setText("No injection symbols allowed") 
#             self.wrong_inputs = True 
#         if any(symbol in self.admin_code for symbol in forbidden_symbols): 
#             self.lbl_wrong_admin_code.setText("No Injection syabols allowed")
#             self.wrong_inputs= True
#         if self.controller.get_user_id(self.user_id) is not None: 
#             self.lbl_unavailable_user_id.setText("User ID already exist") 
#             self.wrong_inputs = True 
#         if self.user_id.strip() == "": 
#             self.lbl_unavailable_user_id.setText("User ID must not be emptyl") 
#             self.wronge_inputs = True 
#         if self.password.strip() == "": 
#            self.lbl_unauthorized_password.setText("Password aust not be empty!")
#            self.wrong_inputs = True
#         if self.admin_code.strip() != "":
#            if not self.controller.check_admin_code(self.admin_code):
#                self.lbl_wrong_admin_code.setText("wrong admin code")
#                self.wrong_inputs = True

#     def clear_window(self): 
#         self.txt_user_id.clear() 
#         self.txt_password.clear() 
#         self.txt_admin_code.clear() 
#         self.lbl_unavailable_user_id.setText("") 
#         self.lbl_unauthorized_password.setText("") 
#         self.lbl_wrong_admin_code.setText("")

#_______________________________________________________________________________________-


import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal

from program.controller.controller import Controller  # Fixed import path

class UI_signup_window(QMainWindow):
    signal_object = pyqtSignal()

    def __init__(self, parent=None):
        super(UI_signup_window, self).__init__(parent)
        uic.loadUi(os.path.join(os.path.dirname(__file__), "ui_files", "signup_page.ui"), self)

        self.controller = Controller()

        # Corrected UI element names
        self.btn_cancel = self.findChild(QPushButton, "btn_cancel")
        self.btn_signup = self.findChild(QPushButton, "btn_signup")
        self.txt_user_id = self.findChild(QLineEdit, "txt_user_id")  # Fixed space issue
        self.txt_password = self.findChild(QLineEdit, "txt_password")
        self.txt_admin_code = self.findChild(QLineEdit, "txt_admin_code")

        self.lbl_unavailable_user_id = self.findChild(QLabel, "lbl_unavailable_user_id")  # Fixed spaces
        self.lbl_unauthorized_password = self.findChild(QLabel, "lbl_unauthorized_password")  # Fixed typo
        self.lbl_wrong_admin_code = self.findChild(QLabel, "lbl_wrong_admin_code")  # Fixed dot issue

        # Ensure UI elements exist before connecting signals
        if self.btn_cancel:
            self.btn_cancel.clicked.connect(self.btn_cancel_clicked)
        else:
            print("❌ ERROR: QPushButton 'btn_cancel' not found in UI file!")

        if self.btn_signup:
            self.btn_signup.clicked.connect(self.btn_signup_clicked)
        else:
            print("❌ ERROR: QPushButton 'btn_signup' not found in UI file!")

    def btn_cancel_clicked(self):
        self.clear_window()
        self.signal_object.emit()
        self.close()

    def btn_signup_clicked(self):
        self.wrong_inputs = False
        self.check_input()

        if not self.wrong_inputs:
            if self.admin_code.strip() != '':
                self.controller.insert_new_user(self.user_id, self.password, self.admin_code)
            else:
                self.controller.insert_new_user(self.user_id, self.password)

            self.clear_window()
            self.signal_object.emit()
            self.close()

    def get_window_values(self):
        """Retrieve values from input fields."""
        self.user_id = self.txt_user_id.text()
        self.password = self.txt_password.text()
        self.admin_code = self.txt_admin_code.text()

    def check_input(self):
        """Validate input fields."""
        self.get_window_values()
        forbidden_symbols = ["'", '"', ";", "--", "/*", "*/", "#"]

        # Validate user_id
        if any(symbol in self.user_id for symbol in forbidden_symbols):
            self.lbl_unavailable_user_id.setText("No injection symbols allowed")
            self.wrong_inputs = True
        if self.user_id.strip() == "":
            self.lbl_unavailable_user_id.setText("User ID must not be empty!")
            self.wrong_inputs = True
        if self.controller.get_user_id(self.user_id) is not None:
            self.lbl_unavailable_user_id.setText("User ID already exists")
            self.wrong_inputs = True

        # Validate password
        if any(symbol in self.password for symbol in forbidden_symbols):
            self.lbl_unauthorized_password.setText("No injection symbols allowed")
            self.wrong_inputs = True
        if self.password.strip() == "":
            self.lbl_unauthorized_password.setText("Password must not be empty!")
            self.wrong_inputs = True

        # Validate admin_code
        if self.admin_code.strip() != "":
            if any(symbol in self.admin_code for symbol in forbidden_symbols):
                self.lbl_wrong_admin_code.setText("No injection symbols allowed")
                self.wrong_inputs = True
            if not self.controller.check_admin_code(self.admin_code):
                self.lbl_wrong_admin_code.setText("Wrong admin code")
                self.wrong_inputs = True

    def clear_window(self):
        """Clear all input fields and reset labels."""
        self.txt_user_id.clear()
        self.txt_password.clear()
        self.txt_admin_code.clear()
        self.lbl_unavailable_user_id.setText("")
        self.lbl_unauthorized_password.setText("")
        self.lbl_wrong_admin_code.setText("")

    
