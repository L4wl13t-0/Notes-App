from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QWidget
from PyQt5 import uic, QtCore, QtWidgets
import sys

class RenameDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("uiQT/renameDialog.ui", self)
        self.value = 1
        self.btn_rename.rejected.connect(self.changeName)

    def changeName(self):
        self.value = 0

class TabPage(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)    
        textEdit = QtWidgets.QTextEdit()
        textEdit.setGeometry(QtCore.QRect(3, 6, 821, 521))
        textEdit.setMaximumSize(QtCore.QSize(821, 521))
        textEdit.setInputMethodHints(QtCore.Qt.ImhMultiLine)
        textEdit.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        textEdit.setLineWrapColumnOrWidth(0)
        textEdit.setTabStopWidth(80)
        textEdit.setObjectName("textEdit")
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(textEdit)

class Window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi("uiQT/mainWindows.ui", self)
        self.btn_renameNote.clicked.connect(self.openRenameDialog)
        self.btn_addNote.clicked.connect(self.addNote)
        self.tab_notes.tabCloseRequested.connect(self.delete)

    def openRenameDialog(self):
        renameDialog = RenameDialog()
        renameDialog.exec()
        if(renameDialog.value == 1):
            self.tab_notes.setTabText(self.tab_notes.currentIndex(), renameDialog.lnEdit_rename.text())
        else:
            pass

    def addNote(self):
        self.tab_notes.addTab(TabPage(self.tab_notes), "New Tab")

    def delete(self, index):
        self.tab_notes.removeTab(index)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())