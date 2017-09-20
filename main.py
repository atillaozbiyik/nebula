import platform

if platform.python_version().startswith("2."):
    print ("Only Python 3.x is supported!")
    exit()


import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from ui_files.ui_nebula import Ui_MainWindow
# from LexerQsci import Editor
from tabClass import tabEditor
"""TODO
- add git
- add minimap
- add lexer
- add file tracker
"""


software_version = "0.1"
path_of_me = os.path.dirname(os.path.abspath(sys.argv[0]))


class MyWindowClass(QtWidgets.QMainWindow, Ui_MainWindow):

    tabs = []

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        model = QtWidgets.QFileSystemModel()
        model.setRootPath(path_of_me)


        self.label.setText(os.path.basename(path_of_me))
        self.treeView.setModel(model)
        self.treeView.setRootIndex(model.index(path_of_me))
        self.treeView.hideColumn(1)
        self.treeView.hideColumn(2)
        self.treeView.hideColumn(3)
        self.treeView.setHeaderHidden(True)
        self.treeView.doubleClicked.connect(self.tabHandler)

        # self.infoBox.resize(531,0)

        self.tabWidget.tabCloseRequested.connect(self.delTab)

        self.show()

    def createTab(self, filename, content):
        newTab = tabEditor(parent=self.tabWidget, filename=filename, content=content)
        self.tabs.append(newTab)

    def delTab(self, index):
        widget = self.tabWidget.widget(index)
        if widget is not None:
            widget.deleteLater()
        self.tabWidget.removeTab(index)
        self.tabs[index].deleteLater()
        del(self.tabs[index])

    def checkFileTabIsOpen(self, filename):
        returnText = "False"
        for i in range(0,len(self.tabs)):
            tabText = str(self.tabWidget.tabText(i)).replace("&","")
            # print(tabText)
            # print(filename)
            if tabText == filename:
                # print("Found file")
                returnText = "True"
                return i,returnText
        return 0, returnText

    def tabHandler(self, signal):
        file_path = self.treeView.model().filePath(signal)
        filename = file_path.split("/")[-1]
        index, result = self.checkFileTabIsOpen(filename)
        if result == "False":
            try:
                if os.path.isfile(file_path):
                    with open(file_path, 'r+') as currentFile:
                        self.createTab(filename, currentFile.read())
                        self.tabWidget.setCurrentIndex(len(self.tabs)-1)
            except Exception as e:
                print(e)
        else:
            self.tabWidget.setCurrentIndex(index)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    myWindow = MyWindowClass()
    myWindow.setWindowTitle("CWAG for " +
                            platform.system() + " v." + software_version)

    myWindow.runButton.clicked.connect(lambda: myWindow.checkFileTabIsOpen("main.py"))

    # Start the window centered in screen
    # print (app.desktop().primaryScreen())
    screenGeometry = app.desktop().screenGeometry(0)
    x = (screenGeometry.width() - myWindow.width()) / 2
    y = (screenGeometry.height() - myWindow.height()) / 2
    myWindow.move(x, y)

    myWindow.setVisible(True)

    app_exec_code = app.exec_()
    app.quit()
