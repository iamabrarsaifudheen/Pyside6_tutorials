'''#import components 
from PySide6.QtWidgets import QApplication,QMainWindow,QPushButton
#processing command line
import sys
app=QApplication(sys.argv)

window= QMainWindow()
window.setWindowTitle("Our Window Title")

button=QPushButton()
button.setText("Press me")


window.setCentralWidget(button)

window.show()
app.exec()

'''

import sys
from PySide6.QtWidgets import QApplication,QMainWindow,QPushButton
from button_holder import ButtonHolder
app=QApplication(sys.argv)
def button_clicked():
    print("You clicked the button")

button=QPushButton("Press Me")

button.clicked.connect(button_clicked)


button.show()
app.exec()
