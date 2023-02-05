#import components 
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

