# モジュール
- クラスや関数をひとまとめにしたもの
- 別途インストールが必要なものもある
## インポート表記法				
- `import モジュール名`			  
 			  
- `import モジュール名 as 別名`で別名をつけられる
- 使用するときは
    - `モジュール名.関数名`
    - `別名.関数名`

# python中級
## エクセルの読み書き、操作
### pandas概要
#### 柔軟にデータ処理ができるツール
- モジュール
    - いろんなクラス、関数がひとまとめになってるもの
- インストール
    - 設定のインタープリターからインストールできる
### pndasによるエクセルのよみかき
- read_exel()で読み書きができる。引数は’ファイル名’
	- 基本的にはシート1が読み込まれる
	- シートを指定する場合
        ```  
        sheet_name='aaa'
        ```
	- すべて読み込む場合
        ``` 
        sheet_name=None
        ```
	で読み込める
	- すべて読み込んだ場合はdictionaryになっている。
        ```
        key = sheet_name
        value = sheet_value
        ```
    - そのほかにも操作として
	    ```
        skiprows=[2]    :最初の二行目をスキップ
	    skipfooter=4    :最後の４行をスキップ
	    usecols="A:C"   :A~Cのみを取得
        ```
	- データを１行ずつ確認する場合
		```
        for index in df.iterrows():
		    print(index, row)	#index=行番号、row=データ
        ```
- 集計
	```
    df.query('work' > 8)
	    all_df = concat(df)
    ```
    で複数シートを一つにまとめる
- 書き込み
	```
    df.to_exel('sample.xlsx')
	index=False
	header=False
    ```
	- 複数シートをまとめる場合
	    ```
        with pd.ExcelWriter(sample.xlsx)as writer:
	    df1.to_excel(writer,sheet_name=test1)
	    df2.to_excel(writer,sheet_name=test2)
        ```

### 課題
- タイムカードの必要なシートを一つをまとめる
- フォルダ内のエクセルファイルを一覧で取得
- Path,globを使う
- 各エクセルファイルの特定のシートを取得
- すべてを一つのファイルにまとめる


## Kinterを用いた簡易のGUIアプリ作成
### Tkinter概要
- GUIアプリ開発モジュール
- Tkというツールを呼び出している
- ウィンドウを立ち上げて機能するアプリがGUI
### 使い方
```
import tkinter as tk

root=tk.Tk()				        #アプリ用のクラスをインスタンス(オブジェクト)化
root.title("sample")			    #アプリ名の指定
root.geometry("300x400+100+200")	#サイズ(x)とアプリの軌道座標(+)を指定できる
roor.mainloop()
w=root.winfo_screenwidth()		    #使ってるモニターの横幅を取得
h=root.winfo_screenheight()		    #使ってるモニターの高さを取得
root.geometry(f"{w}x{h}")
```

### TKinter基本機能
#### フレーム
- tkinterにはフレームというものがある
    ```
    frame = ttk.Frame(root, padding=10)		#フレームの設定（定義）
    frame.pack()					        #フレームをアプリ上に挿入
    button=ttk.Button(flame,text='button')	#ボタンの追加
    button.pack()					        #ボタンをアプリ上に追加
    ```

- 変数の名前を変えれば何回でも追加できる
- ほかにもいろんな機能を追加できる
    ```
    frame.grid(row=0,column=0)		#packは上から詰めてく、gridはどこに置くか指定できる
    ```

- オブジェクト指向的にはクラスを継承して書く
    ```
    class MainApp(tk.Frame):
        def __init__(self,parent,*args,**kwargs):
            tk.Frame.__init__(self,parent,*args,*kwargs)
            self.parent=parent

    root=tk.Tk()
    root.title=("sample")
    app=MainApp(root)
    app.mainloop()
    ```

- 複雑な処理の場合クラスの継承をしたほうがいい
<br>- **継承**
    - 大規模な開発等では条件分岐の代わりに使われる。
    - クラスのオーバーライド（親クラスのメソッドの上書き）や必要最低限の加筆修正などを目的に作られる

#### ラベル
- フレーム内にテキストを表示
    ```
    label = ttk.Label(frame, text='aaa')
    ```
#### ボタン
- フレーム内にボタンを配置
    - #commandでは、どの処理を行うか指定する（関数）
        ```
        button=ttk.Button(frame,text='aaa'command=bt)	
        ```
#### エントリー
- 入力の受け付け
    ```
    df bt:
        print(input.get())
        return
    
    text_input=tk.StirnVar()			#入力を代入する変数
    entry=ttk.Entry(frame,textvariable=text_input)	#入力の受け付け
    ```
#### チェックボックス
- チェックボックスの表示
    ```
    df bt:
        print(input.get())
        return

    input=tk.StringVar()				#チェックボックスの入力を代入する変数
    check=ttk.Dheckbutton(frame,			
        variable=input,command=bt)			
    ```
#### スケール
- スケール（スライダー）の表示
    ```
    input=tk.DoubleVer()
    scale=ttk.Scale(
        frame,variable=input,command=bt,		
        length=200,from_=0,to=255)			#length=バーの長さ、from_=値の最小値、to=最大値
    ```

### 便利な機能
- ファイルダイアログ
	```
    file_type=[("データファイル","*.csv")]
	base_dir=os.path.abspath(os.path.dirname(__file__))
	file_path=tk.filedialog.askopenfilename(		#askdirectoryにするとフォルダを検索できる
		filetypes=file_type,intialdir=base_dir)
	input.set(file_path)
    ```
- メッセージボックス
	```
    if XXXXX:
		messagebox.showerror("title","text")
	else:
		messagebox.showinfo("title","text")
    ```

