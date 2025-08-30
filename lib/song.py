class Song:
    pass
    count = 0
    artists = []
    genres = []
    artist_count = {}
    genre_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # Increment song count
        self.add_song_to_count()

        # Add artist and genre
        self.add_to_artists()
        self.add_to_genres()

        # Update histograms
        self.add_to_artist_count()
        self.add_to_genre_count()

    # Class methods
    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_artists(cls):
        if cls._current_artist_not_in_list():
            cls.artists.append(cls._current_artist())

    @classmethod
    def add_to_genres(cls):
        if cls._current_genre_not_in_list():
            cls.genres.append(cls._current_genre())

    @classmethod
    def add_to_artist_count(cls):
        artist = cls._current_artist()
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1

    @classmethod
    def add_to_genre_count(cls):
        genre = cls._current_genre()
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    # Helper methods to access the last initialized instance's artist and genre
    @classmethod
    def _current_artist(cls):
        return cls._last_instance.artist

    @classmethod
    def _current_genre(cls):
        return cls._last_instance.genre

    @classmethod
    def _current_artist_not_in_list(cls):
        return cls._current_artist() not in cls.artists

    @classmethod
    def _current_genre_not_in_list(cls):
        return cls._current_genre() not in cls.genres

    # Keep track of the last initialized instance
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        cls._last_instance = instance
        return instance

    pass