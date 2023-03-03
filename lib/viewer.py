class Viewer:
    def __init__(self, username):
        self._username = username
        self.reviews = []
        self.reviewed_movies = []

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, new_username):
        if isinstance(new_username, str) and 6 <= len(new_username) <= 16:
            self._username = new_username
        else:
            raise ValueError("Username must be a unique string between 6 and 16 characters, inclusive.")

    def add_review(self, review):
        existing_review = next((r for r in self.reviews if r.movie == review.movie), None)
        if existing_review:
            existing_review._rating = review.rating
        else:
            self.reviews.append(review)
            self.reviewed_movies.append(review.movie)

    def reviewed_movie(self, movie):
        return movie in self.reviewed_movies

    def rate_movie(self, movie, rating):
        review = Review(self, movie, rating)
        self.add_review(review)

