import gspread
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tabulate import tabulate

gs = gspread.service_account(filename='credentials.json')
sheet = gs.open_by_key('1uClkxjKnIHsnrjAp9NKGjirv8v24uQItZ1v7z8DE8dk')
worksheet = sheet.sheet1

root = tk.Tk()
root.title("Google Sheets Editor")
root.geometry("1500x555")

def view_data():
    data = worksheet.get_all_values()
    headers = data.pop(0)
    rows = []

    for row in data:
        rows.append(row)

    table = tabulate(rows, headers=headers)

    view_frame = tk.Frame(root)
    view_frame.grid(row=2, column=0, columnspan=5)

    scrollbar = tk.Scrollbar(view_frame, orient=tk.VERTICAL)
    scrollbar.grid(row=0, column=1, sticky=tk.NS)

    text = Text(view_frame, width=150, height=20, yscrollcommand=scrollbar.set)
    text.insert(tk.END, table)
    text.grid(row=0, column=0)
    scrollbar.config(command=text.yview)

    save_button = tk.Button(view_frame, text="Сохранить изменения", command=save_changes)
    save_button.grid(row=1, column=0, pady=5)

    back_button = tk.Button(view_frame, text="Назад", command=view_frame.destroy)
    back_button.grid(row=1, column=1, pady=5)

def save_changes():
    new_table = text.get('1.0', 'end')
    new_data = []

    # Отфильтровать пустые строки
    for row in new_table.split('\n'):
        if row.strip() != '':
            new_data.append(row.split('\t'))

    worksheet.clear()

    for row in new_data:
        worksheet.append_row(row)

    messagebox.showinfo("Сохранить изменения", "Изменения успешно сохранены!")

def add_row():
    new_name = name_entry.get()
    new_age = age_entry.get()
    worksheet.append_row([new_name, new_age])
    messagebox.showinfo("Добавить запись", "Запись успешно добавлена!")

def edit_row():
    index = int(index_entry.get())
    new_name = name_entry.get()
    new_age = age_entry.get()
    update_cell(index, 1, new_name)
    update_cell(index, 2, new_age)
    messagebox.showinfo("Редактировать запись", "Запись успешно изменена!")



def delete_row():
    index = int(index_entry.get())
    worksheet.delete_rows(index)
    messagebox.showinfo("Удалить запись", "Запись успешно удалена!")

def sort_data():
    column = sort_column.get()
    sort_order = sort_order.get()
    sorted_data = worksheet.get_all_records(empty2zero=False, head=1, default_blank="")
    sorted_data = sorted(sorted_data, key=lambda x: x[column], reverse=sort_order == 'desc')
    worksheet.clear()
    worksheet.append_row(sheet.row_values(1))
    for row in sorted_data:
        worksheet.append_row(list(row.values()))
    view_data()

def sort_by_column():
    column = sort_column.get()
    worksheet.sort(column)
    view_data()

view_button = tk.Button(root, text="Просмотреть", command=view_data)
view_button.grid(row=1, column=0)

sort_label = tk.Label(root, text="Сортировка:")
sort_label.grid(row=1, column=1)

sort_column = StringVar()
sort_column.set(worksheet.row_values(1)[0])
sort_column_menu = OptionMenu(root, sort_column, *worksheet.row_values(1))
sort_column_menu.grid(row=1, column=2)

sort_order = StringVar()
sort_order.set("asc")
sort_order_menu = OptionMenu(root, sort_order, "asc", "desc")
sort_order_menu.grid(row=1, column=3)

sort_by_order_button = tk.Button(root, text="Сортировать по столбцу", command=sort_by_column)
sort_by_order_button.grid(row=1, column=4)

sort_button = tk.Button(root, text="Сортировать", command=sort_data)
sort_button.grid(row=1, column=5)

name_label = tk.Label(root, text="A:")
name_label.grid(row=3, column=0)

name_entry = Entry(root)
name_entry.grid(row=3, column=1)

age_label = tk.Label(root, text="B:")
age_label.grid(row=4, column=0)

age_entry = Entry(root)
age_entry.grid(row=4, column=1)

add_button = tk.Button(root, text="Добавить", command=add_row)
add_button.grid(row=5, column=0)

index_label = tk.Label(root, text="Индекс:")
index_label.grid(row=5, column=1)

index_entry = Entry(root)
index_entry.grid(row=5, column=2)

edit_button = tk.Button(root, text="Редактировать", command=edit_row)
edit_button.grid(row=5, column=3)

delete_button = tk.Button(root, text="Удалить", command=delete_row)
delete_button.grid(row=5, column=4)

root.mainloop()
