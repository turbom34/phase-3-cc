class Movie:
    def __init__(self, title):
        self._title = title
        self.reviews = []
        self.reviewers = []
        
    def set_title(self, title):
        if isinstance(title, str) and len(title) > 0:
            self._title = title
        else:
            raise ValueError("Title must be a string greater than 0 characters.")
    
    def title(self):
        return self._title
    
    def add_review(self, review):
        if isinstance(review, Review):
            self.reviews.append(review)
            self.reviewers.append(review.viewer)
        else:
            raise ValueError("Review must be a Review instance.")
    
    def average_rating(self):
        total_ratings = 0
        for review in self.reviews:
            total_ratings += review.rating
        if len(self.reviews) > 0:
            return total_ratings / len(self.reviews)
        else:
            return False
    
    @classmethod
    def highest_rated(cls, movies):
        highest_rated_movie = None
        highest_rating = 0
        for movie in movies:
            avg_rating = movie.average_rating()
            if avg_rating and avg_rating > highest_rating:
                highest_rating = avg_rating
                highest_rated_movie = movie
        return highest_rated_movie


