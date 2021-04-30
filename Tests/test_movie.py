import pytest
from Models.movie_review import Movie

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
    assert type(the_movie_review.__class__._name) == property
    assert the_movie_review._name == "Trees"
    the_movie_review.name = "Spiderman"
    assert the_movie_review._name == "Spiderman"

    
def test_year_property():
    """
    Tests whether year property exists
    """
    the_movie_review = Movie("Trees", 2011, 7.0, "comedy", "look at nature", "very good", 105, "PG")
    
    assert hasattr(the_movie_review, '_year')
    assert type(the_movie_review.__class__._year) == property
    assert the_movie_review._year == 2011
    the_movie_review.year = 2015
    assert the_movie_review._year == 2015

def test_rating_property():
    """
    Tests whether rate property exists
    """
    the_movie_review = Movie("Trees", 2011, 7.0, "comedy", "look at nature", "very good", 105, "PG")
    
    assert hasattr(the_movie_review, '_rating')
    assert type(the_movie_review.__class__._rating) == property
    assert the_movie_review._rating == 7.0
    the_movie_review.rating = 8.6
    assert the_movie_review._rating == 8.6

def test_genre_property():
    """
    Tests whether genre property exists
    """
    the_movie_review = Movie("Trees", 2011, 7.0, "comedy", "look at nature", "very good", 105, "PG")
    
    assert hasattr(the_movie_review, '_genre')
    assert type(the_movie_review.__class__._genre) == property
    assert the_movie_review._genre == "comedy"
    the_movie_review.genre = "action"
    assert the_movie_review._genre == "action"

def test_description_property():
    """
    Tests whether description property exists
    """
    the_movie_review = Movie("Trees", 2011, 7.0, "comedy", "look at nature", "very good", 105, "PG")
    
    assert hasattr(the_movie_review, '_description')
    assert type(the_movie_review.__class__._description) == property
    assert the_movie_review._description == "look at nature"
    the_movie_review.description = "amazing movie"
    assert the_movie_review._description == "amazing movie"

def test_summary_property():
    """
    Tests whether summary property exists
    """
    the_movie_review = Movie("Trees", 2011, 7.0, "comedy", "look at nature", "very good", 105, "PG")
    
    assert hasattr(the_movie_review, '_summary')
    assert type(the_movie_review.__class__._summary) == property
    assert the_movie_review._summary == "very good"
    the_movie_review.summary = "all about the trees"
    assert the_movie_review._summary == "all about the trees"

def test_length_property():
    """
    Tests whether length property exists
    """
    the_movie_review = Movie("Trees", 2011, 7.0, "comedy", "look at nature", "very good", 105, "PG")
    
    assert hasattr(the_movie_review, '_length')
    assert type(the_movie_review.__class__._length) == property
    assert the_movie_review._length == 105
    the_movie_review.length = 120
    assert the_movie_review._length == 120

def test_maturity_property():
    """
    Tests whether maturity property exists
    """
    the_movie_review = Movie("Trees", 2011, 7.0, "comedy", "look at nature", "very good", 105, "PG")
    
    assert hasattr(the_movie_review, '_maturity')
    assert type(the_movie_review.__class__._maturity) == property
    assert the_movie_review._maturity == "PG"
    the_movie_review.maturity = "R"
    assert the_movie_review._rating == "R"

def test_to_dict():
    """
    Tests whether method to_dict exists
    """
    the_score = Score()

    assert hasattr(the_score, 'to_dict')
    assert the_score.to_dict() == {"name": "", "score": 0, "date": "test-date"}

def test_from_dict():
    """
    Tests whether or not the data is received correctly from the dictionary 
    """
    the_score = Score()

    assert hasattr(the_score, 'from_dict')
    the_score.from_dict({"name": "John", "score": 100, "date": 'test-date2'})
    
    assert the_score.player_name == "John"
    assert the_score.score == 100
    assert the_score.date == "test-date2"
