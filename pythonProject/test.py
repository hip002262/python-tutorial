import pandas as pd
from pathlib import Path

exl_dir = Path('excels')    #excelsのパスを取得
file_list = list(exl_dir.glob('*.xlsx'))     #パスからファイル名をリスト化して取得
print(file_list)

target_sheet = 'Sheet2'     #まとめるシートを指定
all_df_list = []        #リストの宣言
for file in file_list:       #ファイルをひとつづつ読み込んで一つの変数にまとめる
    df = pd.read_excel(file, sheet_name=target_sheet)
    print(df)
    all_df_list.append(df)

#df = pd.concat(all_df_list)

with pd.ExcelWriter('work.xlsx') as writer:     #リスト化されたデータを一つのファイルにまとめ出力
    for i in range(len(file_list)):
        all_df_list[i].to_excel(writer,sheet_name=file_list[i].stem)