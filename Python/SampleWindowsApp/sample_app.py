# Tkinterライブラリのインポート
import tkinter

# アプリの作成
app = tkinter.Tk()

# アプリの画面設定
app.geometry(
    "400x400" # アプリ画面のサイズ
)
app.title(
    "アプリのタイトル" # アプリのタイトル
)

##### 〜処理を記述する場所〜 #####

# ボタンクリック時に実行する関数
def click_func():
    global label
    # ラベルの表示テキストを変更
    label[ "text"] = "クリックされました"


# ラベルを作成
label = tkinter.Label(
    app, # ラベルの作成先アプリ
    font = ("System", 30), # ラベルのフォント
    text = "ラベルです" # ラベルに表示するテキスト
)
label.place(
    x = 50, # ラベルの配置先座標x
    y = 50, # ラベルの配置先座標y
)

# ボタンクリックのイベント受付
# ボタンを作成
button = tkinter.Button(
    app, # ボタンの作成先アプリ
    text = "ボタン", # ボタンに表示するテキスト
    command = click_func # ボタンクリック時に実行する関数
)
# ボタンの配置
button.place(
    x = 100, # ボタンの配置先座標x
    y = 100, # ボタンの配置先座標y
)

# アプリの待機
app.mainloop()