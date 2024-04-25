import pymssql
from datetime import datetime
from enum import Enum

class Tables(Enum):
    Category = 'Category'
    Tag = 'Tag'
    Post = 'Post'
    Person = 'Person'
    Application = 'Application'
    Category_App = 'Category_App'
    Tag_App = 'Tag_App'
    Raiting = 'Raiting'
    Feedback = 'Feedback'

class Sql:
    # def __init__(self, database="REUCLOUD",server='127.0.0.1'):
        # self.cnxn = pymssql.connect(server=server, port=1444, user='sa', password='Password123', database=database)
    def __init__(self, database="REUCLOUD", server="myserv"):
        self.cnxn = pymssql.connect(server, 'sa', 'Password123', database)
        self.cursor = self.cnxn.cursor() 
        
        
    def _select_id_table(self, table: Tables):
        try:
            self.cursor.execute(f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE ORDINAL_POSITION = 1 and TABLE_NAME = N'{table.value}'")
            rows = self.cursor.fetchone()
            # columns = [column[0] for column in rows]
            return ''.join(rows)
        except Exception as e:
            print(e, '_select_id_table')
            return []
        
    def _select_columns(self, table: Tables):
        try:
            self.cursor.execute(f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N'{table.value}'")
            rows = self.cursor.fetchall()
            columns = [column[0] for column in rows]
            return columns
        except Exception as e:
            print(e, 'select_columns')
            return []
    
    def select_all_table(self, table: Tables):
        try:
            columns = self._select_columns(table)
            results = []
            self.cursor.execute(f'SELECT * FROM {table.value}')
            rows = self.cursor.fetchall()
            for row in rows:
                results.append(dict(zip(columns, row)))
            print(results,rows,'59')
            return results
        except Exception as e:
            print(e, 'select_all_table')
            return []
    
    
    def select_one_table(self, table: Tables, where: str):
        try:
            data = self.select_all_table(table)
            print(data,where,101)
            print(type(data),type(where),101)
            for i in data:
                for j in i:
                    if str(i[j]) in where:
                        print(i[j],where,102)
                        return i
        except Exception as e:
            print(e, 'select_one_table')
            return []
    
    
    def post(self, table: Tables, data: dict):
        try:
            _insert = f'INSERT INTO {table.value} VALUES ('
            i=int(0)
            for key, value in data.items():
                if i == len(data)-1:
                    if type(value)is str:
                        _insert += f"N'{value}')"
                    else:
                        _insert += f"{value})"
                else:
                    if type(value)is str:
                        _insert += f"N'{value}', "
                    else:
                        _insert += f"{value}, "
                i+=1
            self.cursor.execute(_insert)
            self.cnxn.commit()
            return True
        except Exception as e:
            print(e, 'post',table)
            return []
    
    
    def put(self, table: Tables, data: dict, idtable: str):
        try:
            _update = f'UPDATE {table.value} SET '
            i=int(0)
            for key, value in data.items():
                if i == len(data)-1:
                    if type(value)is str:
                        _update += f"{key} = N'{value}', "
                    else:
                        _update += f"{key} = {value}, "
                else:
                    if type(value)is str:
                        _update += f"{key} = N'{value}', "
                    else:
                        _update += f"{key} = {value}, "
                i+=1
            _update +=' WHERE '
            _update = _update.replace(',  WHERE', ' WHERE')
            id = {
                self._select_id_table(table):idtable
            }
            for key, value in id.items():
                if type(value)is str:
                    _update += f"{key} = N'{value}'"
                else:
                    _update += f"{key} = {value}"
            self.cursor.execute(_update)
            self.cnxn.commit()
            return True
        except Exception as e:
            print(e, 'put')
            return []
    
        
    def delete(self, table: Tables, idtable: str):
        try:
            _delete = f'DELETE FROM {table.value} WHERE '
            id = {
                self._select_id_table(table):idtable
            }
            for key, value in id.items():
                if type(value)is str:
                    _delete += f"{key} = N'{value}'"
                else:
                    _delete += f"{key} = {value}"
            print(_delete)
            self.cursor.execute(_delete)
            self.cnxn.commit()
            return True
        except Exception as e:
            print(e, 'delete')
            return []