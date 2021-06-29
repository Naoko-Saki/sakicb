import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Button
import pandas as pd
import csv
from datetime import date


def nyuryoku():
    today1 = date.today()
    today2 = today1.isoformat()

    word = today2,values['input_details'],values['input_spent']

    with open(values['kiroku_File_Path'],'a', newline='') as f :
        writer = csv.writer(f)
        writer.writerow(word)

def spent(selfile):
    df= pd.read_csv(selfile)
    totalam = df['spent'].sum()
    print(f'この月は{totalam}円使っています')
    return df

def details(selectfile):
    with open(selectfile,'r') as f :
        reader = csv.reader(f)
        for line in reader:
            print(line)
        return reader



sg.theme('DarkTeal3')

layout = [  [sg.Text('Cash Book')],
            [sg.Text('記録ファイル指定してね')],
            [sg.Text('File', size=(5,1)), sg.Input(), sg.FileBrowse('Select a file',key='kiroku_File_Path')],
            [sg.Button('これまでの合計は',key='read_kiroku')],
            [sg.Text('用途と金額を入力してね')],
            [sg.Text('用途',size=(5,1)), sg.InputText(key='input_details'), sg.Text('金額',size=(5,1)), sg.InputText(key='input_spent'),sg.Text('円'),sg.Button('入力OK!',key='detail_spent')],
            [sg.Button('合計金額を見る',key='now_spent'),sg.Button('詳細表示する',key='thism_spent')],
            [sg.Text('見たいファイル指定してね')],
            [sg.Text('File', size=(5,1)), sg.Input(), sg.FileBrowse('Select a file',key='read_File_Path')],
            [sg.Button('詳細表示する',key='read'),sg.Button('合計金額を見る！!',key='then_spent')],
            [sg.Output(size=(70,20))],
            [sg.Button('Quit')]
]

window = sg.Window('My Cash Book', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Quit':
        break

    if event == 'read_kiroku':
        sf = spent(values['kiroku_File_Path'])

    if event == 'detail_spent':
        print(values['input_details'],values['input_spent']+'円')
        nyuryoku()

    if event == 'now_spent':
        ns = spent(values['kiroku_File_Path'])

    if event == 'thism_spent':
        tm = details(values['kiroku_File_Path'])

    if event == 'read':
        miru= details(values['read_File_Path'])
    
    if event == 'then_spent':
        mimiru = spent(values['read_File_Path'])



window.close()
