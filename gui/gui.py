#-'''- coding: utf-8 -'''-

import sys
from PySide.QtCore import *
from PySide.QtGui import *

class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        # 空の縦レイアウトを作る
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        # ウィジェットを作成します。
        self.edit = QLineEdit("")
        self.button = QPushButton("Math")
        self.lineEdit = QLineEdit('lineEdit')
        # レイアウトを作成しウィジェットを追加します
        # ダイアログのレイアウトを設定します
        self.layout.addWidget(self.edit)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.lineEdit)
        # ボタンのシグナルをgreetingsと接続します
        self.button.clicked.connect(self.greetings)

# ユーザへ挨拶します
    def greetings(self):
        if(int(self.edit.text()) % 2 == 0):
            self.lineEdit.setText("gu")
        else:
            self.lineEdit.setText("ki")


if __name__ == '__main__':
    # Qt Applicationを作ります
    app = QApplication(sys.argv)
    # formを作成して表示します
    form = Form()
    form.show()
    # Qtのメインループを開始します
    sys.exit(app.exec_())