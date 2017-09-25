from astparser import AstParser
import platform
import sys
import os

from PyQt5.QtCore import Qt, QEvent, pyqtSignal
from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QShortcut

from PyQt5.QtWidgets import QMainWindow, QMenu, QApplication, QFileSystemModel
from clang.cindex import CursorKind, SourceLocation
from ui_files.ui_nebula import Ui_MainWindow
from LexerQsci import Editor
from tools import debug

"""
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




    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        super(MyWindowClass, self).__init__(parent)
        self.installEventFilter(self)
        self.setupUi(self)

        self.QSciEditor = Editor(parent=self)
        self.QSciEditor.setIndentationGuides(True)

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
        self.treeOutline.clicked.connect(self.outline_clicked)

        self.pushButton_2.clicked.connect(self.clean)
        self.gridLayout.addWidget(self.QSciEditor)
        self.ast = AstParser()
        self.show()

        for key in self.keybindings:
            self.shortcut = QShortcut(self)
            self.shortcut.setKey(key[0])
            self.shortcut.activated.connect(getattr(self, key[1]))

    def save(self):
        file = open(self.QSciEditor.filename, "w")
        file.write(self.QSciEditor.text())
        file.close()
        self.refresh_outline()
        debug(self.QSciEditor.filename + " is saved..." )


    def quit(self):
        debug("quitting..." )
        app.quit()

    def openMenu(self, position):
        menu = QMenu()
        menu.addAction(self.tr("Go to"))
        menu.exec_(self.treeOutline.viewport().mapToGlobal(position))

    def test(self, signal):
        file_path = self.treeView.model().filePath(signal)
        self.QSciEditor.filename = file_path  # Soon will be used to save to that file.
        # try:
        if os.path.isfile(file_path):
            with open(file_path, 'r+') as currentFile:
                self.QSciEditor.setText(currentFile.read())
                self.refresh_outline()

    def refresh_outline(self):
        kinds = []
        kinds.append(CursorKind.FUNCTION_DECL)
        kinds.append(CursorKind.VAR_DECL)
        kinds.append(CursorKind.DECL_REF_EXPR)
        kinds.append(CursorKind.COMPOUND_STMT)
        # kinds.append(CursorKind.STRUCT_DECL)
        kinds.append(CursorKind.FIELD_DECL)

        outline = self.ast.get_outline(self.QSciEditor.filename, kinds)
        self.treeOutline.setModel(outline)


                # except Exception as e:
        #     print(e)

    def outline_clicked(self, index):
        loc = (self.treeOutline.model().itemFromIndex(index).location)
        debug("Node Location: " + str(loc.line) + "," + str(loc.column))
        self.QSciEditor.setCursorPosition(loc.line - 1, loc.column - 1)
        self.QSciEditor.ensureLineVisible(loc.line - 1)
        self.QSciEditor.ensureCursorVisible()
        self.QSciEditor.setFocus()

    def clean(self, signal):
        debug("clean...")

    def autocomplete(self):
        self.QSciEditor.autoCompleteFromAll()
        debug("autocompleted...")

    def testplace(self):
        debug("This is for testing purposes...")

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
