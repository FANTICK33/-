from PyQt6.QtWidgets import *
from PyQt6.QtGui import QIcon
import gspread
from google.oauth2.service_account import Credentials

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Google Sheets App'
        self.left = 10
        self.top = 10
        self.width = 500
        self.height = 300
        self.table = QTableWidget()
        self.sheet_names = []
        self.sheet = None
        self.row_count = 0
        self.col_count = 0
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowIcon(QIcon('icon.png'))
        vbox = QVBoxLayout()

        hbox = QHBoxLayout()
        label = QLabel('Select a sheet')
        hbox.addWidget(label)
        self.sheet_name_field = QLineEdit()
        hbox.addWidget(self.sheet_name_field)
        btn = QPushButton('Open Sheet')
        btn.clicked.connect(self.open_sheet)
        hbox.addWidget(btn)
        vbox.addLayout(hbox)

        self.table.setColumnCount(1)
        self.table.setRowCount(1)
        self.table.setHorizontalHeaderLabels(['Data'])
        vbox.addWidget(self.table)

        hbox = QHBoxLayout()
        edit_field = QLineEdit()
        hbox.addWidget(edit_field)
        edit_btn = QPushButton('Update')
        edit_btn.clicked.connect(self.edit)
        hbox.addWidget(edit_btn)
        delete_btn = QPushButton('Delete')
        delete_btn.clicked.connect(self.delete)
        hbox.addWidget(delete_btn)
        vbox.addLayout(hbox)

        hbox = QHBoxLayout()
        add_field = QLineEdit()
        hbox.addWidget(add_field)
        add_btn = QPushButton('Add')
        add_btn.clicked.connect(self.add)
        hbox.addWidget(add_btn)
        vbox.addLayout(hbox)

        self.setLayout(vbox)
        self.show()

    def open_sheet(self):
        self.sheet_name = self.sheet_name_field.text()
        if self.sheet_name not in self.sheet_names:
            self.sheet_names.append(self.sheet_name)
        creds = Credentials.from_service_account_file('path/to/key.json')
        client = gspread.authorize(creds)
        sheet = client.open(self.sheet_name).sheet1
        self.sheet = sheet
        self.row_count = sheet.row_count
        self.col_count = sheet.col_count
        data = sheet.get_all_values()
        self.table.c

lear()
        self.table.setRowCount(len(data))
        self.table.setColumnCount(self.col_count)
        self.table.setHorizontalHeaderLabels(data[0])
        for i in range(1, len(data)):
            for j in range(self.col_count):
                self.table.setItem(i-1, j, QTableWidgetItem(data[i][j]))

    def sort(self):
        column = self.table.currentColumn()
        if self.sort_order == 'ascending':
            data = self.sheet.get_all_values()[1:]
            data.sort(key=lambda x: x[column])
            self.sheet.clear()
            self.sheet.append_row(self.table.horizontalHeaderItem(i).text() for i in range(self.col_count))
            self.sheet.insert_rows(data)
            self.sort_order = 'descending'
        else:
            data = self.sheet.get_all_values()[1:]
            data.sort(key=lambda x: x[column], reverse=True)
            self.sheet.clear()
            self.sheet.append_row(self.table.horizontalHeaderItem(i).text() for i in range(self.col_count))
            self.sheet.insert_rows(data)
            self.sort_order = 'ascending'

    def edit(self):
        row = self.table.currentRow()
        col = self.table.currentColumn()
        new_value = self.sender().parent().children()[0].text()
        if self.sheet is not None:
            self.sheet.update_cell(row+1, col+1, new_value)
            data = self.sheet.get_all_values()[1:]
            for i in range(len(data)):
                for j in range(self.col_count):
                    self.table.setItem(i, j, QTableWidgetItem(data[i][j]))

    def delete(self):
        row = self.table.currentRow()
        if self.sheet is not None:
            self.sheet.delete_row(row+1)
            data = self.sheet.get_all_values()[1:]
            self.table.clear()
            self.table.setRowCount(len(data))
            self.table.setColumnCount(self.col_count)
            self.table.setHorizontalHeaderLabels(self.sheet.row_values(1))
            for i in range(len(data)):
                for j in range(self.col_count):
                    self.table.setItem(i, j, QTableWidgetItem(data[i][j]))

    def add(self):
        value = self.sender().parent().children()[0].text()
        if self.sheet is not None:
            self.sheet.append_row(value.split(','))
            data = self.sheet.get_all_values()[1:]
            self.table.clear()
            self.table.setRowCount(len(data))
            self.table.setColumnCount(self.col_count)
            self.table.setHorizontalHeaderLabels(self.sheet.row_values(1))
            for i in range(len(data)):
                for j in range(self.col_count):
                    self.table.setItem(i, j, QTableWidgetItem(data[i][j]))

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec())
...
