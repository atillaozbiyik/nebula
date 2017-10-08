from PyQt5 import QtCore, QtGui, QtWidgets
from LexerQsci import Editor

class tabEditor(QtWidgets.QWidget):
    def __init__(self, parent=None, filepath = '', content = ''):
        super(tabEditor, self).__init__()
        # print(parent)
        # print(filename)
        # print(content)
        self.setObjectName("tab")
        parent.addTab(self, "")
        self._filepath = filepath
        self.filename = filepath.split("/")[-1]

        self.QSciEditor = Editor()
        # self.gridLayout.addWidget(self.QSciEditor)
        editorLayout = QtWidgets.QGridLayout(self)
        editorLayout.setObjectName("editorLayout")
        editorLayout.addWidget(self.QSciEditor)
        self.QSciEditor.setText(content)
        _translate = QtCore.QCoreApplication.translate
        parent.setTabText(parent.indexOf(self), _translate("MainWindow", self.filename ))