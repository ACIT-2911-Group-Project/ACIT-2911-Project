import pytest
import sqlite3
from db.db_manager import DatabaseManager


# @pytest.fixture
def setup_database():
    #fixture to set up database with test data
    #rowID (Primary Key) auto given by SQLite
    conn = sqlite3.connect("test_flicks.db")
    cursor = conn.cursor()
    #delete old table so not duplicating values for tests
    cursor.execute("DROP table IF EXISTS movies;")
    conn.commit()
    #create new table for tests
    cursor.execute("CREATE TABLE IF NOT EXISTS movies ( \
                id INTEGER PRIMARY KEY, \
                name TEXT NOT NULL, \
                year INTEGER NOT NULL, \
                rating INTEGER NOT NULL, \
                genre TEXT NOT NULL, \
                review TEXT NOT NULL")
    conn.commit()
    db = DatabaseManager("test_flicks.db")

def test_add():
    #test if db manager add function working
    db = DatabaseManager("test_flicks.db")
    
    db.add("Trees", 1999, 9.3, "Comedy", "Great")
    db.add("Grass", 2010, 7.5, "Drama", "Average")
    
    results = db.selectAll()
    assert len(results) == 2

def test_removeByName():
    #test if db manager delete movie review from database
    db = DatabaseManager("test_flicks.db")
    
    db.add("Trees", 1999, 9.0, "Comedy", "Great")
    db.add("Grass", 2010, 7.5, "Drama", "Average")
    db.add("Lindt", 2009, 9.5, "Thriller", "Amazing")
    db.add("Chez", 1999, 5.0, "Horror", "Bad")
    db.add("BitC", 2013, 8.5, "Drama", "Good")
    db.add("Straw", 2006, 7.5, "Documentary", "Average")
    
    
    results2 = db.selectAll()
    assert len(results) == 6


# def test_connection():
#     # Test to make sure that there are 2 items in the database

#     # cursor = setup_database
#     conn = sqlite3.connect("test_flicks.db")
#     cursor = conn.cursor()
#     assert len(list(cursor.execute('SELECT * FROM stocks'))) == 2

# def main():
#     test_add()

# main()
    