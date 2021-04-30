from movie_review import Movie


class MovieManager:
    """ Simple class to represent a Movie manager"""
    def __init__(self):
        """ Initializes dictionary of scores

        Args:
            none
        
        Raises:
            none
        """
        self._movies = {}

    @property
    def scores(self):
        "Return a list of scores"
        return list(self._movies.values())
    
    def add_movie(self, movie_obj):
        "add a new score to scores dictionary with name of score as key "
        self._movies[movie_obj.name] = movie_obj
        
    def delete_movie(self, movie_name):
        "remove a score from scores dictionary"
        self._movies.pop(movie_name)

    def __len__(self):
        "return number of items in movies dictionary "
        return len(self._movies)
    
    def get_movies(self):
        "return a list of dictionary representations of all scores"
        scores_list = []
        sorted_list = sorted(self.scores, reverse=True)
        for score in sorted_list:
            scores_list.append(score.to_dict())
        return scores_list
            
    