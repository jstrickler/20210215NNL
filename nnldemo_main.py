#!/usr/bin/env python

import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from ui_nnldemo import Ui_NNLDemo


class NNLDemoMain(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # Set up the user interface from Designer.
        self.ui = Ui_NNLDemo()
        self.ui.setupUi(self)

        # Connect up menu actions
        # self.ui.actionExit.triggered.connect(self.close)

        # Connect up buttons.
        # self.ui.BUTTON_NAME.clicked.connect(self._pushed)
        self.ui.actionWombat.triggered.connect(self._wombats)
        self.ui.bt_maybe.clicked.connect(self._maybe_clicked)

    def _maybe_clicked(self):
        self.ui.le_first_name.setText(self.ui.le_last_name.text())

    def _wombats(self):
        self.ui.le_last_name.setText("WOMBATS!")
        print("I like wombats!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = NNLDemoMain()
    main.show()
    status_code = app.exec()
    sys.exit(status_code)
