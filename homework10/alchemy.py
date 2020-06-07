from sqlalchemy.sql.functions import now

from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

HOSTNAME = "127.0.0.1"
PORT = "3306"
DATABASE = "bbs"
USERNAME = "root"
PASSWORD = "root"

DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8". \
    format(username=USERNAME, password=PASSWORD, host=HOSTNAME, port=PORT, db=DATABASE)

engine = create_engine(DB_URI)

Base = declarative_base(engine)
session = sessionmaker(engine)()


class Bbs(Base):
    __tablename__ = "bbs"
    id = Column(Integer(11), primary_key=True, autoincrement=True)
    contents = Column(Text)
    name = Column(String(45))
    time = Column(DateTime)
    is_delete = Column(Integer(1))


    def __str__(self):
        return "<Article(name %s,contents %s,time %s)>" % (self.name, self.contents,self.time)


# 添加数据
def add_data():
    bbs1 = Bbs(contents='你好', name='jacy',time=now(),is_delete=0)

    session.add(bbs1)
    session.commit()

# 删除数据
def delete_data():
    bbs = session.query(Bbs).filter_by(name='jacy').all()
    for p in bbs:
        session.delete(p)
    session.commit()

# 更改数据
def update_data():
    bbs = session.query(Bbs).first()
    bbs.contents = "修改内容"
    session.commit()

def select_data():
    # 查询所有数据
    all_bbs = session.query(Bbs).all()
    for p in all_bbs:
        print(p)
