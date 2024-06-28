import tkinter as tk
from tkinter import ttk
import os
from tkinter import filedialog
from tkinter import messagebox
import pandas as pd
from pathlib import Path

class MainApp(tk.Frame):
    def __init__(self,parent,*args,**kwargs):
        tk.Frame.__init__(self,parent,*args,*kwargs)
        self.parent=parent

def ref_dir():
    base_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = tk.filedialog.askdirectory(initialdir=base_dir)
    input_dir.set(file_path)

def export_xlsx():
    dir_name = input_dir.get()
    sheet_name =input_sheet.get()
    file_name = input_name.get()

    if dir_name =="":
        messagebox.showerror("ERROR","フォルダを選択してください")
        return
    if sheet_name == "":
        messagebox.showerror("ERROR", "シート名を入力してください")
        return
    if file_name == "":
        messagebox.showerror("ERROR", "ファイル名を入力してください")
        return

    exl_dir = Path(dir_name) # excelsのパスを取得
    file_list = list(exl_dir.glob('*.xlsx'))  # パスからファイル名をリスト化して取得

    if file_list == []:
        messagebox.showerror("ERROR","指定したフォルダ内にファイルがありません")
        return
    all_df_list = []  # リストの宣言
    flag = False

    for file in file_list:# ファイルをひとつづつ読み込んで一つの変数にまとめる
        xls = pd.ExcelFile(file)
        sheet_names = xls.sheet_names
        for name in sheet_names:
            if sheet_name == name:
                df = xls.parse(sheet_name)
                print(df)
                all_df_list.append(df)
                flag = True

        if flag == False:
            messagebox.showerror("ERROR", "指定されたシート名がファイル内に存在しません")
            return

    # df = pd.concat(all_df_list)

    with pd.ExcelWriter(file_name+'.xlsx') as writer:  # リスト化されたデータを一つのファイルにまとめ出力
        for i in range(len(file_list)):
            all_df_list[i].to_excel(writer, sheet_name=file_list[i].stem)
    messagebox.showinfo("INFO","ファイルが出力されました")


root =tk.Tk()
root.title('sample')
root.geometry("375x200")

frame_dir= ttk.Frame(root,padding=10)
frame_dir.grid(row=0,column=1,sticky=tk.W + tk.E)
dir_label = ttk.Label(frame_dir,text='参照するフォルダ')
dir_label.pack(side=tk.LEFT)
input_dir=tk.StringVar()
dir_entry=ttk.Entry(frame_dir,width=30,textvariable=input_dir)
dir_entry.pack(side=tk.LEFT)
dir_button = ttk.Button(frame_dir, text='参照',command=ref_dir)
dir_button.pack(side=tk.RIGHT)

frame_sheet= ttk.Frame(root,padding=10)
frame_sheet.grid(row=2,column=1,sticky=tk.W + tk.E)

sheet_label = ttk.Label(frame_sheet,text='参照するシート名  ')
sheet_label.pack(side=tk.LEFT)

input_sheet=tk.StringVar()
sheet_entry=ttk.Entry(frame_sheet,width=30,textvariable=input_sheet)
sheet_entry.pack(side=tk.RIGHT)

frame_name= ttk.Frame(root,padding=10)
frame_name.grid(row=4,column=1,sticky=tk.W + tk.E)

name_label = ttk.Label(frame_name,text='作成ファイル名     ')
name_label.pack(side=tk.LEFT)

input_name=tk.StringVar()
name_entry=ttk.Entry(frame_name,width=30,textvariable=input_name)
name_entry.pack(side=tk.RIGHT)

frame_ok= ttk.Frame(root,padding=10)
frame_ok.grid(row=6, column=1,sticky=tk.W + tk.E)

ok_button = ttk.Button(frame_ok, text='ok',command=export_xlsx)
ok_button.pack(side=tk.LEFT)

app = MainApp(root)


app.mainloop()



