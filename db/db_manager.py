import sqlite3

class DatabaseManager:
    def __init__(self, filename):        
        self._db = sqlite3.connect(filename)
        self._cursor = self._db.cursor()
        
        #check if table exist
        self._cursor.execute('SELECT name from sqlite_master where type="table"')
        res = self._cursor.fetchone()
        
        if not res or "movies" not in res:
            # if movies table does not exist, it will be created
            self._cursor.execute("CREATE TABLE IF NOT EXISTS movies ( \
                id INTEGER PRIMARY KEY, \
                name TEXT NOT NULL, \
                year INTEGER NOT NULL, \
                rating INTEGER NOT NULL, \
                genre TEXT NOT NULL, \
                review TEXT NOT NULL, \
                length INTEGER NOT NULL, \
                maturity TEXT NOT NULL)")
            self._db.commit()
            
            
    def add(self, name_, year_, rating_, genre_, review_, length_, maturity_):
        "add a new movie to db"
        fields = [name_, year_, rating_, genre_, review_, length_, maturity_]
        self._cursor.execute("INSERT INTO movies ('name', 'year', 'rating', 'genre', 'review', 'length', 'maturity') VALUES (?,?,?,?,?,?,?);", fields)
        self._db.commit()


    def selectAll(self):
        ''' return a list of all movies '''
        self._cursor.execute("SELECT * FROM movies")
        return self._cursor.fetchall()
    
    def selectByName(self, name_):
        ''' return a list of movies that match a given name '''
        field = [name_]
        self._cursor.execute("SELECT * FROM movies WHERE name like ?;", ('%'+name_+'%',))
        return self._cursor.fetchall()    
    
    def selectByYear(self, year_):
        ''' return a list of movies that math a given year '''
        field = [year_]
        self._cursor.execute("SELECT * FROM movies WHERE year=?;", field)
        return self._cursor.fetchall()  
        
    def removeByName(self, name_):
        ''' delete all entries in DB that match specified name '''
        field = [name_]
        self._cursor.execute("DELETE FROM movies WHERE name=?;", field)
        self._db.commit() 
        
    
    def close(self):
        self._db.close()
      