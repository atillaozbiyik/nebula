from astparser import AstParser
import platform
import sys
import os

from PyQt5.QtCore import Qt, QEvent, pyqtSignal
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QShortcut

from PyQt5.QtWidgets import QMainWindow, QMenu, QApplication, QFileSystemModel
from clang.cindex import CursorKind, SourceLocation
from ui_files.ui_nebula import Ui_MainWindow
# from LexerQsci import Editor
from tabClass import tabEditor
from embeddedTerminal import embterminal
from tools import debug
"""TODO
- add git
- add minimap
- add lexer
- add file tracker
=======
from LexerQsci import Editor
from tools import debug

TODO
- Save & CTRL+S!
- Auto code completion
- Ctrl-Z
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
- Variable refacor/rename
- File and project templates
- Move autocomplete source to clang from Qscintilla
"""

software_version = "0.1"
path_of_me = os.path.dirname(os.path.abspath(sys.argv[0]))


class MyWindowClass(QMainWindow, Ui_MainWindow):

    keybindings = [
                    (Qt.CTRL + Qt.Key_S     , "save"),
                    (Qt.CTRL + Qt.Key_Q     , "quit"),
                    (Qt.CTRL + Qt.Key_R     , "refresh_outline"),
                    (Qt.CTRL + Qt.Key_Space , "autocomplete"),
                    (Qt.Key_F1              , "testplace"),
    ]

    tabs = []

    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        super(MyWindowClass, self).__init__(parent)
        self.installEventFilter(self)
        self.setupUi(self)

        # self.QSciEditor = tabEditor(parent=self)
        # self.QSciEditor.setIndentationGuides(True)

        model = QFileSystemModel()
        model.setRootPath(path_of_me)


        self.label.setText(os.path.basename(path_of_me))
        self.treeView.setModel(model)
        self.treeView.setRootIndex(model.index(path_of_me))
        self.treeView.hideColumn(1)
        self.treeView.hideColumn(2)
        self.treeView.hideColumn(3)
        self.treeView.setHeaderHidden(True)
        self.treeView.doubleClicked.connect(self.tabHandler)

        self.terminal = embterminal(self.pageLayout)
        # self.process = QtCore.QProcess(self)
        # self.terminal = QtWidgets.QWidget(self)
        # self.pageLayout.addWidget(self.terminal)
        # self.process.start('xterm', ['-into', str(self.terminal.winId())])

        # self.page.setLayout(layout)

        # self.infoBox.resize(531,0)
        # self.pageLayout
        self.tabWidget.tabCloseRequested.connect(self.delTab)
        self.shortcuts = []
        for key in self.keybindings:
            self.shortcuts.append (QShortcut(self))
            self.shortcuts[-1].setKey(key[0])
            self.shortcuts[-1].activated.connect(getattr(self, key[1]))

        self.treeOutline.title = "Outline View"  # Probably treeOutline will be a discrete class soon..
        self.treeOutline.setContextMenuPolicy(Qt.CustomContextMenu)
        self.treeOutline.customContextMenuRequested.connect(self.openMenu)
        self.treeOutline.clicked.connect(self.outline_clicked)
        self.cleanButton.clicked.connect(self.clean)
        # self.gridLayout.addWidget(self.QSciEditor)
        self.ast = AstParser()
        self.show()

    def createTab(self, filename, content):
        newTab = tabEditor(parent=self.tabWidget, filepath=filename, content=content)
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
                        self.createTab(file_path, currentFile.read())
                        self.tabWidget.setCurrentIndex(len(self.tabs)-1)
                        self.refresh_outline()
            except Exception as e:
                print(e)
        else:
            self.tabWidget.setCurrentIndex(index)


    def save(self):
        file = open(self.tabs[self.tabWidget.currentIndex()].QSciEditor.text().filename, "w")
        file.write(self.tabs[self.tabWidget.currentIndex()].QSciEditor.text())
        file.close()
        self.refresh_outline()
        debug(self.tabs[self.tabWidget.currentIndex()].QSciEditor.text().filename + " is saved..." )

    def quit(self):
        debug("quitting..." )
        app.quit()

    def openMenu(self, position):
        menu = QMenu()
        menu.addAction(self.tr("Go to"))
        menu.exec_(self.treeOutline.viewport().mapToGlobal(position))

    def test(self, signal):
        file_path = self.treeView.model().filePath(signal)
        self.self.tabs[self.tabWidget.currentIndex()].QSciEditor.filename = file_path  # Soon will be used to save to that file.
        # try:
        if os.path.isfile(file_path):
            with open(file_path, 'r+') as currentFile:
                self.self.tabs[self.tabWidget.currentIndex()].QSciEditor.setText(currentFile.read())
                self.refresh_outline()

    def refresh_outline(self):
        kinds = []
        kinds.append(CursorKind.FUNCTION_DECL)
        kinds.append(CursorKind.VAR_DECL)
        kinds.append(CursorKind.DECL_REF_EXPR)
        kinds.append(CursorKind.COMPOUND_STMT)
        # kinds.append(CursorKind.STRUCT_DECL)
        kinds.append(CursorKind.FIELD_DECL)

        outline = self.ast.get_outline(self.tabs[self.tabWidget.currentIndex()]._filepath, kinds)
        self.treeOutline.setModel(outline)


                # except Exception as e:
        #     print(e)

    def outline_clicked(self, index):
        loc = (self.treeOutline.model().itemFromIndex(index).location)
        debug("Node Location: " + str(loc.line) + "," + str(loc.column))
        self.tabs[self.tabWidget.currentIndex()].QSciEditor.setCursorPosition(loc.line - 1, loc.column - 1)
        self.tabs[self.tabWidget.currentIndex()].QSciEditor.ensureLineVisible(loc.line - 1)
        self.tabs[self.tabWidget.currentIndex()].QSciEditor.ensureCursorVisible()
        self.tabs[self.tabWidget.currentIndex()].QSciEditor.setFocus()

    def clean(self, signal):
        debug("clean...")

    def autocomplete(self):
        self.tabs[self.tabWidget.currentIndex()].QSciEditor.autoCompleteFromAll()
        debug("autocompleted...")

    def testplace(self):
        debug("This is for testing purposes...")

if __name__ == "__main__":
    app = QApplication(sys.argv)
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
