from PyQt5 import QtCore, QtGui, QtWidgets

class embterminal(QtWidgets.QWidget):
    def __init__(self,parent=None):
        QtWidgets.QWidget.__init__(self)
        self.process = QtCore.QProcess(self)
        self.terminal = QtWidgets.QWidget(self)
        layout = QtWidgets.QVBoxLayout(self)

        win = QtWidgets.QWidget()
        winID = int(win.winId())

        sub_win = QtGui.QWindow.fromWinId(winID)
        container = QtWidgets.QWidget.createWindowContainer(sub_win)
        container.setLayout(layout)
        sub_win_id = int(container.winId())

        parent.addWidget(container)
        # self.process.start('xterm',['-into', str(self.terminal.winId())])
        self.process.start('xterm', ['-into', str(sub_win_id)])

# app = QtWidgets.QApplication(sys.argv)
# win = QtWidgets.QWidget()
# winID = int(win.winId())
#
# sub_win = QtGui.QWindow.fromWinId(winID)
# container = QtWidgets.QWidget.createWindowContainer(sub_win)
#
# sub_win_id = int(container.winId())
#
# process = QtCore.QProcess(container)