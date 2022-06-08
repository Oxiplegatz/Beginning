from dataclasses import dataclass


@dataclass
class Movie:
    """Class that describes a movie."""

    genre: list
    director: str
    writers: list
    cast: list
    duration: int
    release_year: int
    imdb_rating: float

    def get_description(self) -> str:
        pass
