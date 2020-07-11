import random, string
import datetime

DB = "db"
TB = "example"
COLUMNS = "(id,name,pwd)"
names = ["your selection of account names"]

def RandomProcedure(FixedDB):
    proc = []
    proc2 = []
    insert_count = random.choice(range(0,20))
    tb, table_creation = RandomTable()
    for _ in range(0, insert_count):
        proc.append(RandomInsert(tb))
    for _ in range(0, random.choice(range(0, 5))):
        proc.append(RandomSelectA(TB))
    for _ in range(0, random.choice(range(0, 5))):
        proc.append(RandomSelectB(TB,20))
    for _ in range(0, random.choice(range(0, 5))):
        proc.append(RandomSelectC(TB))
    for _ in range(0, random.choice(range(0, 5))):
        proc.append(RandomUpdateA(TB))
    for _ in range(0, random.choice(range(0, 5))):
        proc2.append(RandomSelectC(tb))
    for _ in range(0, random.choice(range(0, 5))):
        proc2.append(RandomSelectB(tb,insert_count))
    for _ in range(0, random.choice(range(0, 5))):
        proc2.append(RandomUpdateB(tb,insert_count))
    for _ in range(0, random.choice(range(0, 5))):
        proc2.append(RandomUpdateC(tb))
    #this_coin = random.choice([0,1])
    #proc.extend(SelectAdvanced(FixedDB,tb)) if this_coin else proc2.extend(SelectAdvanced(FixedDB,tb))
    random.shuffle(proc)
    random.shuffle(proc2)
    proc.extend(proc2)
    return table_creation,proc

def FixedProcedure(sqls,FixedDB=DB,FixedTB=TB):
    proc = []
    proc.append(CreateDB(FixedDB))
    proc.append(use_db(FixedDB))
    proc.append(FixedTable(FixedTB))
    for i in range(len(sqls)):
        proc.append(FixedInsert(FixedTB,sqls[i]))
    return proc

def RandomTable():
    name = random_char(5)
    this_sql = "CREATE TABLE "+ name + " (id smallint unsigned not null auto_increment, name varchar(32) not null, pwd varchar(32) not null, constraint pk_example primary key (id));"
    return name, this_sql

def FixedTable(FixedTB):
    this_sql = "CREATE TABLE " + FixedTB + " (id smallint unsigned not null auto_increment, name varchar(32) not null, pwd varchar(32) not null, constraint pk_example primary key (id));"
    return this_sql

def RandomInsert(tb):
    content1 = random_content()
    content2 = random_content()
    this_sql = "INSERT INTO " + tb + " (id,name,pwd) VALUES (null, '"+ content1 +"', '"+ content2 +"');"
    return this_sql

def FixedInsert(tb,sql,cols=COLUMNS):
    vals = ""
    for i in range(len(sql)-1):
        vals+= "'"+ str(sql[i])+ "', "
    vals+="'"+ str(sql[-1])+"'"
    this_sql = "INSERT INTO " + tb + " "+ cols + " VALUES (null, " + vals + ");"
    return this_sql

def RandomSelectA(tb):
    name = random.choice(names)
    this_sql = "SELECT * FROM " + tb + "  WHERE name=\""+ name +"\";"
    return this_sql

def RandomSelectB(tb,count):
    id = random.choice(range(0, count+1))
    this_sql = "SELECT * FROM " + tb + "  WHERE id=" + str(id) + ";"
    return this_sql

def RandomSelectC(tb):
    name = random_content()
    this_sql = "SELECT * FROM " + tb + "  WHERE name=\""+ name +"\";"
    return this_sql

def RandomUpdateA(tb):
    name = random.choice(names)
    new_pwd = random_content()
    this_sql = "UPDATE " + tb + " SET pwd=\""+ new_pwd +"\" WHERE name=\""+ name +"\";"
    return this_sql

def RandomUpdateB(tb,count):
    id = random.choice(range(0, count+1))
    new_pwd = random_content()
    this_sql = "UPDATE " + tb + " SET pwd=\""+ new_pwd +"\" WHERE id=" + str(id) + ";"
    return this_sql

def RandomUpdateC(tb):
    name = random_content()
    new_pwd = random_content()
    this_sql = "UPDATE " + tb + " SET pwd=\""+ new_pwd +"\" WHERE name=\""+ name +"\";"
    return this_sql

def SelectAdvanced(db,tb):
    return [GetTables(db), GetEntries(tb)]

def GetEntries(tb):
    this_sql = "SELECT * FROM " + tb + ";"
    return this_sql

def GetTables(db):
    this_sql = "SELECT table_name FROM information_schema.tables WHERE table_schema=\"" + db + "\";"
    return this_sql

def CreateDB(db):
    this_sql = "CREATE DATABASE "+ db + ";"
    return this_sql

def use_db(db):
    return "use "+ db +";"

def random_char(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))

def random_content():
    stringLength = random.choice(range(0, 30))
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(stringLength))
