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
        description = 'Here is a {species}, a {breed} to be exact. It is of {size} size. Its name is {name}, and it is {age} years old.'.format(
            species=self.species, breed=self.breed, name=self.name, size=self.size, age=self.age)
        if self.friendliness == 'friendly':
            description += ' {name} is a friendly animal.'.format(name=self.name)
        elif self.friendliness == 'neutral':
            description += ' {name} is a calm animal, it minds its own business.'.format(name=self.name)
        elif self.friendliness == 'aggressive':
            description += ' {name} is an agressive animal. You better watch out.'.format(name=self.name)
        return description

    def can_adopt(self):
        if self.friendliness == 'friendly' or self.friendliness == 'neutral':
            animal_species_list.pop(animal_species_list.index(self.species))
            print(
                self.__repr__() + '\nIt is now yours. Congratulations!\nWe have these animals left: ' + ', '.join(
                    animal_species_list) + '. Maybe you will recommend someone to your friends!'
            )
        else:
            alternative = input(
                'You chose to adopt {name}, the {species}. This is a wild animal, it\'s very aggressive. Unfortunately you cannot adopt it. Would you like to check out other animals? Yes/No \n'.format(
                    name=self.name, species=self.species)
            )
            if alternative == 'no' or alternative == 'No':
                print('We are sorry to hear that and we wish you all the best.')
            else:
                animal_species_list.pop(animal_species_list.index(self.species))
                alternative = input(
                    'Great! We have these animals: ' + ', '.join(animal_species_list) + '. Who would you like to adopt? \n'
                )
                if alternative in animal_species_list:
                    return animals_dict[alternative].can_adopt()
                else:
                    print('Unfortunately we don\'t have this animal.')


class Visitor:

    def __init__(self, name, age, sex, income, account_balance):
        self.name = name
        self.age = age
        self.sex = sex
        self.income = income
        if income >= 100000:
            self.income_level = 'high'
        elif income >= 50000:
            self.income_level = 'medium'
        else:
            self.income_level = 'low'
        self.account_balance = account_balance

    def __repr__(self):
        if self.sex == 'Male' or self.sex == 'male':
            return 'Our new visitor is {name}. He is {age} years old. Greetings!\n'.format(name=self.name, age=self.age)
        else:
            return 'Our new visitor is {name}. She is {age} years old. Greetings!\n'.format(name=self.name, age=self.age)

    def adopt_animal(self):
        animal_choice = input(
            'Please come in. We have many animals to adopt. Which one do you like: ' + ', '.join(animal_species_list) + '?\n')
        while animal_choice not in animal_species_list:
            animal_choice = input('We don\'t seem to have this animal. It\'s an animal, right? Please choose from the ones we have.\n')
        choice = input('I see you have chosen to adopt a {animal}. Would you like to proceed? Yes/No \n'.format(animal=animal_choice))
        if choice == 'no' or choice == 'No':
            new_choice = input('I\'m sorry to hear that. Maybe you would like to adopt someone else?\n')
            if new_choice == 'yes' or new_choice == 'Yes':
                animal_species_list.pop(animal_species_list.index(animal_choice))
                animal_choice = input('We have these animals: ' + ', '.join(animal_species_list) + '\nWho would you like to adopt?\n')
                while animal_choice not in animal_species_list:
                    animal_choice = input('We don\'t seem to have this animal. It\'s an animal, right? Please choose from the ones we have.\n')
                animals_dict[animal_choice].can_adopt()
            elif new_choice == 'no' or new_choice == 'No':
                print('Okay. Good luck!')
        elif choice == 'yes' or choice == 'Yes':
            animals_dict[animal_choice].can_adopt()
        else:
            print('Error.')

    def deduct_money(self, amount):
        self.account_balance = self.account_balance - amount

    def become_sponsor(self):
        animal_choice = input('Please come in. I\'m glad to hear that you want to sponsor one of our animals. I see you have {income} income, that might be important. You can choose who you want to sponsor:\n'.format(name=self.name, income=self.income_level) + ', '.join(animal_species_list) + '\n')
        while animal_choice not in animal_species_list:
            animal_choice = input('We don\'t seem to have this animal. It\'s an animal, right? Please choose from the ones we have.\n')
        animal_index = animal_species_list.index(animal_choice)
        deduct_amount = animals_dict[animal_choice].sponsor_cost
        choice = input('I see you have chosen to sponsor {animal}. It costs {sum} per month. Would you like to proceed? Yes/No \n'.format(animal=animal_choice, sum=deduct_amount))
        while choice not in ['no', 'No', 'yes', 'Yes']:
            choice = input('Please answer yes or no. ')
        if choice == 'no' or choice == 'No':
            print('I\'m sorry to hear that. Good luck!')
        elif choice == 'yes' or choice == 'Yes':
            if deduct_amount <= self.account_balance:
                self.deduct_money(deduct_amount)
                sponsors_list.append(self.name + ' is a sponsor of ' + animal_names_list[animal_index] + ', the ' + animal_choice + '.')
                print('Great! You have become a sponsor of {name}, the {animal}. We have deducted {sum} from your account.'.format(animal=animal_choice, sum=deduct_amount, name=animal_names_list[animal_index]))
            else:
                print('You don\'t have enough money to become a sponsor of ' + animal_names_list[animal_index] + ', the ' + animal_choice + '.')


