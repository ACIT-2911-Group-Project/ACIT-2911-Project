from db.db_manager import DatabaseManager

class DataAccessHelper():
    
  def queryByMovieName(self, name):
    #search movie review by name
    db = DatabaseManager("flicks.db")
    movie_reviews = db.selectByName(name)
    db.close()
    return movie_reviews
  
  def queryByMovieYear(self, year):
    #search movie review by year
    db = DatabaseManager("flicks.db")
    movie_reviews = db.selectByYear(year)
    db.close()
    return movie_reviews
  
  def queryByMovieRating(self, rating):
    #search movie by rating
    db = DatabaseManager("flicks.db")
    movie_reviews = db.selectByRating(rating)
    db.close()
    return movie_reviews
  
  def queryAll(self):  
    #return all movies in database  
    db = DatabaseManager("flicks.db")
    movie_reviews = db.selectAll()
    db.close()
    return movie_reviews
  
  def insertMovieReview(self, movie_review):
    #add movie review to database
    db = DatabaseManager("flicks.db")
    db.insertByObject(movie_review)
    db.close() 
    
  def removeMovieReview(self, movie_review_id):
    #delete movie review from database
    db = DatabaseManager("flicks.db")
    db.removeByID(movie_review_id)
    db.close()
    
  def updateMovieReview(self, movie_review):
    #update a specific moview review from database
    db = DatabaseManager("flicks.db")
    db.updateByObject(movie_review)
    db.close()
    