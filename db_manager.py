import sqlite3

class DatabaseManager:
    def __init__(self, filename):        
        self._db = sqlite3.connect(filename)
        self._cursor = self._db.cursor()
        
        #check if table exist
        self._cursor.execute('SELECT name from sqlite_master where type="table"')
        res = self._cursor.fetchone()
        
        if not res or "movies" not in res:
            #if movies table does not exist, it will be created with 3 columns "name", "year" and "rating"
            self._cursor.execute("CREATE TABLE movies (name TEXT NOT NULL, year INTEGER NOT NULL, rating INTEGER NOT NULL, genre TEXT NOT NULL, description TEXT NOT NULL, summary TEXT NOT NULL, length INTEGER NOT NULL, maturity TEXT NOT NULL)")
            self._db.commit()
            
            
    def add(self, name_, year_, rating_, genre_, description_, summary_, length_, maturity_):
        "add a new movie to db"
        fields = [name_, year_, rating_, genre_, description_, summary_, length_, maturity_]
        self._cursor.execute("INSERT INTO movies ('name', 'year', 'rating', 'genre', 'description', 'summary', 'length', 'maturity') VALUES (?,?,?,?,?,?,?,?);", fields)
        self._db.commit()


    def select_all(self):
        #return list of JSON serialized score objects sorted in descending order
        self._cursor.execute("SELECT * FROM movies")
        return self._cursor.fetchall()
    
    
    def remove_by_name(self, name_):
        #delete all entries in DB that match specified name
        fields = [name_]
        self._cursor.execute("DELETE FROM movies WHERE name=?;", fields)
        self._db.commit() 
        
    
    def close(self):
        self._db.close()