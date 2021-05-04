import pytest
from models.movie_review import Movie

def test_instance():
    #Test if the movie review class is saving data properly
    the_movie_review = Movie("Trees", 2011, 7.0, "comedy", "look at nature", "very good", 105, "PG")
    
    assert hasattr(the_movie_review, '_name')
    assert type(the_movie_review._name) == str
    assert the_movie_review._name == "Trees"
    
    assert hasattr(the_movie_review, '_year')
    assert type(the_movie_review._year) == int
    assert the_movie_review._year == 2011

    assert hasattr(the_movie_review, '_rating')
    assert type(the_movie_review._rating) == float
    assert the_movie_review._rating == 7.0

    assert hasattr(the_movie_review, '_genre')
    assert type(the_movie_review._genre) == str
    assert the_movie_review._genre == "comedy"

    assert hasattr(the_movie_review, '_description')
    assert type(the_movie_review._description) == str
    assert the_movie_review._description == "look at nature"
    
    assert hasattr(the_movie_review, '_summary')
    assert type(the_movie_review._summary) == str
    assert the_movie_review._summary == "very good"

    assert hasattr(the_movie_review, '_length')
    assert type(the_movie_review._length) == int
    assert the_movie_review._length == 105
    
    assert hasattr(the_movie_review, '_maturity')
    assert type(the_movie_review._maturity) == str
    assert the_movie_review._maturity == "PG"
    
def test_name_property():
    """
    Tests whether name property exists
    """
    the_movie_review = Movie("Trees", 2011, 7.0, "comedy", "look at nature", "very good", 105, "PG")
    
    assert hasattr(the_movie_review, '_name')
    assert type(the_movie_review.__class__.name) == property
    assert the_movie_review._name == "Trees"
    the_movie_review.name = "Spiderman"
    assert the_movie_review._name == "Spiderman"

    
def test_year_property():
    """
    Tests whether year property exists
    """
    the_movie_review = Movie("Trees", 2011, 7.0, "comedy", "look at nature", "very good", 105, "PG")
    
    assert hasattr(the_movie_review, '_year')
    assert type(the_movie_review.__class__.year) == property
    assert the_movie_review._year == 2011
    the_movie_review.year = 2015
    assert the_movie_review._year == 2015

def test_rating_property():
    """
    Tests whether rate property exists
    """
    the_movie_review = Movie("Trees", 2011, 7.0, "comedy", "look at nature", "very good", 105, "PG")
    
    assert hasattr(the_movie_review, '_rating')
    assert type(the_movie_review.__class__.rating) == property
    assert the_movie_review._rating == 7.0
    the_movie_review.rating = 8.6
    assert the_movie_review._rating == 8.6

def test_genre_property():
    """
    Tests whether genre property exists
    """
    the_movie_review = Movie("Trees", 2009, 7.0, "comedy", "look at nature", "very good", 105, "PG")
    
    assert hasattr(the_movie_review, '_genre')
    assert type(the_movie_review.__class__.genre) == property
    assert the_movie_review._genre == "comedy"
    the_movie_review.genre = "action"
    assert the_movie_review._genre == "action"

def test_description_property():
    """
    Tests whether description property exists
    """
    the_movie_review = Movie("Trees", 2011, 7.0, "comedy", "look at nature", "very good", 105, "PG")
    
    assert hasattr(the_movie_review, '_description')
    assert type(the_movie_review.__class__.description) == property
    assert the_movie_review._description == "look at nature"
    the_movie_review.description = "amazing movie"
    assert the_movie_review._description == "amazing movie"

def test_summary_property():
    """
    Tests whether summary property exists
    """
    the_movie_review = Movie("Trees", 2011, 7.0, "comedy", "look at nature", "very good", 105, "PG")
    
    assert hasattr(the_movie_review, '_summary')
    assert type(the_movie_review.__class__.summary) == property
    assert the_movie_review._summary == "very good"
    the_movie_review.summary = "all about the trees"
    assert the_movie_review._summary == "all about the trees"

def test_length_property():
    """
    Tests whether length property exists
    """
    the_movie_review = Movie("Trees", 2011, 7.0, "comedy", "look at nature", "very good", 105, "PG")
    
    assert hasattr(the_movie_review, '_length')
    assert type(the_movie_review.__class__.length) == property
    assert the_movie_review._length == 105
    the_movie_review.length = 120
    assert the_movie_review._length == 120

def test_maturity_property():
    """
    Tests whether maturity property exists
    """
    the_movie_review = Movie("Trees", 2011, 7.0, "comedy", "look at nature", "very good", 105, "PG")
    
    assert hasattr(the_movie_review, '_maturity')
    assert type(the_movie_review.__class__.maturity) == property
    assert the_movie_review._maturity == "PG"
    the_movie_review.maturity = "R"
    assert the_movie_review._maturity == "R"

def test_movie_str():
    the_movie_review = Movie("Trees", 2011, 7.0, "comedy", "look at nature", "very good", 105, "PG")
    assert str(the_movie_review) == "Name: Trees; Year: 2011; Rating: 7.0; Genre: comedy; Description: look at nature; Summary: very good; Length: 105; Maturity: PG"
