import requests # htmlを取得
from bs4 import BeautifulSoup # HTML解析、スクレイピング

# 対象のURLを取得
url = "https://suumo.jp/jj/chintai/ichiran/FR301FC001/?ar=030&bs=040&ta=13&sc=13123&cb=0.0&ct=9999999&et=9999999&cn=9999999&mb=0&mt=9999999&shkr1=03&shkr2=03&shkr3=03&shkr4=03&fw2=&srch_navi=1"

#何ページかある場合この処理をしておくとforループを使う時にいいらしい
target_url = url.format(1)

res = requests.get(target_url) # レスポンス取得
soup = BeautifulSoup(res.text) # ＨTML解析

#抽出したい情報のタグやクラスは検証で確認
contents = soup.find_all('div',class_='cassetteitem_content')

#find_all()で取得した結果は、Pythonリスト形式になっているので、len()を使えば中身の要素数を確認できる
len(contents)

# 1ページ目
content = contents[0]

# 欲しい情報を取得
title = content.find('div',class_='cassetteitem_content-title').text
address = content.find('li',class_='cassetteitem_detail-col1').text
access = content.find('li',class_='cassetteitem_detail-col2').text
age = content.find('li',class_='cassetteitem_detail-col3').text

#情報が取得できているか確認
title,address,access,age


## ↓↓csvファイルに出力する処理を追加

# csvファイルへの出力やデータの整理が出来るライブラリ？
import pandas as pd
from pandas import Series, DataFrame

# オブジェクトに変換？
title = Series(title)
address = Series(address)
access = Series(access)
age = Series(age)

# データを一列追加
suumo_df = pd.concat([title, address, access, age], axis=1)
# カラム名を指定
suumo_df.columns = ['タイトル', '住所', 'アクセス', '築年数']
# csvファイルに出力
suumo_df.to_csv('suumo.csv', sep = '\t', encoding='utf-16', header=True, index=False)