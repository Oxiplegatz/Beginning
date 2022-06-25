from dataclasses import dataclass
from typing import ClassVar


@dataclass
class Movie:
    """Class that describes a movie."""

    title: str
    genre: tuple
    director: tuple
    writer: tuple
    cast: tuple
    synopsis: str
    duration: int
    release_year: int
    imdb_rating: float

    DESCRIPTION: ClassVar[str] = (
        '{synopsis}\n\nThe movie is directed by {director} and written by '
        '{writer}. Cast includes: {cast}. Its genre is described as {genre}. '
        'The movie is {duration} minutes long. It was released in {release_year} '
        'and has an IMDB rating of {imdb_rating}.'
    )

    def get_description(self) -> str:
        movie_description = (self.DESCRIPTION.format(
            title=self.title,
            director=', '.join(self.director),
            writer=', '.join(self.writer),
            cast=', '.join(self.cast[:-1]) + f' and {self.cast[-1]}',
            genre=', '.join(self.genre),
            synopsis=self.synopsis,
            duration=self.duration,
            release_year=self.release_year,
            imdb_rating=self.imdb_rating,
        ))

        return movie_description
