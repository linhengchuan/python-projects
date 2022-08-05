import os
import sys
from PySide2.QtWidgets import (
    QMainWindow, QApplication, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QWidget, QLineEdit, QTextEdit
)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Encryptor/Decryptor")
        self.setGeometry(500, 500, 400, 300)
        
        hlayout = QHBoxLayout()
        
        vlayout_left = QVBoxLayout()
        vlayout_left.addWidget(QLabel("Input: "))
        self.input_box = QTextEdit()
        vlayout_left.addWidget(self.input_box)
        hlayout.addLayout(vlayout_left)
        
        vlayout_mid = QVBoxLayout()
        vlayout_mid.addStretch(1)
        self._btn_encrypt = QPushButton("Encrypt")
        self._btn_encrypt.clicked.connect(self._encrypt)
        self._btn_decrypt = QPushButton("Decrypt")
        self._btn_decrypt.clicked.connect(self._decrypt)
        vlayout_mid.addWidget(self._btn_encrypt)
        vlayout_mid.addWidget(self._btn_decrypt)
        vlayout_mid.addWidget(QLabel("Key(1 character): "))
        self.key_box = QLineEdit()
        self.key_box.setMaxLength(1)
        vlayout_mid.addWidget(self.key_box)
        vlayout_mid.addStretch(1)
        hlayout.addLayout(vlayout_mid)
        
        vlayout_right = QVBoxLayout()
        vlayout_right.addWidget(QLabel("Output: "))
        self.output_box = QTextEdit()
        vlayout_right.addWidget(self.output_box)
        hlayout.addLayout(vlayout_right)

        widget = QWidget()
        widget.setLayout(hlayout)
        self.setCentralWidget(widget)
        self.show()

    def _encrypt(self):
        text = self.input_box.toPlainText()
        key = self.key_box.displayText()
        if len(key)==0 or len(text)==0:
            self.output_box.setText(text)
        else:
            unicode_key = ord(key)
            new_text = ""
            for char in text:
                unicode_char = ord(char)
                new_text+= (chr(unicode_char+unicode_key))
            self.output_box.setText(new_text)
    
    def _decrypt(self):
        text = self.output_box.toPlainText()
        key = self.key_box.displayText()
        if len(key)==0 or len(text)==0:
            self.input_box.setText(text)
        else:
            unicode_key = ord(key)
            new_text = ""
            for char in text:
                if char==' ':
                    unicode_char = 160
                else:
                    unicode_char = ord(char)
                new_text+= (chr(unicode_char-unicode_key))
            self.input_box.setText(new_text)

if not QApplication.instance():
    app = QApplication(sys.argv)
else:
    app = QApplication.instance()
w = MainWindow()
app.exec_()