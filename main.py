#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem
from PyQt5.QtWidgets import QApplication, QMainWindow


class CoffeeInfoViewer(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.connection = sqlite3.connect("coffee.sqlite")
        self.cursor = self.connection.cursor()
        self.initUI()

    # noinspection PyPep8Naming
    def initUI(self):
        sql_command = """SELECT * FROM coffee"""
        res = self.connection.cursor().execute(sql_command).fetchall()
        if not res:
            QMessageBox.warning(self, "Информация о результате.",
                                'К сожалению, ничего не нашлось.',
                                QMessageBox.Ok)
        # Заполним размеры таблицы.
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        # Заполняем таблицу элементами.
        self.tableWidget.setHorizontalHeaderLabels(
            ['ID', 'Название сорта', 'Степень обжарки', 'Молотый / в зёрнах',
             'Описание вкуса', 'Цена', 'Объём упаковки'])
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elem)))
        self.tableWidget.resizeColumnsToContents()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CoffeeInfoViewer()
    ex.show()
    sys.exit(app.exec_())
