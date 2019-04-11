# download the pic from asin_table
# coolsoup29
# 20190411


import multiprocessing,requests
from setting import *
import pymysql



def cnn_db():
    print("正在连接数据库...")
    db=pymysql.connect('*.*.*.*','user','pwd','db',charset='utf8')
    cur=db.cursor()
    cur.execute('select img,asin from asin_table where id>88541;')
    img_data=cur.fetchall()
    db.close()
    print("数据下载成功!")
    return img_data



def down(msg):
    req=requests.get(msg[0],headers=headers_img)
    content = req.content
    with open("./img/%s.png"%msg[1],'wb') as f:
        f.write(content)
        print(msg[1],'has down!')



def mul_start():
    data=cnn_db()
    p = multiprocessing.Pool(128)
    for msg in data:  # data 是要多进程处理的参数
        p.apply_async(down, args=(msg,))
    print('正在多进程抓取写入第goods层链接')
    p.close()
    p.join()
    print('第goods层链接写入完成!')
    print("line to mysql..")

if __name__ == '__main__':
    mul_start()
