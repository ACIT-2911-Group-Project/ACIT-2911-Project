import pytest
import sqlite3
from Models.movie_review import Movie
from db.db_manager import DatabaseManager



@pytest.fixture
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

def test_success_add(setup_database):
    db = DatabaseManager("test_flicks.db")
    
    
    #test insert By object
    exa1 = Movie(1, "Lemon", 2011, 7.0, "comedy", "very good")
    db.insertByObject(exa1)
    exa2 = Movie(2, "Spiderman", 2012, 9.0, "action", "amazing")
    db.insertByObject(exa2)

    results = db.selectAll()
    assert len(results) == 2

def test_fail_add(setup_database):
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

def test_remove_movie_review(setup_database):
    #Test if db manager delete movie review from database
    db = DatabaseManager("test_flicks.db")
    exa1 = Movie(1, "Lemon", 2011, 7.0, "comedy", "very good")
    db.insertByObject(exa1)
    exa2 = Movie(2, "Spiderman", 2012, 9.0, "action", "amazing")
    db.insertByObject(exa2)
    
    #success
    db.removeByID(2)

    results = db.selectAll()
    assert len(results) == 1
    

def test_update_movie_review(setup_database):
    #Test if db manager update movie review from database
    db = DatabaseManager("test_flicks.db")
    exa1 = Movie(1, "Lemon", 2011, 7.0, "comedy", "very good")
    db.insertByObject(exa1)

    #change name of exa1
    exa1.name = "Apple"

    db.updateByObject(exa1)

    result = db.selectAll()

    assert exa1.name == result[0][1]

    #change year of exa1
    exa1.year = 2015

    db.updateByObject(exa1)
    
    result = db.selectAll()
    
    assert exa1.year == result[0][2]
    
    #change rating of exa1
    exa1.rating = 9.0

    db.updateByObject(exa1)
    
    result = db.selectAll()
    
    assert exa1.rating == result[0][3]

    #change genre of exa1
    exa1.genre = "action"

    db.updateByObject(exa1)
    
    result = db.selectAll()
    
    assert exa1.genre == result[0][4]
    
    #change year of exa1
    exa1.review = "Exceptional"

    db.updateByObject(exa1)
    
    result = db.selectAll()
    
    assert exa1.review == result[0][5]