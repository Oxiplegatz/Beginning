from graph import Vertex, Graph
from movieclass import Movie
from movies_dict import movies_database
from calculations import calculate_similarity


def get_similarity_dict(chosen_movie: Movie) -> dict:
    """Creates a dictionary of all movies similar to a given movie with their respective similarity scores."""
    similar_movies = {}

    for movie in movies.values():
        if chosen_movie != movie:
            similarity_score = calculate_similarity(chosen_movie, movie)
            # If similarity score is 1 or less, the function disregards similarity as minor
            if similarity_score > 1.0:
                similar_movies[movie.title] = similarity_score

    return similar_movies


def build_graph(movies_list: dict.values) -> Graph:
    """Creates a graph from a given list of Movie objects."""
    graph = Graph()

    for movie in movies_list:
        vertex = Vertex(movie.title)
        edges_base = get_similarity_dict(movie)
        for key, value in edges_base.items():
            vertex.add_edge(key, value)
        graph.add_vertex(vertex)

    return graph


def create_info_dict(movies_dict: dict) -> dict:
    """Formats a database to a dictionary {title: Movie}."""
    all_movies = {}

    for movie in movies_dict:
        movie_to_add = Movie(*movies_dict[movie])
        all_movies[movie] = movie_to_add
    return all_movies


movies = create_info_dict(movies_database)
movies_graph = build_graph(movies.values())
