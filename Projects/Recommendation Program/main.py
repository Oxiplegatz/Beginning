from movieclass import Movie
from graph import Graph
from calculations import get_common_attributes
from builders import movies, movies_graph

AFFIRMATIVE = ['y', 'ye', 'yes', 'yeah']
UNSUCCESSFUL = 'I am sorry I could not help you. Good luck!'


def welcome() -> None:
    """A function that prints the opening message."""
    print('Welcome to "Movie Advice"! This program can recommend a movie based on the movies you like.')


def get_movie_info(movie: Movie) -> None:
    """Prints description of a movie."""
    description = Movie.get_description(movie)
    print(description)


def choose_movie(movies_list: dict[str: Movie]) -> None:
    """Receives user input, finds all corresponding movies in the database and lets user choose one."""
    chosen_movies = []
    user_input = input('Please select a movie. Start typing a title and press Enter to see if a movie you think of'
                       ' is in the database:\n').lower()

    for movie in movies_list:
        if movie.title.lower().startswith(user_input) or movie.title.lower().startswith(f'the {user_input}'):
            chosen_movies.append(movie)

    if len(chosen_movies) == 1:
        user_input = input(f'There is only one movie in the database that matches'
                           f' your input: {chosen_movies[0].title}. Would you like to find similar movies? y/n\n')
        if user_input.lower() in AFFIRMATIVE:
            return find_similar(chosen_movies[0], movies_graph)
        else:
            repeat_choice = input('I am sorry to hear that. Would you like to try and look for more movies? y/n\n')
            if repeat_choice in AFFIRMATIVE:
                return choose_movie(movies.values())
            else:
                print(UNSUCCESSFUL)
                return

    if len(chosen_movies) > 1:
        list_num = 1
        list_indices = []
        print('"Movie Advice" have found these movies:\n')
        for movie in chosen_movies:
            list_indices.append(list_num)
            print(f'{list_num}. {movie.title}')
            list_num += 1

        user_input = input('\nPlease choose a movie, and I will try to find similar ones. You do not have'
                           ' to type the full name of the movie, just the number:\n')

        while not user_input.isdigit():
            user_input = input('Please choose a number from the list:\n')
        if int(user_input) not in list_indices:
            print('Error. Number not in list.')
            return

        movie_index = int(user_input) - 1
        movie_of_choice = chosen_movies[movie_index]

        return find_similar(movie_of_choice, movies_graph)

    else:
        repeat_choice = input('Unfortunately, there are no matching movies in the database. Would you like'
                              ' to try again? y/n\n')
        if repeat_choice.lower() in AFFIRMATIVE:
            return choose_movie(movies.values())
        else:
            print(UNSUCCESSFUL)


def find_similar(movie_of_choice: Movie, graph: Graph) -> None:
    """Finds all movies similar to a given movie using a pre-built graph."""
    movie_title = movie_of_choice.title
    similar_movies = graph.graph_dict[movie_title].get_edges()
    if similar_movies:
        print(f'Your movie of choice is {movie_title}. Here are movies that look most similar to it:')

        # The code below is a bit redundant, it can be done easier
        # without this, but here it is implemented as an exercise in graphs
        result_dict = {}

        for movie in similar_movies:
            similarity_score = graph.graph_dict[movie_title].get_edge_weight(movie)
            result_dict[movie] = similarity_score
        result_dict_sorted = sorted(result_dict.items(), key=lambda x: x[1], reverse=True)

        # As a result the function prints out top 3 movies with the highest similarity score,
        # along with all their common attributes
        for movie, similarity_score in result_dict_sorted[:3]:
            print('─' * 10)
            print(f'{movie}\nSimilarity score: {similarity_score} out of 10.0\n')
            get_movie_info(movies[movie])
            print(get_common_attributes(movies[movie], movie_of_choice))
        return

    user_input = input(f'Your movie of choice is {movie_title}. Unfortunately, there are no similar movies'
                       f' in the database. Would you like to try a new search? y/n\n')
    if user_input in AFFIRMATIVE:
        return choose_movie(movies.values())
    else:
        print(UNSUCCESSFUL)


def main():
    welcome()
    choose_movie(movies.values())


if __name__ == '__main__':
    main()
