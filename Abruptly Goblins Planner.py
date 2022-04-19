
gamers = {}


def add_gamer(gamer, gamers_list):
    if 'name' in gamer and 'availability' in gamer:
        gamers_list.update({gamer.get('name'): gamer.get('availability')})


add_gamer({'name': 'Kimberly Warner', 'availability': ['Monday', 'Tuesday', 'Friday']}, gamers)
add_gamer({'name': 'Thomas Nelson', 'availability': ['Tuesday', 'Thursday', 'Saturday']}, gamers)
add_gamer({'name': 'Joyce Sellers', 'availability': ['Monday', 'Wednesday', 'Friday', 'Saturday']}, gamers)
add_gamer({'name': 'Michelle Reyes', 'availability': ['Wednesday', 'Thursday', 'Sunday']}, gamers)
add_gamer({'name': 'Stephen Adams', 'availability': ['Thursday', 'Saturday']}, gamers)
add_gamer({'name': 'Joanne Lynn', 'availability': ['Monday', 'Thursday']}, gamers)
add_gamer({'name': 'Latasha Bryan', 'availability': ['Monday', 'Sunday']}, gamers)
add_gamer({'name': 'Crystal Brewer', 'availability': ['Thursday', 'Friday', 'Saturday']}, gamers)
add_gamer({'name': 'James Barnes Jr.', 'availability': ['Tuesday', 'Wednesday', 'Thursday', 'Sunday']}, gamers)
add_gamer({'name': 'Michel Trujillo', 'availability': ['Monday', 'Tuesday', 'Wednesday']}, gamers)


def build_daily_frequency_table():
    return {'Monday': 0, 'Tuesday': 0, 'Wednesday': 0, 'Thursday': 0, 'Friday': 0, 'Saturday': 0, 'Sunday': 0}


count_availability = build_daily_frequency_table()


def calculate_availability(gamers_list, available_frequency):
    for days in gamers_list.values():
        for day in days:
            if day in available_frequency.keys():
                available_frequency[day] += 1
    return available_frequency


calculate_availability(gamers, count_availability)
print(count_availability)


def find_best_night(availability_table):
    days_in_order = sorted(availability_table.values())
    for day, count in availability_table.items():
        if count == days_in_order[-1]:
            return day


game_night = find_best_night(count_availability)
print(game_night)


def available_on_night(gamers_list, day):
    available_gamers = []
    for name in gamers_list.keys():
        if day in gamers_list[name]:
            available_gamers.append(name)
    return available_gamers


attending_game_night = available_on_night(gamers, game_night)
print(attending_game_night)


def form_email(name, game, day_of_week):
    return '{}, you are invited to the game of {} on {}!'.format(name, game, day_of_week)


def send_email(gamers_who_can_attend, day, game):
    for gamer in gamers_who_can_attend:
        print(form_email(gamer, game, day))


send_email(attending_game_night, game_night, 'Abruptly Goblins!')


unable_to_attend_best_night = {gamer: days for gamer, days in gamers.items() if gamer not in attending_game_night}

second_night_availability = build_daily_frequency_table()

calculate_availability(unable_to_attend_best_night, second_night_availability)

second_night = find_best_night(second_night_availability)

available_second_game_night = available_on_night(gamers, second_night)
send_email(available_second_game_night, second_night, 'Abruptly Goblins!')
