import pytest
import sqlite3
from Models.movie_review import Movie
from db.db_manager import DatabaseManager

#Must delete test_flicks.db file and run tests
#in order otherwise will not work


#@pytest.fixture
def setup_database():
    #fixture to set up database with test data
    #rowID (Primary Key) auto given by SQLite
    conn = sqlite3.connect("test_flicks.db")
    cursor = conn.cursor()
    #Delete old table so not duplicating values for tests
    cursor.execute("DROP table IF EXISTS movies;")
    conn.commit()
    #Create new table for tests
    cursor.execute("CREATE TABLE IF NOT EXISTS movies ( \
                id INTEGER PRIMARY KEY, \
                name TEXT NOT NULL, \
                year INTEGER NOT NULL, \
                rating INTEGER NOT NULL, \
                genre TEXT NOT NULL, \
                review TEXT NOT NULL)")
    conn.commit()
    db = DatabaseManager("test_flicks.db")

def test_success_add():
    db = DatabaseManager("test_flicks.db")
    
    
    #test insert By object
    exa1 = Movie(1, "Lemon", 2011, 7.0, "comedy", "very good")
    db.insertByObject(exa1)
    exa2 = Movie(2, "Spiderman", 2012, 9.0, "action", "amazing")
    db.insertByObject(exa2)

    results = db.selectAll()
    assert len(results) == 2

def test_fail_add():
    #test all 5 incorrect fields - if each one returns the right error
    db = DatabaseManager("test_flicks.db")
    #test invalid id - should return Value error if not int
    with pytest.raises(ValueError):
        db.insertByObject(Movie("", "Trees", 2011, 7.0, "comedy", "very good"))
    
    #test invalid name - should return Value error if not str or if empty
    with pytest.raises(ValueError):
        db.insertByObject(Movie(6, 2, 2011, 7.0, "comedy", "very good"))

    #test invalid year - should return Value error if year is less 1890
    with pytest.raises(ValueError):
        db.insertByObject(Movie(7, "Trees", 1888, 7.0, "comedy", "very good"))

    #test invalid rating - should return Value error if not float or not between 0.0 - 10.0
    with pytest.raises(ValueError):
        #int given as rating instead of float
        db.insertByObject(Movie(8, "Trees", 2011, 7, "comedy", "very good"))
        #float given that is not within 0.0 - 10.0 range
        db.insertByObject(Movie(9, "Grass", 2011, 11.0, "comedy", "very good"))

    #test invalid genre - should return Value error if not str or if empty
    with pytest.raises(ValueError):
        db.insertByObject(Movie(10, "Trees", 2011, 7.0, True, "very good"))
        
    #test invalid review - should return Value error if not str or if empty
    with pytest.raises(ValueError):
        db.insertByObject(Movie(11, "Trees", 2011, 7.0, "drama", False))

def test_remove_movie_review():
    #Test if db manager delete movie review from database
    #starts with 4 movie review entries from previous tests
    db = DatabaseManager("test_flicks.db")
    
    #success
    db.removeByID(2)

    results = db.selectAll()
    assert len(results) == 1