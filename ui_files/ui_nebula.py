# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nebula.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(859, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QWidget{\n"
"background:rgb(34,45,50);\n"
"border-radius: 3px;\n"
"color:white;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setSpacing(4)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.buttonBox = QtWidgets.QGroupBox(self.centralwidget)
        self.buttonBox.setMinimumSize(QtCore.QSize(0, 50))
        self.buttonBox.setMaximumSize(QtCore.QSize(16777215, 50))
        self.buttonBox.setStyleSheet("QPushButton:hover{\n"
"       color:rgb(224,224,224);\n"
"        background:rgb(24,39,45);\n"
"}\n"
"QPushButton {\n"
"        border:1px solid rgb(64,75,80);\n"
"        border-radius: 2px;\n"
"        padding: 5px 5px 2px 5px;\n"
"        background:rgb(44,59,65);\n"
"        color: rgb(240,240,240);\n"
"        height: 30px;\n"
"}\n"
"QPushButton:pressed {\n"
"        background: rgb();\n"
"        padding-top: 2px;\n"
"        padding-left: 4px;\n"
"}\n"
"QPushButton:pressed {\n"
"        background: rgb();\n"
"        padding-top: 2px;\n"
"        padding-left: 4px;\n"
"}\n"
"QPushButton:disabled{\n"
"        background: rgb(34,45,50);\n"
"        padding-top: 2px;\n"
"        padding-left: 4px;\n"
"        color: rgb(100,100,100);\n"
"}")
        self.buttonBox.setTitle("")
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.buttonBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.runButton = QtWidgets.QPushButton(self.buttonBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.runButton.sizePolicy().hasHeightForWidth())
        self.runButton.setSizePolicy(sizePolicy)
        self.runButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.runButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/resources/run.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.runButton.setIcon(icon)
        self.runButton.setIconSize(QtCore.QSize(24, 24))
        self.runButton.setObjectName("runButton")
        self.horizontalLayout.addWidget(self.runButton)
        self.cleanButton = QtWidgets.QPushButton(self.buttonBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cleanButton.sizePolicy().hasHeightForWidth())
        self.cleanButton.setSizePolicy(sizePolicy)
        self.cleanButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.cleanButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/resources/clean.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cleanButton.setIcon(icon1)
        self.cleanButton.setIconSize(QtCore.QSize(24, 24))
        self.cleanButton.setObjectName("cleanButton")
        self.horizontalLayout.addWidget(self.cleanButton)
        self.installButton = QtWidgets.QPushButton(self.buttonBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.installButton.sizePolicy().hasHeightForWidth())
        self.installButton.setSizePolicy(sizePolicy)
        self.installButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.installButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/resources/install.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.installButton.setIcon(icon2)
        self.installButton.setIconSize(QtCore.QSize(24, 24))
        self.installButton.setObjectName("installButton")
        self.horizontalLayout.addWidget(self.installButton)
        self.debugButton = QtWidgets.QPushButton(self.buttonBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.debugButton.sizePolicy().hasHeightForWidth())
        self.debugButton.setSizePolicy(sizePolicy)
        self.debugButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.debugButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/resources/debug.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.debugButton.setIcon(icon3)
        self.debugButton.setIconSize(QtCore.QSize(24, 24))
        self.debugButton.setObjectName("debugButton")
        self.horizontalLayout.addWidget(self.debugButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout_5.addWidget(self.buttonBox, 0, 0, 1, 1)
        self.mainContainer = QtWidgets.QGroupBox(self.centralwidget)
        self.mainContainer.setObjectName("mainContainer")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.mainContainer)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.splitter_3 = QtWidgets.QSplitter(self.mainContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter_3.sizePolicy().hasHeightForWidth())
        self.splitter_3.setSizePolicy(sizePolicy)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.projectBox = QtWidgets.QGroupBox(self.splitter_3)
        self.projectBox.setMinimumSize(QtCore.QSize(0, 0))
        self.projectBox.setMaximumSize(QtCore.QSize(300, 16777215))
        self.projectBox.setStyleSheet("QGroupBox{\n"
"border:1px solid white;\n"
"border-radius:0px;\n"
"}")
        self.projectBox.setTitle("")
        self.projectBox.setObjectName("projectBox")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.projectBox)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.splitter_2 = QtWidgets.QSplitter(self.projectBox)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.fileBox = QtWidgets.QGroupBox(self.splitter_2)
        self.fileBox.setObjectName("fileBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.fileBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.fileBox)
        self.label.setMinimumSize(QtCore.QSize(0, 30))
        self.label.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.treeView = QtWidgets.QTreeView(self.fileBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeView.sizePolicy().hasHeightForWidth())
        self.treeView.setSizePolicy(sizePolicy)
        self.treeView.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.treeView.setObjectName("treeView")
        self.verticalLayout.addWidget(self.treeView)
        self.structureBox = QtWidgets.QGroupBox(self.splitter_2)
        self.structureBox.setTitle("")
        self.structureBox.setObjectName("structureBox")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.structureBox)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.treeOutline = QtWidgets.QTreeView(self.structureBox)
        self.treeOutline.setObjectName("treeOutline")
        self.gridLayout_7.addWidget(self.treeOutline, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.splitter_2, 0, 0, 1, 1)
        self.workSpaceBox = QtWidgets.QGroupBox(self.splitter_3)
        self.workSpaceBox.setObjectName("workSpaceBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.workSpaceBox)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.splitter = QtWidgets.QSplitter(self.workSpaceBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.editorBox = QtWidgets.QGroupBox(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editorBox.sizePolicy().hasHeightForWidth())
        self.editorBox.setSizePolicy(sizePolicy)
        self.editorBox.setStyleSheet("QWidget{\n"
"background:rgb(34,45,50);\n"
"border-radius: 3px;\n"
"color:white;\n"
"}\n"
"QTextEdit{\n"
"border:2px solid white;\n"
"}\n"
"#editorBox{\n"
"border:1px solid white;\n"
"border-radius:0px;\n"
"}")
        self.editorBox.setTitle("")
        self.editorBox.setObjectName("editorBox")
        self.gridLayout = QtWidgets.QGridLayout(self.editorBox)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.editorBox)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setMovable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)
        self.infoBox = QtWidgets.QGroupBox(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.infoBox.sizePolicy().hasHeightForWidth())
        self.infoBox.setSizePolicy(sizePolicy)
        self.infoBox.setMinimumSize(QtCore.QSize(0, 0))
        self.infoBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.infoBox.setMouseTracking(True)
        self.infoBox.setStyleSheet("QPushButton:hover{\n"
"       color:rgb(224,224,224);\n"
"        background:rgb(24,39,45);\n"
"}\n"
"QPushButton {\n"
"        border-top:1px solid white;\n"
"        border-right:1px solid white;\n"
"        border-left:1px solid white;\n"
"        border-radius: 0px;\n"
"        padding: 5px 5px 2px 5px;\n"
"        background:rgb(44,59,65);\n"
"        color: rgb(240,240,240);\n"
"        height: 15px;\n"
"}\n"
"QPushButton:pressed {\n"
"        background: rgb();\n"
"        padding-top: 2px;\n"
"        padding-left: 4px;\n"
"}\n"
"QPushButton:pressed {\n"
"        background: rgb();\n"
"        padding-top: 2px;\n"
"        padding-left: 4px;\n"
"}\n"
"QPushButton:disabled{\n"
"        background: rgb(34,45,50);\n"
"        padding-top: 2px;\n"
"        padding-left: 4px;\n"
"        color: rgb(100,100,100);\n"
"}\n"
"QStackedWidget{\n"
"        border:1px solid white;\n"
"        border-radius:0px;\n"
"}")
        self.infoBox.setTitle("")
        self.infoBox.setObjectName("infoBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.infoBox)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.infoBox)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_3.addWidget(self.pushButton_4, 0, 2, 1, 1)
        self.stackedWidget = QtWidgets.QStackedWidget(self.infoBox)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.pageLayout = QtWidgets.QGridLayout(self.page)
        self.pageLayout.setContentsMargins(0, 0, 0, 0)
        self.pageLayout.setSpacing(0)
        self.pageLayout.setObjectName("pageLayout")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.gridLayout_3.addWidget(self.stackedWidget, 1, 0, 1, 6)
        self.pushButton_5 = QtWidgets.QPushButton(self.infoBox)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_3.addWidget(self.pushButton_5, 0, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.infoBox)
        self.pushButton_2.setText("")
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_3.addWidget(self.pushButton_2, 0, 5, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.infoBox)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_3.addWidget(self.pushButton_3, 0, 3, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.infoBox)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_3.addWidget(self.pushButton, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 0, 4, 1, 1)
        self.gridLayout_4.addWidget(self.splitter, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.splitter_3, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.mainContainer, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 859, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuRun = QtWidgets.QMenu(self.menubar)
        self.menuRun.setObjectName("menuRun")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew_Project = QtWidgets.QAction(MainWindow)
        self.actionNew_Project.setObjectName("actionNew_Project")
        self.actionNew_File = QtWidgets.QAction(MainWindow)
        self.actionNew_File.setObjectName("actionNew_File")
        self.actionOpen_Project = QtWidgets.QAction(MainWindow)
        self.actionOpen_Project.setObjectName("actionOpen_Project")
        self.actionOpen_File = QtWidgets.QAction(MainWindow)
        self.actionOpen_File.setObjectName("actionOpen_File")
        self.actionRun = QtWidgets.QAction(MainWindow)
        self.actionRun.setObjectName("actionRun")
        self.actionBuild = QtWidgets.QAction(MainWindow)
        self.actionBuild.setObjectName("actionBuild")
        self.actionClean = QtWidgets.QAction(MainWindow)
        self.actionClean.setObjectName("actionClean")
        self.actionDebug = QtWidgets.QAction(MainWindow)
        self.actionDebug.setObjectName("actionDebug")
        self.actionRun_Options = QtWidgets.QAction(MainWindow)
        self.actionRun_Options.setObjectName("actionRun_Options")
        self.actionDebug_Options = QtWidgets.QAction(MainWindow)
        self.actionDebug_Options.setObjectName("actionDebug_Options")
        self.menuFile.addAction(self.actionNew_Project)
        self.menuFile.addAction(self.actionNew_File)
        self.menuFile.addAction(self.actionOpen_Project)
        self.menuFile.addAction(self.actionOpen_File)
        self.menuRun.addAction(self.actionRun)
        self.menuRun.addAction(self.actionBuild)
        self.menuRun.addAction(self.actionClean)
        self.menuRun.addAction(self.actionDebug)
        self.menuRun.addAction(self.actionRun_Options)
        self.menuRun.addAction(self.actionDebug_Options)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuRun.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.mainContainer.setTitle(_translate("MainWindow", "GroupBox"))
        self.fileBox.setTitle(_translate("MainWindow", "GroupBox"))
        self.label.setText(_translate("MainWindow", "Project:"))
        self.workSpaceBox.setTitle(_translate("MainWindow", "GroupBox"))
        self.pushButton_4.setText(_translate("MainWindow", "Evaluate Expression"))
        self.pushButton_5.setText(_translate("MainWindow", "Debug Console"))
        self.pushButton_3.setText(_translate("MainWindow", "Output"))
        self.pushButton.setText(_translate("MainWindow", "Terminal"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuRun.setTitle(_translate("MainWindow", "Run"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionNew_Project.setText(_translate("MainWindow", "New Project"))
        self.actionNew_File.setText(_translate("MainWindow", "New File"))
        self.actionOpen_Project.setText(_translate("MainWindow", "Open Project"))
        self.actionOpen_File.setText(_translate("MainWindow", "Open File"))
        self.actionRun.setText(_translate("MainWindow", "Run"))
        self.actionBuild.setText(_translate("MainWindow", "Build"))
        self.actionClean.setText(_translate("MainWindow", "Clean"))
        self.actionDebug.setText(_translate("MainWindow", "Debug"))
        self.actionRun_Options.setText(_translate("MainWindow", "Run Options"))
        self.actionDebug_Options.setText(_translate("MainWindow", "Debug Options"))

import rsrcs_rc
