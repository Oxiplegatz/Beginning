from movieclass import Movie


def calculate_similarity(movie_one: Movie, movie_two: Movie) -> float:
    """Calculates similarity between two movies and returns the similarity factor."""
    similarity_factor = 0

    if movie_one.director == movie_two.director:
        # The common director contributes to similarity more than other factors
        similarity_factor += 2

    for movie_one_genre in movie_one.genre:
        # The common genre has the least weight among all factors
        for movie_two_genre in movie_two.genre:
            if movie_one_genre == movie_two_genre:
                similarity_factor += 0.5

    for movie_one_writer in movie_one.writer:
        for movie_two_writer in movie_two.writer:
            if movie_one_writer == movie_two_writer:
                similarity_factor += 1

    for movie_one_actor in movie_one.cast:
        for movie_two_actor in movie_two.cast:
            if movie_one_actor == movie_two_actor:
                similarity_factor += 1

    return similarity_factor
