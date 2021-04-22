import sqlite3
from uuid import uuid1
from datetime import datetime

def init(this, file, table_name):
    this.file = file
    this.table = table_name
    connect = sqlite3.connect(str(file))
    connect.close()
def current_time(this):
    times = datetime.now()

    year = times.year
    month = times.month
    day = times.day

    hour = times.hour
    minute = times.minute
    second = times.second
    
    if len(str(minute)) < 2:
        minute = f"0{minute}"

    if len(str(hour)) < 2:
        hour = f"0{hour}"

    mod_time = f"{year}/{month}/{day}/{hour}/{minute}/{second}"
    return mod_time
class ControlElementStorage():
    def __init__(self, file, table_name):
        init(self, file, table_name)

    def write(self, name:str, put_type:str, value_type:str):
        connect = sqlite3.connect(str(self.file))
        cursor = connect.cursor()
        exe = f"""INSERT INTO {self.table} (name, put_type, value_type) VALUES 
        ('{name}', '{put_type}', '{value_type}')
        """
        cursor.execute(exe)
        connect.commit()
        connect.close()

    def create_table(self):
        connect = sqlite3.connect(str(self.file))
        cursor = connect.cursor()
        
        cursor.execute(f"""
        CREATE TABLE ControlElements (
        name       TEXT PRIMARY KEY,
        put_type   TEXT,
        value_type TEXT
        );
        """)
        connect.commit()
        connect.close()

    def clear(self):
        connect = sqlite3.connect(str(self.file))
        cursor = connect.cursor()

        cursor.execute(f"DELETE FROM {self.table}").fetchall()

        connect.commit()
        connect.close()

    def delete_elements(self):
        connect = sqlite3.connect(str(self.file))
        cursor = connect.cursor()

        cursor.execute(f"""
        DELETE FROM {self.table}
        """).fetchall()

        connect.commit()
        connect.close()

    def update_element(self, name:str, state:str):
        #update name and path, choose file by UUID

        connect = sqlite3.connect(str(self.file))
        cursor = connect.cursor()

        exe = f"""UPDATE {self.table} set state = '{state}' where name = '{name}'"""
        print(exe)
        cursor.execute(exe)

        connect.commit()
        connect.close()
    
    def availability(self, name):
        connect = sqlite3.connect(str(self.file))
        cursor = connect.cursor()

        exe = f"""SELECT * FROM {self.table} where name = '{name}'"""
        return bool(cursor.execute(exe).fetchall())
        connect.close()


if __name__ == "__main__":
    db_path = "./data/control-elements-state.db"
    storage = ControlElementStorage(db_path, "ControlElements")