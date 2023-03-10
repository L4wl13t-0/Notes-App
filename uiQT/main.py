# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindows.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 700)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 700))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 700))
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.fr_up = QtWidgets.QFrame(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.fr_up.setFont(font)
        self.fr_up.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_up.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_up.setObjectName("fr_up")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.fr_up)
        self.horizontalLayout.setContentsMargins(11, 5, 11, 1)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lbl_tittle = QtWidgets.QLabel(self.fr_up)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbl_tittle.setFont(font)
        self.lbl_tittle.setStyleSheet("")
        self.lbl_tittle.setFrameShape(QtWidgets.QFrame.Box)
        self.lbl_tittle.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lbl_tittle.setTextFormat(QtCore.Qt.AutoText)
        self.lbl_tittle.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_tittle.setWordWrap(False)
        self.lbl_tittle.setObjectName("lbl_tittle")
        self.horizontalLayout.addWidget(self.lbl_tittle)
        self.verticalLayout.addWidget(self.fr_up)
        self.fr_down = QtWidgets.QFrame(self.centralwidget)
        self.fr_down.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_down.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_down.setObjectName("fr_down")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.fr_down)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.fr_notes = QtWidgets.QFrame(self.fr_down)
        self.fr_notes.setStyleSheet("font: 10pt \"Consolas\";\n"
"border: 2px solid #ffffff;")
        self.fr_notes.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_notes.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_notes.setObjectName("fr_notes")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.fr_notes)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tab_notes = QtWidgets.QTabWidget(self.fr_notes)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.tab_notes.setFont(font)
        self.tab_notes.setStyleSheet("QTabWidget::pane { /* The tab widget frame */\n"
"    border-top: 1px solid #111010;\n"
"}\n"
"QTabWidget::tab-bar {\n"
"    left: 5px; /* move to the right by 5px */\n"
"}\n"
"QTabBar::tab {\n"
"    background: #111010;\n"
"    border: 2px solid #C4C4C3;\n"
"    border-bottom-color: #C2C7CB; /* same as the pane color */\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"    min-width: 8ex;\n"
"    padding: 2px;\n"
"}\n"
"QTabBar::tab:selected {\n"
"    background: #491d88;\n"
"}\n"
"QTabBar::tab:hover{\n"
"    background: #491d88;\n"
"}\n"
"QTabBar::tab:selected {\n"
"    border-bottom-color: #111010; /* same as pane color */\n"
"}")
        self.tab_notes.setDocumentMode(False)
        self.tab_notes.setTabsClosable(True)
        self.tab_notes.setMovable(True)
        self.tab_notes.setTabBarAutoHide(False)
        self.tab_notes.setObjectName("tab_notes")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.textEdit = QtWidgets.QTextEdit(self.tab)
        self.textEdit.setGeometry(QtCore.QRect(3, 6, 821, 521))
        self.textEdit.setMaximumSize(QtCore.QSize(821, 521))
        self.textEdit.setStyleSheet("QTextEdit\n"
"{\n"
"    border: 0;\n"
"    font: 10pt \"Consolas\";\n"
"}")
        self.textEdit.setInputMethodHints(QtCore.Qt.ImhMultiLine)
        self.textEdit.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.textEdit.setLineWrapColumnOrWidth(0)
        self.textEdit.setTabStopWidth(80)
        self.textEdit.setObjectName("textEdit")
        self.tab_notes.addTab(self.tab, "")
        self.verticalLayout_3.addWidget(self.tab_notes)
        self.horizontalLayout_2.addWidget(self.fr_notes)
        self.fr_buttons = QtWidgets.QFrame(self.fr_down)
        self.fr_buttons.setStyleSheet("font: 10pt \"Consolas\";\n"
"border: 2px solid #ffffff;")
        self.fr_buttons.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fr_buttons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_buttons.setObjectName("fr_buttons")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.fr_buttons)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout_2.setSpacing(4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btn_addNote = QtWidgets.QPushButton(self.fr_buttons)
        self.btn_addNote.setStyleSheet("QPushButton {\n"
"    background-color: #27ae60;\n"
"    border-radius: 8px;\n"
"    border-style: none;\n"
"    color: #fff;\n"
"    font-size: 16px;\n"
"    font-weight: 600;\n"
"    letter-spacing: normal;\n"
"    line-height: 1.5;\n"
"    outline: none;\n"
"    padding: 13px 20px;\n"
"    position: relative;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    vertical-align: top;\n"
"    white-space: nowrap;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"  background-color: #16cc65;     \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #0b7538;\n"
"}")
        self.btn_addNote.setCheckable(False)
        self.btn_addNote.setObjectName("btn_addNote")
        self.verticalLayout_2.addWidget(self.btn_addNote)
        self.btn_renameNote = QtWidgets.QPushButton(self.fr_buttons)
        self.btn_renameNote.setStyleSheet("QPushButton {\n"
"    background-color: #fea444;\n"
"    border-radius: 8px;\n"
"    border-style: none;\n"
"    color: #fff;\n"
"    font-size: 16px;\n"
"    font-weight: 600;\n"
"    letter-spacing: normal;\n"
"    line-height: 1.5;\n"
"    outline: none;\n"
"    padding: 13px 20px;\n"
"    position: relative;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    vertical-align: top;\n"
"    white-space: nowrap;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: #f5840c;     \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #b0712e;\n"
"}")
        self.btn_renameNote.setObjectName("btn_renameNote")
        self.verticalLayout_2.addWidget(self.btn_renameNote)
        self.horizontalLayout_2.addWidget(self.fr_buttons)
        self.horizontalLayout_2.setStretch(0, 10)
        self.horizontalLayout_2.setStretch(1, 1)
        self.verticalLayout.addWidget(self.fr_down)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 8)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tab_notes.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "NoJodan Notes"))
        self.lbl_tittle.setText(_translate("MainWindow", "NoJodan Notes"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Consolas\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.tab_notes.setTabText(self.tab_notes.indexOf(self.tab), _translate("MainWindow", "Nota 1"))
        self.btn_addNote.setText(_translate("MainWindow", "ADD"))
        self.btn_renameNote.setText(_translate("MainWindow", "RENAME"))
