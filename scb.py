import csv
from datetime import date

import PySimpleGUI as sg


def nyuryoku() -> None:
    today = date.today().isoformat()

    word = today, values['input_details'], values['input_spent']

    with open(values['kiroku_file_path'], 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(word)

def spent(selfile) -> None:
    cb_list = []

    f = open(selfile,'r')

    rows = csv.reader(f)

    for row in rows:
        cb_list.append(row[2])

    del cb_list[0]
    nwlist = [int(i) for i in cb_list]
    totalam = sum(nwlist)
    print(f"この月は{totalam}円使っています")

    f.close()

    

def details(selectfile) -> None:
    with open(selectfile, 'r') as f :
        reader = csv.reader(f)
        for line in reader:
            print(line)
        

sg.theme('DarkTeal3')

layout = [  
    [sg.Text('Cash Book')],
    [sg.Text('記録ファイル指定してね')],
    [sg.Text('File', size=(5,1)), sg.Input(), sg.FileBrowse('Select a file', key='kiroku_file_path')],
    [sg.Button('これまでの合計は', key='read_kiroku')],
    [sg.Text('用途と金額を入力してね')],
    [sg.Text('用途',size=(5,1)), sg.InputText(key='input_details'), sg.Text('金額', size=(5,1)), sg.InputText(key='input_spent'), sg.Text('円'), sg.Button('入力OK!', key='detail_spent')],
    [sg.Button('合計金額を見る', key='now_spent'), sg.Button('詳細表示する', key='thism_spent')],
    [sg.Text('見たいファイル指定してね')],
    [sg.Text('File', size=(5,1)), sg.Input(), sg.FileBrowse('Select a file', key='read_file_path')],
    [sg.Button('詳細表示する', key='read'), sg.Button('合計金額を見る！!', key='then_spent')],
    [sg.Output(size=(70, 20))],
    [sg.Button('Quit')]
]

window = sg.Window('My Cash Book', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Quit':
        break

    if event == 'read_kiroku':
        spent(values['kiroku_file_path'])

    if event == 'detail_spent':
        print(f"Added {values['input_details']}: {values['input_spent']}円")
        nyuryoku()

    if event == 'now_spent':
        spent(values['kiroku_file_path'])

    if event == 'thism_spent':
        details(values['kiroku_file_path'])

    if event == 'read':
        details(values['read_file_path'])
    
    if event == 'then_spent':
        spent(values['read_file_path'])

window.close()

