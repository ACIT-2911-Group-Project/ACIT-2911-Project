from db.db_manager import DatabaseManager

class DataAccessHelper():
    
  def queryByMovieName(self, name):
    #Search movie review by name
    db = DatabaseManager("flicks.db")
    movie_reviews = db.selectByName(name)
    db.close()
    return movie_reviews
  
  def queryByMovieYear(self, year):
    #Search movie review by year
    db = DatabaseManager("flicks.db")
    movie_reviews = db.selectByYear(year)
    db.close()
    return movie_reviews
  
  def queryByMovieRating(self, rating):
    #Search movie by rating
    db = DatabaseManager("flicks.db")
    movie_reviews = db.selectByRating(rating)
    db.close()
    return movie_reviews
  
  def queryAll(self):  
    #Return all movies in database  
    db = DatabaseManager("flicks.db")
    movie_reviews = db.selectAll()
    db.close()
    return movie_reviews
  
  def insertMovieReview(self, movie_review):
    #Add movie review to database
    db = DatabaseManager("flicks.db")
    db.insertByObject(movie_review)
    db.close() 
    
  def removeMovieReview(self, movie_review_id):
    #Delete movie review from database
    db = DatabaseManager("flicks.db")
    db.removeByID(movie_review_id)
    db.close()
    
  def updateMovieReview(self, movie_review):
    #Update a specific moview review from database
    db = DatabaseManager("flicks.db")
    db.updateByObject(movie_review)
    db.close()
    