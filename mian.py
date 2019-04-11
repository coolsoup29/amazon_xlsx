# write the message from t2 to xlsx
# add pic to xlsx from ./img
# author:coolsoup29
# time:20190411

import xlsxwriter
import pymysql
from PIL import Image


def cnn_db():
    db=pymysql.connect('111.230.10.127','root','coolsoup','test',charset='utf8')
    return db

def start(f_type):
    db=cnn_db()
    cur=db.cursor()
    sel_sql='select * from t2 where type="%s" and rank!=0 order by rank;'%f_type
    cur.execute(sel_sql)
    data=cur.fetchall()
    print(len(data))
    db.close()
    workbook = xlsxwriter.Workbook('./file/%s.xlsx' % f_type)

    worksheet = workbook.add_worksheet('first_sheet')
    for msg in data:
        index = data.index(msg)
        try:

            img = Image.open('./img/%s.png' % msg[2])
            img = img.resize((80, 80))
            img.save('./img2/%s.png' % msg[2])
            # img.save()
            worksheet.insert_image(index, 0, './img2/%s.png' % msg[2])
        except Exception as e:
            print(e)
            worksheet.write(index, 0, 'NONE')
        worksheet.write(index, 1, msg[2])
        worksheet.write(index, 2, msg[3])
        worksheet.write(index, 3, msg[4])
        worksheet.write(index, 4, msg[5])
    workbook.close()

    print("DONE!")

for s in ['girl']:  #'men','women','boy',
    print("正在写入%s的表格"%s)
    start(s)