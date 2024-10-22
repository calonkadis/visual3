import PySimpleGUI as sg
sg.theme("DarkGreen4")
import tkinter as tk
from tkinter import Label

# Membuat jendela utama
root = tk.Tk()
root.title("Profile")
root.geometry("400x200")
root.configure(bg='#5A6473')

# Menampilkan label informasi dengan alignment kiri
Label(root, text="NPM              : 2310010529", font=("Arial", 12), bg='#5A6473', fg='white', anchor='w').place(x=20, y=20)
Label(root, text="Nama             : MUHAMMAD HIKMATUULAH", font=("Arial", 12), bg='#5A6473', fg='white', anchor='w').place(x=20, y=50)
Label(root, text="Kelas            : 5A NON REG BANJARMASIN", font=("Arial", 12), bg='#5A6473', fg='white', anchor='w').place(x=20, y=80)
Label(root, text="Mata kuliah      : PEMROGRAM VISUAL 3", font=("Arial", 12), bg='#5A6473', fg='white', anchor='w').place(x=20, y=110)

# Menjalankan loop jendela
root.mainloop()