### 課題
前回のアプリをGUI化
- フォルダ選択
- まとめるシート名
- 作成ファイル名
<br>のダイアログを追加する


## matplotlibを用いたグラフ作成方法
### matplotlib概要
- pythonで柔軟なグラフ生成を行うことができる
#### インストール
- 設定からインタープリターでインストール
#### サンプルデータ
- csvファイルを作成する
#### モジュールの使用方法
- For Example...
    ```
    import matplotlib.pyplot as plt
    import pandas as pd

    df = pd.read_csv('sample.csv')

    fig = plt.figure()
    ax = fig.add_subplot()

    ax.plot(df['month'],df['sales'])
    plt.show()
    ```

## 基本機能
### 描画領域全体を作成
- plt.figure()でグラフの表示領域全体を管理する
- Figureオブジェクトを作成する

    ```
    fig = plt.figure()
    plot.show()
    ```
- これを実行すると白紙が表示される

### 各グラフ領域の作成
- Figureオブジェクトに対して`add_subplot()`で、実際にグラフの領域（メモリ）を管理するAxesオブジェクトを作成する
    ```
    fig = plt.figure()
    ax = fig.add_subplot()

    plot.show()
    ```

### 折れ線グラフの作成
- `plot(x,y)`でx,y情報をもとに折れ線グラフを作成
    ```
    df = pd.read_csv('sample.csv')

    fig = plt.figure()
    ax = fig.add_subplot()

    ax.plot(df['month'],df['sales'])
    plt.show()
    ```
### グラフの保存
- 画像ファイルとして保存ができる
    ```
    plt.savefig('output.png')
    ```

### 表示サイズの変更
- `plt.figure()`に引数を与えることで表示サイズの変更が行える
    ```
    fig = plt.figure(figsize=[6,8])
    ```
- この例だと横：６インチ、縦：８インチのグラフが作成される

### タイトル設定
- グラフにタイトルを設定できる
    ```
    fig.suptitle('sample result')
    ```
### x,y軸のラベル付け
- `Axes.set_xlabel,ylabel()`でx,y軸にラベルを設定できる
    ```
    ax.set_xlabel('month')
    ax.set_ylabel('sales')
    ```
### 複数データの重ね合わせ
- `axes.plot()`を複数実行すると複数グラフを表示できる
- オプションで色の設定ができる

### 凡例表示
- `Axes.plot()`にラベル引数を追加すると凡例を表示できる
    ```
    ax.plot(df['month'],df['sales'],lanel='this year')
    ax.legend()
    ```
## 様々な形式のグラフ作成
### 散布図
- 各値を点で表示するグラフ
- `axes.scatter()`で散布図を作成できる
    ```
    ax.scatter(df['month'],df['sales'])
    ```

### ヒストグラム
- 各値のカウントを表示するグラフ
- `Axes.hist()`でグラフを作成できる
    ```
    ax.hist(df['sales'])
    ```

### 円グラフ
- 比率を見る円グラフを作成
- `Axes.pie()`で円グラフを作成できる
    ```
    ax.pie(df['sales'],label=df['month'])
    ```

### 棒グラフ
- 値を比較するグラフ
- `Axes.bar()`でグラフを作成できる
    ```
    ax.bar(df['month'],df['sales'])
    ```

- 積み上げグラフも作成できる
    ```
    ax.bar(df['month'],df['sales'])
    ax.bar(df['month'],df['previous_sales']
	    bottom=df['sales'])
    ax.legend(['this_year','previous_year'])
    ```
- bottom引数によって積み上げを表現できる
### 複数グラフを表示
- 一つの領域に複数のグラフを表示できる
- `add_subplot(行サイズ、列サイズ、配置番号)`を指定して表示する
    ```
    ax1=fig.add_subplot(2,2,1)
    ax1.plot(df['month'],df['sales'])

    ax2=fig.add_subplot(2,2,2)
    ax2.plot(df['month'],df['previous_sales'])

    ax3=fig.add_subplot(2,2,3)
    ax3.bar(df['month'],df['sales'])

    ax4=fig.add_subplot(2,2,4)
    ax4.scatter(df['month'],df['previous_sales'])
    ```

## matplotlibの代案
### seaborn
- matplotlibをもとに作られた可視化モジュール
- matplotlibの比べて簡潔なコードでグラフが作成できる
    ```
    import matplotlib.pyplot as plt
    import seaborn as sns
    import pandas as pd

    df = pd.read_csv('sample.csv')

    sns.pairplot(df)
    plt.show()
    ```

### plotly
- plotlyは動的なグラフを作成できる
- グラフ生成後に拡大やカーソルを動かしながら表示を変更できる
- 基本的にブラウザ上で動く

    ```python:sample.py
    import plotly
    import plotly.graph_objs as go
    import pandas as pd

    df = pd.read_csv('sample.csv')

    plot_data=go.Scatter(x=df["month"],
    	y=df["sales"],mode='markers')

    fig=go.Figure(plot_data)
    fig.show()
    ```
## 課題
- 2019~2021における東京にどの程度人がいたか年代ごとに記録したデータ
    - 各地区(千代田区、中央区など)
    - 休日、平日、前日
    - 昼、深夜、終日年代
<br>を使用して折れ線グラフを作成
- 横軸に年月、縦軸に滞在人口をプロット
- 使用データは国土交通省の全国の人流オープンデータをもとに作成する
- 作成は前々回のexcelの要領で作成する

- 回答確認はまだ行っていない
- 明日はこの動画の演習から行う
# **Gitに上げる**