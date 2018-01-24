# -'''- coding: utf-8 -'''-

import sys
from PySide.QtCore import *
from PySide.QtGui import *

class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setWindowTitle("My Form")
        # ウィジェットを作成します。
        self.edit = QLineEdit("")
        self.button = QPushButton("math")
        # レイアウトを作成しウィジェットを追加します
        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.button)
        # ダイアログのレイアウトを設定します
        self.setLayout(layout)

def greetings(self):
    print ("Hello", self.edit.text())


if __name__ == '__main__':
    # Qt Applicationを作成します
    app = QApplication(sys.argv)
    # formを作成して表示します
    form = Form()
    form.show()
    # Qtのメインループを開始します
    sys.exit(app.exec_())


