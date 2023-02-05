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

app=QApplication(sys.argv)

class ButtonHolder(QMainWindow):
     def __init__ (self):
        super().__init__()
        self.setWindowTitle("Button Holder App")
        button = QPushButton("Press Me!")
        #Set up the button as our central widget
        self.setCentralWidget(button)
 


window=ButtonHolder()
window.show()
app.exec()