from movieclass import Movie


def calculate_similarity(movie_one: Movie, movie_two: Movie) -> float:
    """Calculates similarity between two movies and returns the similarity score."""
    similarity_score = 0

    for movie_one_director in movie_one.director:
        if movie_one_director in movie_two.director:
            # The common director contributes to similarity more than other factors
            similarity_score += 2.0

    for movie_one_genre in movie_one.genre:
        # The common genre has the least weight among all factors
        if movie_one_genre in movie_two.genre:
            similarity_score += 0.5

    for movie_one_writer in movie_one.writer:
        if movie_one_writer in movie_two.writer:
            similarity_score += 1.0

    for movie_one_actor in movie_one.cast:
        if movie_one_actor in movie_two.cast:
            similarity_score += 1.0

    return similarity_score


def get_common_attributes(movie_one: Movie, movie_two: Movie) -> str:
    """Return all common attributes of two given movies."""
    common_attributes = ''

    common_directors = []
    for movie_one_director in movie_one.director:
        if movie_one_director in movie_two.director:
            common_directors.append(movie_one_director)
    if common_directors:
        common_attributes += 'Director: {}\n'.format(', '.join(common_directors))

    common_genres = []
    for movie_one_genre in movie_one.genre:
        if movie_one_genre in movie_two.genre:
            common_genres.append(movie_one_genre)
    if common_genres:
        common_attributes += 'Genre: {}\n'.format(', '.join(common_genres))

    common_writers = []
    for movie_one_writer in movie_one.writer:
        if movie_one_writer in movie_two.writer:
            common_writers.append(movie_one_writer)
    if common_writers:
        common_attributes += 'Writers: {}\n'.format(', '.join(common_writers))

    common_actors = []
    for movie_one_actor in movie_one.cast:
        if movie_one_actor in movie_two.cast:
            common_actors.append(movie_one_actor)
    if common_actors:
        common_attributes += 'Cast: {}\n'.format(', '.join(common_actors))

    if (
            movie_one.release_year in range(movie_two.release_year, movie_two.release_year + 5)
            or
            movie_two.release_year in range(movie_one.release_year, movie_one.release_year + 5)
    ):
        common_attributes += f'Release year: {movie_two.release_year}, {movie_one.release_year}\n'

    if common_attributes:
        return f'\nHere is what {movie_two.title} and {movie_one.title} have in common:\n{common_attributes}'

    return 'The movies have nothing in common!'
