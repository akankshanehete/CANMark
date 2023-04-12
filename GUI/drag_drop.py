
# drag and dropping file into software so it can be plotted

from uploadfilepage import Ui_MainWindow
import sys
from PyQt5 import QtCore, QtWidgets
import platform

op_sys = platform.system()
if op_sys == 'Darwin':
    from Foundation import NSURL
# We use NSURL as a workaround to PySide/ Qt4 for drag/drop
# on OSx


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        """
        This function initializes our main window from the main.py, set its title 
        and also allow the drops on it.
        """
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('PyShine drag drop plot')
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):
        """
        This function will detect the drag enter event from the mouse on the main window
        """
        if e.mimeData().hasUrls:
            e.accept()
        else:
            e.ignore()

    def dragMoveEvent(self, e):
        """
        This function will detect the drag move event on the main window
        """
        if e.mimeData().hasUrls:
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        """
        This function will enable the drop file directly on to the 
        main window. The file location will be stored in the self.filename
        """
        if e.mimeData().hasUrls:
            e.setDropAction(QtCore.Qt.CopyAction)
            e.accept()
            for url in e.mimeData().urls():
                fname = str(url.toLocalFile())
            self.filename = fname
            print("GOT ADDRESS:", self.filename)
            self.readData()
        else:
            e.ignore()  # just like above functions


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
