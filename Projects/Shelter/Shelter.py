import random


class Animal:

    def __init__(self, species, breed, name, age, size, friendliness, sponsor_cost):
        self.species = species
        self.breed = breed
        self.name = name
        self.age = age
        self.size = size
        self.friendliness = friendliness
        self.sponsor_cost = sponsor_cost

    def __repr__(self):
        description = '\nHere is a {species}, a {breed} to be exact. It is of {size} size.' \
                      ' Its name is {name}, and it is {age} years old.'.format(species=self.species, breed=self.breed,
                                                                               name=self.name, size=self.size,
                                                                               age=self.age)
        if self.friendliness == 'friendly':
            description += ' {name} is a friendly animal.'.format(name=self.name)
        elif self.friendliness == 'neutral':
            description += ' {name} is a calm animal, it minds its own business.'.format(name=self.name)
        elif self.friendliness == 'aggressive':
            description += ' {name} is an agressive animal. You better watch out.'.format(name=self.name)
        return description

    def can_adopt(self):
        if self.friendliness == 'friendly' or self.friendliness == 'neutral':
            the_shelter.remove_animal(self)
            current_animals = the_shelter.set_current_animals()
            print(self.__repr__() + '\n\nIt is now yours. Congratulations!\n\nWe have these animals'
                                    ' up for adoption: ' + ', '.join(
                current_animals) + '. Maybe you will recommend someone to your friends!')
        else:
            current_animals = the_shelter.set_current_animals()
            current_animals.remove(self.species)
            alternative = input('You want to adopt {name}, the {species}. This is a wild animal,'
                                ' it\'s very aggressive. Unfortunately you cannot adopt it.'
                                ' Would you like to check out other animals? Yes/No\n'.format(name=self.name,
                                                                                              species=self.species))
            while alternative.lower() not in ['yes', 'no']:
                alternative = input('Please answer "yes" or "no".\n')
            if alternative.lower() == 'no':
                print('We are sorry to hear that, and we wish you all the best.')
                return
            alternative = input(
                'Great! We have these animals: ' + ', '.join(current_animals)
                + '. Who would you like to adopt? \n')
            current_animals = the_shelter.set_current_animals()
            if alternative in current_animals:
                animals[current_animals.index(alternative)].can_adopt()
            else:
                print('Unfortunately we don\'t have this animal.')


class Shelter:

    def __init__(self, animals_list):
        self.animals_list = animals_list

    def __repr__(self):
        random_animals = []
        for i in range(3):
            random_animals.append(self.set_current_animals()[random.randint(0, (len(self.animals_list) - 1))])
        return 'This is an animal shelter. We have all kind of animals' \
               ' you can adopt or sponsor. Here are some of the animals we currently' \
               ' have: ' + ', '.join(random_animals) + '.\n\nPlease tell us about yourself.'

    def get_animals(self):
        return self.animals_list

    def set_current_animals(self):
        current_animals = [animal.species for animal in self.animals_list]
        return current_animals

    def remove_animal(self, animal):
        self.animals_list.remove(animal)

    def add_animal(self, animal):
        if animal is Animal:
            if animal not in self.animals_list:
                self.animals_list.append(animal)
                print('Successfully added {animal} to the shelter.'.format(animal=animal.species))
                return
            print('We already have {name}, the {animal} in our shelter.'.format(animal=animal.species,
                                                                                name=animal.name))
        else:
            print('Error. We accept only animals.')


