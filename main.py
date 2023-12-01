import sys
import os

from PyQt5.QtWidgets import (
    QMainWindow,
    QApplication,
)


from create_new_db import create_new_db
from tab_widget import TaskProjectTabs


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("To Do List")
        self.setMinimumHeight(300)

        self.central_widget = TaskProjectTabs()
        self.setCentralWidget(self.central_widget)

        self.central_widget.task_exit_button.clicked.connect(self.close)
        self.central_widget.project_exit_button.clicked.connect(self.close)


if __name__ == "__main__":
    # creates new database when run for the first time
    if not os.path.exists("to_do.sqlite"):
        create_new_db("to_do.sqlite")
    to_do = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    main_window.raise_()
    to_do.exec_()
