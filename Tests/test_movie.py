import pytest
from Models.movie_review import Movie

@pytest.fixture
def good_review():
    return Movie(2, "Trees", 2011, 7.0, "comedy", "very good")

# @pytest.fixture
# def bad_review():
#     #id,name,year,rating,genre,length,review
#     return Movie("9", 9, 1850, 11.0, 5, -11)

def test_good_instance(good_review):
    #Test if the movie review class is saving data properly

    assert hasattr(good_review, '_id')
    assert type(good_review._id) == int
    assert good_review._id == 2
    
    assert hasattr(good_review, '_name')
    assert type(good_review._name) == str
    assert good_review._name == "Trees"

    assert hasattr(good_review, '_year')
    assert type(good_review._year) == int
    assert good_review._year == 2011

    assert hasattr(good_review, '_rating')
    assert type(good_review._rating) == float
    assert good_review._rating == 7.0

    assert hasattr(good_review, '_genre')
    assert type(good_review._genre) == str
    assert good_review._genre == "comedy"

    assert hasattr(good_review, '_review')
    assert type(good_review._review) == str
    assert good_review._review == "very good"
    
def test_bad_id():
    #Test for error when incorrect id is given
    with pytest.raises(ValueError):
        Movie("", "Trees", 2011, 7.0, "comedy", "very good")
    
def test_bad_name():
    #Test for error when incorrect name is given
    with pytest.raises(ValueError):
        Movie(2, "", 2011, 7.0, "comedy", "very good")

def test_bad_year():
    #Test for error when incorrect year is given
    with pytest.raises(ValueError):
        Movie(2, "Trees", 1850, 7.0, "comedy", "very good")

def test_bad_rating():
    #Test for error when incorrect rating is given
    with pytest.raises(ValueError):
        Movie(2, "Trees", 2011, 11.0, "comedy", "very good")
        
def test_bad_genre():
    #Test for error when incorrect genre is given
    with pytest.raises(ValueError):
        Movie(2, "Trees", 2011, 7.0, False, "very good")

def test_bad_review():
    #Test for error when incorrect review is given
    with pytest.raises(ValueError):
        Movie(2, "Trees", 2011, 7.0, "comedy", 10)
        
def test_id_property(good_review):
    """
    Tests whether id property exists
    """
    assert hasattr(good_review, '_id')
    assert type(good_review.__class__.id) == property
    assert good_review._id == 2
    #tests the setter
    good_review.id = 3
    assert good_review._id == 3
    
def test_name_property(good_review):
    #Tests whether name property exists
    assert hasattr(good_review, '_name')
    assert type(good_review.__class__.name) == property
    assert good_review._name == "Trees"
    good_review.name = "Spiderman"
    assert good_review._name == "Spiderman"

    
def test_year_property(good_review):
    #Tests whether year property exists
    assert hasattr(good_review, '_year')
    assert type(good_review.__class__.year) == property
    assert good_review._year == 2011
    good_review.year = 2015
    assert good_review._year == 2015

def test_rating_property(good_review):
    #Tests whether rate property exists
    assert hasattr(good_review, '_rating')
    assert type(good_review.__class__.rating) == property
    assert good_review._rating == 7.0
    good_review.rating = 8.6
    assert good_review._rating == 8.6

def test_genre_property(good_review):
    #Tests whether genre property exists
    assert hasattr(good_review, '_genre')
    assert type(good_review.__class__.genre) == property
    assert good_review._genre == "comedy"
    good_review.genre = "action"
    assert good_review._genre == "action"

def test_review(good_review):
    #Tests whether review property exists
    assert hasattr(good_review, '_review')
    assert type(good_review.__class__.review) == property
    assert good_review._review == "very good"
    good_review.review = "amazing movie"
    assert good_review._review == "amazing movie"

def test_movie_str(good_review):
    #Test if displaying all the information is good
    assert str(good_review) == "Id: 2; Name: Trees; Year: 2011; Rating: 7.0; Genre: comedy; Review: very good;"