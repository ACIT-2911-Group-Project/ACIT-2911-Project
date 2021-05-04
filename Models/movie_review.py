class Movie:
    """ Simple class to represent a movie """

    def __init__(self, id_, name_, year_, rating_, genre_, length_, review_):
        """ Initializes private attributes

        Args:
            name (str): name of the player (cannot be empty)
            score (int): score of the player (cannot be negative)
        
        Raises:
            ValueError: name is empty or not string, score is not integer or negative
        """
        self.id = id_   
        self.name = name_
        self.year = year_
        self.rating = rating_
        self.genre = genre_
        self.length = length_
        self.review = review_
        
    def __str__(self):
        "Return a string with the name and score of specified user"
        return f"Id: {self.id}; Name: {self.name}; Year: {self.year}; Rating: {self.rating}; Genre: {self.genre}; Review: {self.review}; Length: {self.length}"
        
    def __gt__(self, other):
        "Return a boolean indicating if user score greater than opponent score"
        if type(other) is not type(self):
            raise TypeError("Unsupported type")
                
        return self.rating > other.rating
    
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, value):
        if type(value) is not int:
            raise ValueError("Invalid movie Id.")
        else:
            self._id = value    
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if type(value) is not str or not value:
            raise ValueError("Invalid movie name.")
        else:
            self._name = value
        
    @property
    def year(self):
        return self._year
    
    @year.setter
    def year(self, value):
        if type(value) is not int or value < 1890:
            raise ValueError("Invalid movie release year.")
        else:
            self._year = value

    @property
    def rating(self):
        return self._rating
                
    @rating.setter
    def rating(self, value):
        if type(value) is not float or value < 0.0 or value > 10.0:
            raise ValueError("Invalid movie rating.") 
        else:
            self._rating = value

    @property
    def genre(self):
        return self._genre
    
    @genre.setter
    def genre(self, value):
        if type(value) is not str or not value:
            raise ValueError("Invalid movie genre.")
        else:
            self._genre = value

    @property
    def review(self):
        return self._review
    
    @review.setter
    def review(self, value):
        if type(value) is not str or not value:
            raise ValueError("Invalid movie review.")
        else:
            self._review = value
    
    @property
    def length(self):
        return self._length
                
    @length.setter
    def length(self, value):
        if type(value) is not int or value < 0:
            raise ValueError("Invalid movie length.") 
        else:
            self._length = value
    
    # @property
    # def maturity(self):
    #     return self._maturity
                
    # @maturity.setter
    # def maturity(self, value):
    #     if type(value) is not str or not value:
    #         raise ValueError("Invalid movie maturity.") 
    #     else:
    #         self._maturity = value