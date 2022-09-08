import random
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QSize
import translators as ts

kz= str(random.choice(open("kz.txt").read().split()))
translation=(ts.google(kz, from_language='kk',to_language='en'))
#add count that saves whether the program has been run before


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(300, 200))
        self.setWindowTitle("Kazakh Word of the Day")

        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        pybutton = QPushButton(kz, self)
        pybutton.clicked.connect(self.clickMethod)
        pybutton.resize(200,64)
        pybutton.move(50, 50)

    def clickMethod(self):

        QMessageBox.about(self, "Translation", translation)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )
