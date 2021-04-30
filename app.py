from db_manager import DatabaseManager
from Models.movie_review import Movie


def main():
  db = DatabaseManager("flicks.db")
  
  db.add("Batman", 2008, 9.5, "Thriller", "The dark knight saves Gotham", "Heath Ledger won an Oscar for his great performance. Must watch", 120, "R")

  db.add("Spiderman", 1998, 8, "Action", "Red spider guy", "save bitches from danger", 100, "PG13")
  
  db.close()
  
main()