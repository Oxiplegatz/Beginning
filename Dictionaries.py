letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]


letter_to_points = {key: value for key, value in zip(letters, points)}
letter_to_points[' '] = 0


def score_word(word):
    point_total = 0
    for letter in word:
        if letter not in letter_to_points.keys():
            point_total += 0
        else:
            point_total += letter_to_points.get(letter)
    return point_total


player_to_words = {'player1': ['BLUE', 'TENNIS', 'EXIT'], 'wordNerd': ['EARTH', 'EYES', 'MACHINE'], 'Lexi Con': ['ERASER', 'BELLY', 'HUSKY'], 'Prof Reader': ['ZAP', 'COMA', 'PERIOD']}
player_to_points = {}


def words_played(player, word_played):
    print(player + ' played a word: ' + word_played + '. He scores ' + str(score_word(word_played.upper())) + ' points.')
    player_to_words[player].append(word_played.upper())
    return player_to_words


def update_points_total():
    for player, words in player_to_words.items():
        player_points = 0
        for word in words:
            player_points += score_word(word)
        player_to_points[player] = player_points
    return player_to_points


print(update_points_total())

words_played('wordNerd', 'bazooka')

print(update_points_total())
