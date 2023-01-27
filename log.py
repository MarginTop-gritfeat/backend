import sqlite3
import time


def create_data(image = '', result = '', user_id = '', report = ''):
    u_id = int(time.time())
    data = {
        'id' : u_id,
        'image' : image,
        'result' : result,
        'user_id' : user_id,
        'report' : report,
        '_time' : u_id,
    }
    # print(data)
    return tuple(data.values())

# (id int autoincrement, image varchar(200), result varchar(50), user_id int, report varchar(100), _time integer)

def retrieve_all():
    db = sqlite3.connect('data.db')
    cursor = db.cursor()
    # data = create_data()
    cursor.execute('select * from prediction_log')   #pass tuple 
    data = cursor.fetchall()
    # db.commit()
    return data

def store(image = '', result = '', user_id = '', report = ''):
    db = sqlite3.connect('data.db')
    cursor = db.cursor()
    data = create_data(image = image, result = result, user_id = user_id, report = report)
    cursor.execute('insert into prediction_log(id, image, result, user_id, report, _time) values (?, ?, ?, ?, ?, ?)', data)   #pass tuple 
    # data = cursor.fetchall()
    db.commit()
    return cursor.rowcount

def retrieve(id):

    return 1

# print(store())

# print(retrieve_all())