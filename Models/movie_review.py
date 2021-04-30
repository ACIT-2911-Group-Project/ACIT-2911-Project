class Movie:
    """ Simple class to represent a movie """

    def __init__(self, name_, year_, rating_, genre_, description_, summary_, length_, maturity_):
        """ Initializes private attributes

        Args:
            name (str): name of the player (cannot be empty)
            score (int): score of the player (cannot be negative)
        
        Raises:
            ValueError: name is empty or not string, score is not integer or negative
        """   
        self._name = name_
        self._year = year_
        self._rating = rating_
        self._genre = genre_
        self._description = description_
        self._summary = summary_
        self._length = length_
        self._maturity = maturity_
        
    def __str__(self):
        "Return a string with the name and score of specified user"
        return f"Movie Review: {self.name} ({self.year}) {self.rating} ({self.genre}) {self.description} ({self.summary}) {self.length} ({self.maturity})  "
        
    def __gt__(self, other):
        "Return a boolean indicating if user score greater than opponent score"
        if type(other) is not type(self):
            raise TypeError("Unsupported type")
                
        return self.rating > other.rating

        
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
    def description(self):
        return self._description
    
    @description.setter
    def description(self, value):
        if type(value) is not str or not value:
            raise ValueError("Invalid movie description.")
        else:
            self._description = value

    @property
    def summary(self):
        return self._summary
    
    @summary.setter
    def summary(self, value):
        if type(value) is not str or not value:
            raise ValueError("Invalid movie summary.")
        else:
            self._summary= value
    
    @property
    def length(self):
        return self._length
                
    @length.setter
    def length(self, value):
        if type(value) is not int or value < 0:
            raise ValueError("Invalid movie length.") 
        else:
            self._length = value
    
    @property
    def maturity(self):
        return self._maturity
                
    @maturity.setter
    def maturity(self, value):
        if type(value) is not str or not value:
            raise ValueError("Invalid movie maturity.") 
        else:
            self._maturity = value