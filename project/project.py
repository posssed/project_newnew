import sys
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QLinearGradient, QBrush

#app = QApplication([])
#win = QWidget()
#win.resize(500, 500)
#win.setWindowTitle("AITour Agency")



class App(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('project.ui', self)
        self.LONButton.clicked.connect(self.london)
        self.HawaiButton.clicked.connect(self.havaii)
        self.KyivButton.clicked.connect(self.kyiv)
        self.LAButton.clicked.connect(self.los_A)
        self.CarrButton.clicked.connect(self.caribbean)

    def london(self):
        self.label.setPixmap(QPixmap('london.jpg'))
        self.label_2.setText("Ло́ндон — столиця Англії та Сполученого Королівства, розташована на річці\n Темза. Середмістя Лондона є фінансовим і комерційним центром Сполученого Королівства Великої Британії та Північної Ірландії.")

    def havaii(self):
        self.label.setPixmap(QPixmap('Hawaii.jpg'))

    def kyiv(self):
        self.label.setPixmap(QPixmap('download.jpg'))

    def los_A(self):
        self.label.setPixmap(QPixmap('LA.jpg'))

    def caribbean(self):
        self.label.setPixmap(QPixmap('caribbean.jpg'))
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec())