class Visitor:

    def __init__(self, name, age, sex, account_balance):
        self.name = name
        self.age = age
        self.sex = sex
        self.account_balance = account_balance

    def __repr__(self):
        if self.sex.lower() == 'male':
            return '\nOur new visitor is {name}. He is {age} years old.' \
                   ' Greetings!\n'.format(name=self.name, age=self.age)
        else:
            return '\nOur new visitor is {name}. She is {age} years old.' \
                   ' Greetings!\n'.format(name=self.name, age=self.age)

    def adopt_animal(self):
        animals_list = the_shelter.get_animals()
        current_animals = the_shelter.set_current_animals()
        animal_choice = input('Please come in. We have many animals to adopt.'
                              ' Which one do you like: ' + ', '.join(current_animals) + '?\n')
        while animal_choice not in current_animals:
            animal_choice = input('\nWe don\'t seem to have this animal.'
                                  ' It\'s an animal, right? Please choose from the ones we have.\n')
        choice = input('\nI see you have chosen to adopt a {animal}.'
                       ' Would you like to proceed? Yes/No\n'.format(animal=animal_choice))
        while choice.lower() not in ['yes', 'no']:
            choice = input('\nPlease answer "yes" or "no".\n')
        if choice.lower() == 'no':
            new_choice = input('\nI\'m sorry to hear that. Maybe you would like to adopt someone else?\n')
            if new_choice.lower() == 'yes':
                current_animals.remove(animal_choice)
                animal_choice = input('\nWe have these animals: ' + ', '.join(current_animals) +
                                      '\nWho would you like to adopt?\n')
                while animal_choice not in current_animals:
                    animal_choice = input('\nWe don\'t seem to have this animal. It\'s an animal, right?'
                                          ' Please choose from the ones we have.\n')
                current_animals = the_shelter.set_current_animals()
                animals_list[current_animals.index(animal_choice)].can_adopt()
            elif new_choice.lower() == 'no':
                print('\nOkay. Good luck then!')
            else:
                print('\nError')
            return
        if choice.lower() == 'yes':
            animals_list[current_animals.index(animal_choice)].can_adopt()
        return

    def deduct_money(self, amount):
        self.account_balance -= amount

    def become_sponsor(self):
        animals_list = the_shelter.get_animals()
        current_animals = the_shelter.set_current_animals()
        animal_choice = input('Please come in. I\'m happy to hear that you want'
                              ' to sponsor one of our animals. You can choose who'
                              ' you want to sponsor:\n'.format(name=self.name) +
                              ', '.join(current_animals) + '\n')
        while animal_choice not in current_animals:
            animal_choice = input('We don\'t seem to have this animal. It\'s an animal, right?'
                                  ' Please choose from the ones we have.\n')
        deduct_amount = animals_list[current_animals.index(animal_choice)].sponsor_cost
        animal_name = animals_list[current_animals.index(animal_choice)].name
        choice = input('I see you have chosen to sponsor {animal}. It costs {sum} dollars per month.'
                       ' Would you like to proceed? Yes/No \n'.format(animal=animal_choice, sum=deduct_amount))
        while choice.lower() not in ['yes', 'no']:
            choice = input('Please answer yes or no.\n')
        if choice.lower() == 'no':
            print('I\'m sorry to hear that. Good luck!')
        elif choice.lower() == 'yes':
            if deduct_amount <= self.account_balance:
                self.deduct_money(deduct_amount)
                sponsors_list.append(animal_name + ', the ' + animal_choice + ' is sposored by ' + self.name + '.')
                print('Great! You have become a sponsor of {name}, the {animal}.'
                      ' We have deducted {sum} dollars from your account.'.format(
                        animal=animal_choice, sum=deduct_amount, name=animal_name))
                print('You have been added to the list of our sponsors!\n\nSponsors List\n' + '\n'.join(sponsors_list))
            else:
                print('You don\'t have enough money to become a sponsor of'
                      ' ' + animal_name + ', the ' + animal_choice + '.')


def create_visitor():
    input_one = input('\nWhat is your name?\n')
    if input_one.isalpha():
        name = input_one
    else:
        name = 'John Doe'
        print('\nYou did not provide a name, so let us call you John Doe.')

    input_two = '\nHow old are you?\n'
    age = check_if_number(input_two)

    input_three = input('\nAre you male or female?\n')
    while input_three.lower() not in ['male', 'female']:
        input_three = input('\nPlease choose Male or Female:\n')
    sex = input_three

    input_four = '\nHow much USD are you ready to donate?\n'
    balance = check_if_number(input_four)

    return choose_action(Visitor(name, age, sex, balance))


def choose_action(visitor):
    choice = input('\nHello {name} and welcome to our shelter! Here you can adopt someone'
                   ' or become a sponsor for one of our wonderful animals. What would you'
                   ' like to do?\n'.format(name=visitor.name))
    while choice.lower() not in ['sponsor', 'adopt']:
        choice = input('Please answer "adopt" or "sponsor"\n')
    if choice == 'adopt' or choice == 'Adopt':
        print(visitor)
        return visitor.adopt_animal()
    print(visitor)
    return visitor.become_sponsor()


def check_if_number(user_input):
    while True:
        try:
            number = int(input(user_input))
        except ValueError:
            print('That is not a number.')
            continue
        else:
            return number


dog_bucky = Animal('dog', 'chihuahua', 'Bucky', 6, 'small', 'neutral', 200)
cat_liz = Animal('cat', 'tabby', 'Liz', 2, 'small', 'friendly', 100)
giraffe_brian = Animal('giraffe', 'northern giraffe', 'Tower', 10, 'large', 'aggressive', 600)
croc_jumbo = Animal('crocodile', 'cmerican alligator', 'Jumbo', 4, 'large', 'aggressive', 200)
chameleon_shadow = Animal('chameleon', 'carpet chameleon', 'Shadow', 3, 'medium', 'neutral', 100)
eagle_stripes = Animal('eagle', 'bald eagle', 'Stripes', 6, 'large', 'neutral', 300)
hamster_buncho = Animal('hamster', 'domestic hamster', 'Buncho', 2, 'small', 'friendly', 200)
fish_ponyo = Animal('aquarium fish', 'guppies', 'Ponyo', 1, 'small', 'neutral', 100)
snake_snakey = Animal('snake', 'cobra', 'Ssssissy', 12, 'medium', 'aggressive', 90)
monkey_chip = Animal('monkey', 'chimpanzee', 'Chip', 6, 'medium', 'friendly', 400)

animals = [dog_bucky, cat_liz, giraffe_brian, croc_jumbo, chameleon_shadow,
           eagle_stripes, hamster_buncho, fish_ponyo, snake_snakey, monkey_chip]

the_shelter = Shelter(animals)

sponsors_list = []

print('''
   _____ __         ____           
  / ___// /_  ___  / / /____  _____
  \__ \/ __ \/ _ \/ / __/ _ \/ ___/
 ___/ / / / /  __/ / /_/  __/ /    
/____/_/ /_/\___/_/\__/\___/_/  
''')

print(the_shelter)

create_visitor()

print('')
exit_variable = input('Press Enter to close the program.')
