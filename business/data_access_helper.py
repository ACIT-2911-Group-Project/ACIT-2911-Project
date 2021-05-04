from db.db_manager import DatabaseManager

class DataAccessHelper():
    
  def queryByMovieName(self, name):
    db = DatabaseManager("flicks.db")
    movie_reviews = db.selectByName(name)
    db.close()
    return movie_reviews
  
  def queryByMovieYear(self, year):
    db = DatabaseManager("flicks.db")
    movie_reviews = db.selectByYear(year)
    db.close()
    return movie_reviews
  
  def queryAll(self):    
    db = DatabaseManager("flicks.db")
    movie_reviews = db.selectAll()
    db.close()
    return movie_reviews