import sys
import os

from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *


class TableWidget(QTabWidget):
	def __init__(self):
		super.__init__()
        self.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.setSelectionBehavior(QTableView.SelectRows)
        self.setShowGrid(False)
class TableAcc(TableWidget):
	def __init__(sefl):
		super.__init__()
		self.setColumnCount(2)
		self.setHorizontalHeaderLabels(["Accounts", "Password"])

class MyViettelGUI(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("My Viettel")
		self.setMinimumHeight(300)
		self.centralwidget = TableAcc()
		self.setCentralWidget(self.centralwidget)


if __name__ == "__main__":
	app = QApplication(sys.argv)

	main_window = MyViettelGUI()
	main_window.show()
	app.exec()