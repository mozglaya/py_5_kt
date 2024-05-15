import csv
from datetime import date, datetime
import tkinter as tk
from tkinter import Tk, Label

today = date.today()

events = []

with open('data.csv', encoding='utf-8') as fp:
    plans = csv.DictReader(fp, delimiter = ";")
    for row in plans:
        events.append(list(row.values()))

def to_do(events):
    calendar = []
    for event in events:
        event[0] = datetime.strptime(event[0], '%Y-%m-%d').date()
        if event[0] < today:
            td = today - event[0]
            calendar.append(f'Прошло {td.days} дней от события "{event[1]}"')
        if event[0] > today:
            td = event[0] - today
            calendar.append(f'Осталось {td.days} дней до события "{event[1]}"')
        if event[0] == today:
            calendar.append(f'Прямо сейчас проходит событие "{event[1]}"')
    return calendar

output = to_do(events)

root = Tk()

root.title("Важные дела")
root.geometry("700x300")
root['bg'] = 'black'

label = Label(
    text='Мои планы:',
    font=("Courier", 30),
    bg='black'
)
label.pack()

plans_var = tk.StringVar(value=output)

listbox = tk.Listbox(
root,
listvariable=plans_var,
width=55,
font=('Courier', 20),
justify='center',
bg='black'
)

for item in range(4):
    listbox.itemconfig(item, {'fg':'red'})
listbox.itemconfig(4, {'fg':'yellow'})
for item in range(5, 9):
    listbox.itemconfig(item, {'fg':'green'})
listbox.pack()

root.mainloop()