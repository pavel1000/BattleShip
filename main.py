from placement import ship_placement
from game import game_field
from view.form import Ui_Form

from net import net_window
from netGame import net_game_field
from net_placement import net_ship_placement

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
        self.start.theme_combo.setCurrentIndex(3)
        self.start.show()

        self.placement = ship_placement()
        self.game = game_field(self.placement.fields)

        self.start.nextWin.connect(self.placement.show)
        self.placement.back.connect(self.start.show)
        self.placement.nextWin.connect(self.game.show)
        self.game.closed.connect(self.start.show)
        self.game.closed.connect(self.newGameChanges)

        self.start.resizeSygnal.connect(self.resizeWindows)

        self.net = net_window()
        self.net_placement = net_ship_placement(self.start.type, self.net.ip)
        self.net_game = net_game_field(self.net_placement.fields, self.net_placement.connect, self.net_placement.turn)

        self.net.nextNetWin.connect(self.net_placement.show)
        self.net.nextNetServerWin.connect(self.net_placement.show)
        # self.net.pushBack(self.start.show)

        self.start.nextNetWin.connect(self.net.show)
        self.net_placement.back.connect(self.start.show)
        self.net_placement.nextWin.connect(self.net_game.show)
        self.net_game.closed.connect(self.start.show)
        self.net_game.closed.connect(self.newGameChanges)
    
    def resizeWindows(self, g):
        self.start.setGeometry(g)
        self.placement.setGeometry(g)
        self.game.setGeometry(g)
        self.net.setGeometry(g)
        self.net_placement.setGeometry(g)
        self.net_game.setGeometry(g)

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
    nextNetWin = pyqtSignal()

    def __init__(self):
        super(startWindow, self).__init__()
        self.type = None 
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.theme_combo = QComboBox(self)
        # При правке списка ниже необходимо изменять и файл "resources.qrc"
        # А затем выполнять "pyrcc5 resources.qrc -o resources_rc.py"
        self.theme_combo.addItems(['AMOLED', 'aqua', 'ConsoleStyle', 'Dark',
                                   'ElegantDark', 'MacOS', 'ManjaroMix',
                                   'MaterialDark', 'NeonButtons', 'Ubuntu'])

        self.ui.newSoloGame.clicked.connect(self.nextWindow)
        self.ui.newNetGame.clicked.connect(self.nextNetWindow)

    def nextWindow(self):
        self.close()
        self.type = 1
        self.nextWin.emit()
    
    def nextNetWindow(self):
        self.close()
        self.type = 0
        self.nextNetWin.emit()

    def positioning(self):
        x = self.width()//2 - self.ui.newSoloGame.width()//2
        y = self.height()//2 - self.ui.newSoloGame.height()//2
        self.ui.newSoloGame.setGeometry(x-120, y, self.ui.newSoloGame.width(), self.ui.newSoloGame.height())
        self.ui.newNetGame.setGeometry(x+120, y, self.ui.newNetGame.width(), self.ui.newNetGame.height())
        w, h = self.theme_combo.width(), self.theme_combo.height()
        x = self.width()*9//10 - w//2
        y = self.height()*9//10 - h//2
        self.theme_combo.setGeometry(x, y, w, h)

    def resizeEvent(self, event):
        '''Подгоняет размер элементов под размер экрана.'''
        self.positioning()
        self.resizeSygnal.emit(self.geometry())
        return super().resizeEvent(event)


if __name__ == '__main__':
    app = MainApp(sys.argv)
    sys.exit(app.exec_())
