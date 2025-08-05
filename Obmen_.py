import requests
import json
from tkinter import *
from tkinter import messagebox as mb


def exchange();






window = Tk()
window.title('Курсы валют')
window.geometry('360x180')

Label(text='введитке код валюты').pack(padx=10, pady=10)

entry = Entry()
entry.pack(padx=10, pady=10)

Button(text='Получить курс обмена к доллару', command=exchange).pack(padx=10, pady=10)

window.mainloop()