def create_visitor():

    first_input = input('What\'s your name?\n')
    if first_input.isalpha():
        name = first_input
    else:
        name = 'John Doe'
        print('You did not provide a name, so let us call you John Doe.')

    second_input = 'How old are you?\n'
    age = check_if_number(second_input)

    third_input = input('Are you male or female?\n')
    while third_input not in ['Male', 'Female', 'male', 'female']:
        third_input = input('Please choose Male or Female:\n')
    sex = third_input

    fourth_input = 'What\'s your annual income in USD?\n'
    income = check_if_number(fourth_input)

    fifth_input = 'How much are you ready to spend in our shelter?\n'
    balance = check_if_number(fifth_input)

    return multichoice(Visitor(name, age, sex, income, balance))


def multichoice(visitor):
    choice = input('Hello {name} and welcome to our shelter! Here you can adopt someone or become a sponsor for one of our wonderful animals. What would you like to do?\n'.format(name=visitor.name))
    while choice not in ['sponsor', 'adopt', 'Sponsor', 'Adopt']:
        choice = input('Please answer "adopt" or "sponsor"\n')
    if choice == 'adopt' or choice == 'Adopt':
        print(visitor)
        visitor.adopt_animal()
    else:
        print(visitor)
        visitor.become_sponsor()


def check_if_number(user_input):
    while True:
        try:
            number = int(input(user_input))
        except ValueError:
            print('That is not a number.')
            continue
        else:
            return number


dog_bucky = Animal('dog', 'chihuahua', 'Bucky', 6, 'small', 'neutral', 500)
cat_liz = Animal('cat', 'tabby', 'Liz', 2, 'small', 'friendly', 300)
giraffe_brian = Animal('giraffe', 'northern giraffe', 'Tower', 10, 'large', 'aggressive', 6000)
croc_jumbo = Animal('crocodile', 'cmerican alligator', 'Jumbo', 4, 'large', 'aggressive', 2000)
chameleon_shadow = Animal('chameleon', 'carpet chameleon', 'Shadow', 3, 'medium', 'neutral', 1000)
eagle_stripes = Animal('eagle', 'bald eagle', 'Stripes', 6, 'large', 'neutral', 1200)
hamster_buncho = Animal('hamster', 'domestic hamster', 'Buncho', 2, 'small', 'friendly', 200)
fish_ponyo = Animal('aquarium fish', 'guppies', 'Ponyo', 1, 'small', 'neutral', 100)
snake_snakey = Animal('snake', 'cobra', 'Ssssisy', 12, 'medium', 'aggressive', 800)
monkey_bananas = Animal('monkey', 'chimpanzee', 'Bananas', 6, 'medium', 'friendly', 2400)

animals_dict = {dog_bucky.species: dog_bucky, cat_liz.species: cat_liz, giraffe_brian.species: giraffe_brian,
                croc_jumbo.species: croc_jumbo, chameleon_shadow.species: chameleon_shadow,
                eagle_stripes.species: eagle_stripes, hamster_buncho.species: hamster_buncho,
                fish_ponyo.species: fish_ponyo, snake_snakey.species: snake_snakey, monkey_bananas.species: monkey_bananas}

animal_species_list = [dog_bucky.species, cat_liz.species, giraffe_brian.species, croc_jumbo.species,
                       chameleon_shadow.species, eagle_stripes.species, hamster_buncho.species, fish_ponyo.species, snake_snakey.species, monkey_bananas.species]

animal_names_list = [value.name for value in animals_dict.values()]

animal_sponsorship_list = [value.sponsor_cost for value in animals_dict.values()]

sponsors_list = []

print('''
   _____ __         ____           
  / ___// /_  ___  / / /____  _____
  \__ \/ __ \/ _ \/ / __/ _ \/ ___/
 ___/ / / / /  __/ / /_/  __/ /    
/____/_/ /_/\___/_/\__/\___/_/  
''')

create_visitor()

print('')
finish = input('Press "Enter" to exit.')
