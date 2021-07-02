from placement import ship_placement
from game import game_field
from view.form import Ui_Form

import os
import sys
import resources_rc
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QComboBox
from PyQt5.QtCore import QRect, pyqtSignal, QFile, QTextStream


class MainApp(QApplication):
    def __init__(self, argv):
        super().__init__(argv)

        self.start = startWindow()
        self.start.theme_combo.activated[str].connect(self.setTheme)
        self.setTheme('Dark')
        self.start.show()

        self.placement = ship_placement()
        self.game = game_field(self.placement.fields)

        self.start.nextWin.connect(self.placement.show)
        self.placement.back.connect(self.start.show)
        self.placement.nextWin.connect(self.game.show)
        self.game.closed.connect(self.start.show)
        self.game.closed.connect(self.newGameChanges)

        self.start.resizeSygnal.connect(self.resizeWindows)
    
    def resizeWindows(self, g):
        self.start.setGeometry(g)
        self.placement.setGeometry(g)
        self.game.setGeometry(g)

    def newGameChanges(self):
        self.placement.returnShips()
        self.game.resetFields()
    
    def setTheme(self, theme):
        if os.path.exists(theme):
            file = QFile(theme)
        else:
            file = QFile(':/qss/'+theme+'.qss')
        file.open(QFile.ReadOnly | QFile.Text)
        style = QTextStream(file)
        self.setStyleSheet(style.readAll())


class startWindow(QWidget):
    nextWin = pyqtSignal()
    resizeSygnal = pyqtSignal(QRect)
    theme = pyqtSignal(str)

    def __init__(self):
        super(startWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.theme_combo = QComboBox(self)
        # При правке списка ниже необходимо изменять и файл "resources.qrc"
        # А затем выполнять "pyrcc5 resources.qrc -o resources_rc.py"
        self.theme_combo.addItems(['AMOLED', 'aqua', 'ConsoleStyle', 'Dark',
                                   'ElegantDark', 'MacOS', 'ManjaroMix',
                                   'MaterialDark', 'NeonButtons', 'Ubuntu'])
        self.theme_combo.setCurrentIndex(3)

        self.ui.pushButton.clicked.connect(self.nextWindow)

    def nextWindow(self):
        self.close()
        self.nextWin.emit()

    def positioning(self):
        x = self.width()//2 - self.ui.pushButton.width()//2
        y = self.height()//2 - self.ui.pushButton.height()//2
        self.ui.pushButton.setGeometry(x, y, self.ui.pushButton.width(), self.ui.pushButton.height())
        w, h = self.theme_combo.width(), self.theme_combo.height()
        x = self.width()*0.9 - w//2
        y = self.height()*0.9 - h//2
        self.theme_combo.setGeometry(x, y, w, h)

    def resizeEvent(self, event):
        '''Подгоняет размер элементов под размер экрана.'''
        self.positioning()
        self.resizeSygnal.emit(self.geometry())
        return super().resizeEvent(event)


if __name__ == '__main__':
    app = MainApp(sys.argv)
    sys.exit(app.exec_())
