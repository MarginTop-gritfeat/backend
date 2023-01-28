import sqlite3
# from flask import * 
import time
# import monitoring
import json


def create_data(image = '', relation = ''):
    u_id = int(time.time())
    data = {
        'id' : u_id,
        'image' : image,
        'relation' : relation,
        # 'user_id' : user_id,
        # 'report' : report,
        '_time' : u_id,
    }
    # print(data)
    return tuple(data.values())


def store(image = '', relation = ''):
    db = sqlite3.connect('data.db')
    cursor = db.cursor()
    data = create_data(image, relation * 100)
    cursor.execute('insert into monitor(id, image, relation, _time) values (?, ?, ?, ?)', data)   #pass tuple 
    # data = cursor.fetchall()
    db.commit()
    return cursor.rowcount

# id integer primary key, image varchar(200), relation float, _time integer 

def retrieve_all():
    db = sqlite3.connect('data.db')
    cursor = db.cursor()
    # data = create_data()
    cursor.execute('select * from monitor order by _time desc')   #pass tuple 
    data = cursor.fetchall()
    # print(data)
    # db.commit()
    return data

def calculate_result():

    return 1

# store()
# print(json.dumps(retrieve_all()))
