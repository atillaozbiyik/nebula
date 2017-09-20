import platform

from astparser import AstParser

if platform.python_version().startswith("2."):
    print ("Only Python 3.x is supported!")
    exit()


import sys
import os
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QMenu, QApplication, QFileSystemModel


from ui_files.ui_nebula import Ui_MainWindow
from LexerQsci import Editor


"""
TODO
- Save & CTRL+S!
- Auto code completion
- Compiler integration
    Compiler parameters
    Makefile generator
    Import Makefile?
    Import other IDE project files
- Debugger integration
    GDB server integration
    Breakpoints
    Stop on change
    Variable view
    Expression evaluation
- Block selection
- Customisation of almost everything :
    Colors, fonts, icons, themes?,
    Custom scripts/Buttons, external plugin support by python scripting?)
- Version Control support
- Minimap
- Lexer/AST
- Add file tracker
- Automatic update
- Program Flasher
- Linter
- Simple GUI Designer ?
"""

software_version = "0.1"
path_of_me = os.path.dirname(os.path.abspath(sys.argv[0]))


class MyWindowClass(QMainWindow, Ui_MainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        model = QFileSystemModel()
        model.setRootPath(path_of_me)
        self.label.setText(path_of_me)
        self.treeView.setModel(model)
        self.treeView.setRootIndex(model.index(path_of_me))
        self.treeView.hideColumn(1)
        self.treeView.hideColumn(2)
        self.treeView.hideColumn(3)
        self.treeView.doubleClicked.connect(self.test)

        self.treeOutline.title = "Outline View"  # Probably treeOutline will be a discrete class soon..
        self.treeOutline.setContextMenuPolicy(Qt.CustomContextMenu)
        self.treeOutline.customContextMenuRequested.connect(self.openMenu)

        # outline_data = [("Alice", [("Keys", []), ("Purse", [("Cellphone", [])])]),
        #                 ("Bob", [("Wallet", [("Credit card", []), ("Money", [])])])]
        #

        self.pushButton_2.clicked.connect(self.clean)
        self.QSciEditor = Editor()
        self.gridLayout.addWidget(self.QSciEditor)
        self.ast = AstParser()
        self.show()

    def addItems(self, parent, tunit):
        for child in tunit.get_children():
            if child.spelling != None:
                item = QStandardItem(child.spelling)
            else:
                item = QStandardItem(str(child.kind))

            item.setEditable(False)
            parent.appendRow(item)
            if child.get_children() is not None:
                self.addItems(item, child)

    # def addItems(self, parent, elements):
    #
    #     for text, children in elements:
    #         item = QStandardItem(text)
    #         item.setEditable(False)
    #         parent.appendRow(item)
    #         if children:
    #             self.addItems(item, children)

    def openMenu(self, position):
        indexes = self.treeOutline.selectedIndexes()
        menu = QMenu()
        menu.addAction(self.tr("Go to"))

        menu.exec_(self.treeOutline.viewport().mapToGlobal(position))

    def test(self, signal):
        file_path = self.treeView.model().filePath(signal)

        # try:
        if os.path.isfile(file_path):
            with open(file_path, 'r+') as currentFile:
                self.QSciEditor.setText(currentFile.read())

                self.model = QStandardItemModel()
                self.treeOutline.setModel(self.model)

                outline = self.ast.get_outline(file_path)

                root_items = [c for c in outline.cursor.get_children()]
                for r in root_items:
                    #
                    # if r.kind == Cursor.FUNCTION_DECL:
                    #     if r.children:
                    #          pass

                    if r.spelling != None:
                        item = QStandardItem(r.spelling)
                    else:
                        item = QStandardItem(str(r.kind))

                    item.setEditable(False)
                    self.model.appendRow(item)
                    self.addItems(self.model, r)

        # except Exception as e:
        #     print(e)

    def clean(self, signal):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
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
