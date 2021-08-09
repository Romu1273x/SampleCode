# module import
import datetime # 日付や時間を取得するモジュール
import smtplib, ssl # メールサーバを操作してメール送信することができるモジュール,　暗号化の仕組みを使うためのモジュール
from email.mime.text import MIMEText # メールを日本語で送信できるようにするためのモジュール

# エンコードエラー回避のため、エンコードを指定
#import sys, codecs
#sys.stdout = codecs.getwriter("utf-8")(sys.stdout)

# googleアカウントログイン
gmail_account = "xxxx@gmail.com"
gmail_password = "password"

# メール内容
mail_to = "xxxx@yahoo.co.jp"
name = "name"
today_date = datetime.date.today()
subject = "{0}様、xxxx".format(name)
body = "{0}\nxxxx。".format(today_date)

# メール設定
msg = MIMEText(body, "html")
msg["Subject"] = subject
msg["To"] = mail_to
msg["From"] = gmail_account

# メール送信
server = smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ssl.create_default_context())
server.login(gmail_account, gmail_password)
server.send_message(msg)
print("送信完了")