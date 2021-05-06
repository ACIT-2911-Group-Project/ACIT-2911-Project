class Movie:
    """ Simple class to represent a movie """

    def __init__(self, id_, name_, year_, rating_, genre_, review_):
        """ Initializes private attributes

        Args:
            id (int): id of the specific movie (cannot be empty)
            name (string): namne of the movie
            year (int): release year of movie (must be 4 digit int)
            rating (float): rating of movie out of 10 (must be a float value between 0 and 10)
            genre (string): the genre of the movie
            review (string): short sentence review of movie

        """
        self.id = id_   
        self.name = name_
        self.year = year_
        self.rating = rating_
        self.genre = genre_
        self.review = review_
        
    def __str__(self):
        #Return a string with the id, name, year of release, rating, genre, review, and length of the movie
        return f"Id: {self.id}; Name: {self.name}; Year: {self.year}; Rating: {self.rating}; Genre: {self.genre}; Review: {self.review};"
        
    def __gt__(self, other):
        #Return Boolean whether self rating greater than opponent
        if type(other) is not type(self):
            raise TypeError("Unsupported type")
                
        return self.rating > other.rating
    
    @property
    def id(self):
        #getter for movie id
        return self._id
    
    @id.setter
    def id(self, value):
        #setter for movie id
        if type(value) is not int:
            raise ValueError("Invalid movie Id.")
        else:
            self._id = value    
        
    @property
    def name(self):
        #getter for movie name
        return self._name
    
    @name.setter
    def name(self, value):
        #setter for movie name
        if type(value) is not str or not value:
            raise ValueError("Invalid movie name.")
        else:
            self._name = value
        
    @property
    def year(self):
        #getter for movie release year
        return self._year
    
    @year.setter
    def year(self, value):
        #setter for movie release year
        if type(value) is not int or value < 1890:
            raise ValueError("Invalid movie release year.")
        else:
            self._year = value

    @property
    def rating(self):
        #getter for movie rating
        return self._rating
                
    @rating.setter
    def rating(self, value):
        #setter for movie rating
        if type(value) is not float or value < 0.0 or value > 10.0:
            raise ValueError("Invalid movie rating.") 
        else:
            self._rating = value

    @property
    def genre(self):
        #getter for movie genre 
        return self._genre
    
    @genre.setter
    def genre(self, value):
        #setter for movie genre 
        if type(value) is not str or not value:
            raise ValueError("Invalid movie genre.")
        else:
            self._genre = value

    @property
    def review(self):
        #getter for movie review 
        return self._review
    
    @review.setter
    def review(self, value):
        #setter for movie review 
        if type(value) is not str or not value:
            raise ValueError("Invalid movie review.")
        else:
            self._review = value
            
    @property
    def length(self):
        # getter for movie length in minutes 
        return self._length
                
    @length.setter
    def length(self, value):
        # setter for movie length in minutes 
        if type(value) is not int or value < 0:
            raise ValueError("Invalid movie length.") 
        else:
            self._length = value

    
