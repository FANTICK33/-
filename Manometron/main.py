import gspread
import tk as tk
from tk import *
from tk import messagebox


gs = gspread.service_account(filename='credentials.json')
sheet = gs.open_by_key('1uClkxjKnIHsnrjAp9NKGjirv8v24uQItZ1v7z8DE8dk')
worksheet = sheet.sheet1

res = worksheet.get_all_records()

root = tk.Tk()
root.title("Google Sheets Editor")
root.geometry("1000x500")

def view_data():
    data = worksheet.get_all_values()
    for row_index, row in enumerate(data):
        for col_index, value in enumerate(row):
            cell = Label(root, text=value)
            cell.grid(row=row_index+1, column=col_index)

def add_row():
    new_name = name_entry.get()
    new_age = age_entry.get()
    worksheet.append_row([new_name, new_age])
    messagebox.showinfo("Добавить запись", "Запись успешно добавлена!")

def edit_row():
    index = int(index_entry.get())
    new_name = name_entry.get()
    new_age = age_entry.get()
    worksheet.update(f"A{index}", new_name)
    worksheet.update(f"B{index}", new_age)
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

view_button = Button(root, text="Просмотреть", command=view_data)
view_button.grid(row=0, column=0)

sort_label = Label(root, text="Сортировка:")
sort_label.grid(row=1, column=0)

sort_column = StringVar()
sort_column.set(worksheet.row_values(1)[0])
sort_column_menu = OptionMenu(root, sort_column, *worksheet.row_values(1))
sort_column_menu.grid(row=1, column=1)

sort_order = StringVar()
sort_order.set("asc")
sort_order_menu = OptionMenu(root, sort_order, "asc", "desc")
sort_order_menu.grid(row=1, column=2)

sort_button = Button(root, text="Сортировать", command=sort_data)
sort_button.grid(row=1, column=3)

name_label = Label(root, text="Имя:")
name_label.grid(row=2, column=0)

name_entry = Entry(root)
name_entry.grid(row=2, column=1)

age_label = Label(root, text="Возраст:")
age_label.grid(row=3, column=0)

age_entry = Entry(root)
age_entry.grid(row=3, column=1)

add_button = Button(root, text="Добавить", command=add_row)
add_button.grid(row=4, column=0)

index_label = Label(root, text="Индекс:")
index_label.grid(row=4, column=1)

index_entry = Entry(root)
index_entry.grid(row=4, column=2)

edit_button = Button(root, text="Редактировать", command=edit_row)
edit_button.grid(row=4, column=3)

delete_button = Button(root, text="Удалить", command=delete_row)
delete_button.grid(row=4, column=4)

root.mainloop()
