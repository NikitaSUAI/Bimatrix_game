from PyQt5.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
                             QPushButton, QTextEdit, QVBoxLayout)
from typing import List, Tuple
import re
from Game.Game import Game

class WidgetGallery(QDialog):
    example = """(-5,-5) (0,-15)
(-15,0) (-1,-1)"""
    def __init__(self, parent=None):
        super(WidgetGallery, self).__init__(parent)
        self.resize(300, 300)
        self.setLayout(self.layouts())

    def layouts(self):
        mainLayout = QHBoxLayout()

        left_layout = QVBoxLayout()



        label = QLabel("Введите биматричное представление игры")
        left_layout.addWidget(label)

        self.input = QTextEdit()
        self.input.setText(self.example)
        left_layout.addWidget(self.input)

        calculateBut = QPushButton("Найти равновесие Неша")
        calculateBut.clicked.connect(self.calculate)
        left_layout.addWidget(calculateBut)

        self.status = QLabel("Готов")
        left_layout.addWidget(self.status)

        mainLayout.addLayout(left_layout)

        return mainLayout

    def calculate(self):
        try:
            self.status.setText("В рвботе")
            text = self.input.toPlainText()
            g = self.parse(text)
            game = Game(g)
            res = game.play()
            final = list()
            for i in res:
                tmp = list()
                for j in i:
                    tmp.append(j+1)
                final.append(f"{tmp}")
            self.status.setText(f"{', '.join(final)} ∈ NE")
        except BaseException:
            self.status.setText("Произошла ошибка!")



    def parse(self, str) -> List[List[Tuple[int, int]]]:
        res = list()
        for i in str.split("\n"):
            tmp = list()
            for j in i.split(" "):
                tmp_list = list()
                tmp_str = re.sub("(\([+-]*[0-9]+,)([+-]*[0-9]+\))", dashrepl, j)
                for n in tmp_str.split(" "):
                    tmp_list.append(int(n))
                tmp.append(tuple(tmp_list))
            res.append(tmp)
        return res

def dashrepl(matchobj):
    """(1, 1)= -> 1 1"""
    a = matchobj.group(1)[1:][:-1]
    b = matchobj.group(2)[:-1]
    return " ".join((a, b))

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    gallery = WidgetGallery()
    gallery.show()
    sys.exit(app.exec_())