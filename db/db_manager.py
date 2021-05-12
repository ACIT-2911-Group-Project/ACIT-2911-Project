import sqlite3

class DatabaseManager:
    def __init__(self, filename):        
        self._db = sqlite3.connect(filename)
        self._cursor = self._db.cursor()
        
        #Check if table exists
        self._cursor.execute('SELECT name from sqlite_master where type="table"')
        res = self._cursor.fetchone()
        
        if not res or "movies" not in res:
            #If movies table does not exist, it will be created
            self._cursor.execute("CREATE TABLE IF NOT EXISTS movies ( \
                id INTEGER PRIMARY KEY, \
                name TEXT NOT NULL, \
                year INTEGER NOT NULL, \
                rating INTEGER NOT NULL, \
                genre TEXT NOT NULL, \
                review TEXT NOT NULL)")
            self._db.commit()
            
            
    def insertByFields(self, name_, year_, rating_, genre_, review_):
        "add a new movie to db"
        fields = [name_, year_, rating_, genre_, review_]
        self._cursor.execute("INSERT INTO movies ('name', 'year', 'rating', 'genre', 'review') VALUES (?,?,?,?,?);", fields)
        self._db.commit()

    def insertByObject(self, movie_):
        "add a new movie to db"
        fields = [movie_.name, movie_.year, movie_.rating, movie_.genre, movie_.review]
        self._cursor.execute("INSERT INTO movies ('name', 'year', 'rating', 'genre', 'review') VALUES (?,?,?,?,?);", fields)
        self._db.commit()

    def selectAll(self):
        #Return a list of all movies
        self._cursor.execute("SELECT * FROM movies")
        return self._cursor.fetchall()
    
    def selectByName(self, name_):
        #Return a list of movies that match a given name
        field = [name_]
        self._cursor.execute("SELECT * FROM movies WHERE name like ?;", ('%'+name_+'%',))
        return self._cursor.fetchall()    
    
    def selectByYear(self, year_):
        #Return a list of movies that match a given year
        field = [year_]
        self._cursor.execute("SELECT * FROM movies WHERE year=?;", field)
        return self._cursor.fetchall()
    
    def selectByRating(self, rating_):
        #Return a list of movies that are above certain rating
        field = [rating_]
        self._cursor.execute("SELECT * FROM movies WHERE rating>?;", field)
        return self._cursor.fetchall()    
        
    def removeByID(self, id_):
        #Delete all entries in DB that match specified id
        field = [id_]
        self._cursor.execute("DELETE FROM movies WHERE id=?;", field)
        self._db.commit()
        
    def close(self):
        self._db.close()