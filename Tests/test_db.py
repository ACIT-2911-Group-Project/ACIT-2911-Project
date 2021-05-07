import pytest
import sqlite3
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

def test_add():
    #Test if db manager add function working
    db = DatabaseManager("test_flicks.db")
    
    db.add("Trees", 1999, 9.3, "Comedy", "Great")
    db.add("Grass", 2010, 7.5, "Drama", "Average")
    
    results = db.selectAll()
    assert len(results) == 2

# def test_selectByName():
#     #Test if db manager is selecting movie review by name
#     db = DatabaseManager("test_flicks.db")
    
#     result = db.selectByName("Trees")

#     assert result.name == "Trees"

def test_removeByName():
    #Test if db manager delete movie review from database
    db = DatabaseManager("test_flicks.db")
    
    db.removeByName("Trees")

    results = db.selectAll()
    assert len(results) == 1