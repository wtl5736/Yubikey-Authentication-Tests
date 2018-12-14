"""
Name: Yubikey_Implementation_Demo.py
Author: Wesley Lee - wtl5736@rit.edu
Assignment: Authentication Project CSEC-472
Date Created: 11-28-2018
Date Modified: 12-05-2018

Description:
	Yubikey implementation demo with a GUI. Allows a user to enter a 'Client ID'
	and OTP to validate the Yubikey.

"""

import os
import sys
import platform
import yubico_client
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


# GUI Class
class App(QDialog):
	# Global Variables
	clientID = ""

	# Initializes the size of the GUI box
	def __init__(self):
		super().__init__()
		self.title = 'Yubikey Implementation Demo'
		self.width = 350
		self.height = 125
		self.winWidth = 300

		# Windows GUI Flags
		self.setWindowFlags(
			Qt.Window |
			Qt.CustomizeWindowHint |
			Qt.WindowTitleHint |
			Qt.WindowCloseButtonHint
		)

		self.initUI()

	# Initializes the GUI
	def initUI(self):
		self.setWindowTitle(self.title)

		# Different GUI window size based on OS
		if platform.system() == 'Windows':
			self.setFixedSize(self.winWidth, self.height)
		else:
			self.setFixedSize(self.width, self.height)

		self.createGridLayout()

		# Bold Font
		myFont = QFont()
		myFont.setBold(True)
		self.setAutoFillBackground(True)
		p = self.palette()
		p.setColor(self.backgroundRole(), Qt.black)
		self.setPalette(p)

		# Action Notification
		self.notification = QLabel(self)
		self.notification.setText("")
		self.notification.setAlignment(Qt.AlignCenter)

		# Different notification alignment based on OS
		if platform.system() == "Windows":
			self.notification.resize(275, 35)
		else:
			self.notification.resize(330, 35)

		self.notification.setFont(myFont)

		# Grid Box
		windowLayout = QVBoxLayout()
		windowLayout.addWidget(self.horizontalGroupBox)
		self.setLayout(windowLayout)
		self.show()

	# Grid of Buttons
	def createGridLayout(self):
		self.horizontalGroupBox = QGroupBox("")
		self.horizontalGroupBox.setStyleSheet("QGroupBox { border: 1px}")
		layout = QGridLayout()

		# Client ID textbox
		self.clientID_tbox = QLineEdit(self)
		self.clientID_tbox.setPlaceholderText("Enter Client ID")
		self.clientID_tbox.setEchoMode(QLineEdit.Normal)

		# Yubikey OTP textbox
		self.OTP_tbox = QLineEdit(self)
		self.OTP_tbox.setPlaceholderText("Enter Yubikey OTP")
		self.OTP_tbox.setEchoMode(QLineEdit.Password)

		# Yubikey OTP Validate Button
		self.validate_button = QPushButton("Validate", self)
		self.validate_button.clicked.connect(lambda:self.validateYubikey())
		self.validate_button.setStyleSheet('QPushButton{color: white; \
			font-size: 12px; background-color: #1d1d1d; border-radius: 5px; \
			padding: 5px; text-align: center;} \n QPushButton:hover{color: #ff0000;}')

		# Show OTP_Button
		self.showOTP_button = QPushButton('Show OTP', self)
		self.showOTP_button.setCheckable(True)
		self.showOTP_button.clicked.connect(lambda:self.on_click_showOTP(self.showOTP_button))
		self.showOTP_button.setStyleSheet('QPushButton{color: white; \
			font-size: 12px; background-color: #1d1d1d; border-radius: 5px; \
			padding: 5px; text-align: center;} \n QPushButton:hover{color: #ff0000;}')

		# Sets grid
		layout.addWidget(self.clientID_tbox, 0, 1)
		layout.addWidget(self.OTP_tbox, 0, 2)
		layout.addWidget(self.validate_button, 1, 1)
		layout.addWidget(self.showOTP_button, 1, 2)

		self.horizontalGroupBox.setLayout(layout)

	# Validates Yubi OTP w/ Yubico Validation servers
	def validateYubikey(self):
		client_id = self.clientID_tbox.text()
		client_key = 'ENTER YUBIKEY API KEY'
		otp = self.OTP_tbox.text()

		try:
			clientVer = yubico_client.Yubico(client_id=client_id, \
				key=client_key)
			self.notification.setStyleSheet('color: rgb(24,240,24);')
			self.notification.setText("OTP Verification Successful!")
		except:
			self.notification.setStyleSheet('color: red')
			self.notification.setText("OTP Verification Failed!")

	# Shows the password entered
	def on_click_showOTP(self, b):
		#print(b.isChecked())
		if b.isChecked() == True:
			self.OTP_tbox.setEchoMode(QLineEdit.Normal)
		else:
			self.OTP_tbox.setEchoMode(QLineEdit.Password)

# Runs GUI
def gui_main():
	app = QApplication(sys.argv)
	run = App()
	sys.exit(app.exec_())

if __name__ == '__main__':
	gui_main()
