import traceback
import pymysql

#增：insert


def insert():
    conn = pymysql.connect('localhost','root','root','bbs')
    cursor = conn.cursor()
    sql = "insert into bbs values(0, '这是一个备忘录2', 'bub', now(), 0);"
    try:
        cursor.execute(sql)
        conn.commit()
        last_id = cursor.lastrowid
        print(last_id)
    except:
        traceback.print_exc()
        conn.rollback()
    finally:
        conn.close()

#改：update
def update():
    conn = pymysql.connect('localhost', 'root', 'root', 'bbs')
    cursor = conn.cursor()
    sql = "update bbs set contents='备忘录' where id=0;"
    try:
        cursor.execute(sql)
        conn.commit()
    except:
        traceback.print_exc()
        conn.rollback()
    finally:
        conn.close()

#查select
def select():
    conn = pymysql.connect('localhost', 'root', 'root', 'bbs')
    cursor = conn.cursor()
    sql = "select * from bbs where name='Tom';"
    try:
        cursor.execute(sql)
        #ret = cursor.fetchone()
        #ret = cursor.fetchmany(3)
        ret = cursor.fetchall()
        for i in ret:
            print(i)
    except:
        traceback.print_exc()
        conn.rollback()
    finally:
        cursor.close()
        conn.close()


#删：delete
def delete():
    conn = pymysql.connect('localhost', 'root', 'root', 'bbs')
    cursor = conn.cursor()
    sql = "update bbs set is_delete=1 where id=0;"
    try:
        cursor.execute(sql)
        conn.commit()
    except:
        traceback.print_exc()
        conn.rollback()
    finally:
        cursor.close()
        conn.close()


insert()
update()
select()
delete()
