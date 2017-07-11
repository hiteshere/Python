from mydb import MyDB
import pytest

@pytest.fixture(scope="module")
def cur():
    db = MyDB()
    conn = db.connect("server")
    curs = conn.cursor()
    # return curs
    yield curs
    curs.close()
    conn.close()

def test_johns_id(cur):
    # db = MyDB()
    # conn = db.connect("server")
    # cur = conn.cursor()
    id = cur.execute("select id from employee_db where name = John")
    assert id == 123

def test_tom_id(cur):
    # db = MyDB()
    # conn = db.connect("server")
    # cur = conn.cursor()
    id = cur.execute("select id from employee_db where name = Tom")
    assert id == 789