class Review:
    def __init__(self, viewer, movie, rating):
        if not isinstance(rating, int) or rating < 1 or rating > 5:
            raise ValueError("Rating must be an integer between 1 and 5.")
        if not isinstance(viewer, Viewer):
            raise ValueError("Viewer must be an instance of the Viewer class.")
        if not isinstance(movie, Movie):
            raise ValueError("Movie must be an instance of the Movie class.")
        self._viewer = viewer
        self._movie = movie
        self._rating = rating

    @property
    def rating(self):
        return self._rating

    @property
    def viewer(self):
        return self._viewer

    @property
    def movie(self):
        return self._movie

