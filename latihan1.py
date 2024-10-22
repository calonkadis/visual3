import PySimpleGUI as sg

# Data Mahasiswa
data = [
    ['NPM', '2310010529'],
    ['Nama', 'MUHAMMAD HIKMATULLAH'],
    ['Kelas', '3A NONREG BANJARMASIN'],
    ['Mata Kuliah', 'PEMROGRAMAN VISUAL 3']
]

# Layout GUI
layout = [
    [sg.Text('Informasi Mahasiswa', font=('Arial', 30, 'bold'))],
    [sg.Table(values=data, headings=['Keterangan', 'Isi'], auto_size_columns=True, justification='center')],
    [sg.Button('Tutup')]
]

# Membuat Window
window = sg.Window('Latihan Pertama', layout, size=(400, 200))

# Event Loop
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Tutup':
        break

window.close()
