This is a small program called 'Movie Advice'.
It recommends a movie based on the movies you like.

The program uses a test database compiled from top 100 IMDB movies, so the utility
is limited, but most movies in it still have similar ones (about 85% I believe).

The algorithm is pretty basic, it doesn't take into account complex parameters,
like two movies both being about superheroes, or about WWII or made by the same studio.
That's why the result, albeit usually pretty decent, may sometimes not be perfect.

If you want to try out a program, just run the main function. To print and check out 
the whole graph, use print_graph().