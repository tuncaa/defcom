import requests
import sqlite3

def ComDBM(dbname,SQL,dataset):
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    if len(dataset) == 0 :
        c.execute(SQL)
    elif len(dataset) == 1 :
        c.execute(SQL, dataset)
    else:
        c.executemany(SQL,dataset)
    out = c.fetchone()
    conn.commit() #dbの変更を反映
    conn.close()
    return out

# 引数1:対象URL 2:method今のところデフォルトgetのpostのみ例外処理
# def ComDL(URL,method,para,):
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.99 Safari/537.36"
#     }
