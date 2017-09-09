import platform
import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qsci import QsciScintilla, QsciLexerPython
from ui_nebula import Ui_MainWindow

"""TODO 
- add git
- add minimap
- add lexer
- add file tracker
"""

software_version = "0.1"
path_of_me = os.path.dirname(os.path.abspath(sys.argv[0]))

class MyWindowClass(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        model = QtWidgets.QFileSystemModel()
        model.setRootPath(path_of_me)
        self.treeView.setModel(model)
        self.treeView.setRootIndex(model.index(path_of_me))
        self.treeView.hideColumn(1)
        self.treeView.hideColumn(2)
        self.treeView.hideColumn(3)
        self.treeView.doubleClicked.connect(self.test)
        self.show()

    def test(self, signal):
        file_path=self.model().filePath(signal)
        print(file_path)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    myWindow = MyWindowClass()
    myWindow.setWindowTitle("NeBULA for " +
                            platform.system() + " v." + software_version)


    # Start the window centered in screen
    # print (app.desktop().primaryScreen())
    screenGeometry = app.desktop().screenGeometry(0)
    x = (screenGeometry.width() - myWindow.width()) / 2
    y = (screenGeometry.height() - myWindow.height()) / 2
    myWindow.move(x, y)

    myWindow.setVisible(True)

    app_exec_code = app.exec_()
    app.quit()
