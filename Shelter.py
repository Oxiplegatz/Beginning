class Animal:

    def __init__(self, species, breed, name, age, size, friendliness):
        self.species = species
        self.breed = breed
        self.name = name
        self.age = age
        self.size = size
        self.friendliness = friendliness

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
            animal_names_list.pop(animal_names_list.index(self.species))
            print(
                self.__repr__() + '\nIt is now yours. Congratulations!\nWe have these animals left: ' + ', '.join(
                    animal_names_list) + '. Maybe you will recommend someone to your friends!'
            )
        else:
            alternative = input(
                'You chose to adopt {name}, the {species}. This is a wild animal, it\'s very aggressive. Unfortunately you cannot adopt it. Would you like to check out other animals? Yes/No \n'.format(
                    name=self.name, species=self.species)
            )
            if alternative == 'no' or alternative == 'No':
                print('We are sorry to hear that and we wish you all the best.')
            else:
                animal_names_list.pop(animal_names_list.index(self.species))
                alternative = input(
                    'Great! We have these animals: ' + ', '.join(animal_names_list) + ' Who would you like to adopt? \n'
                )
                if alternative in animal_names_list:
                    return animals_dict[alternative].can_adopt()
                else:
                    print('Unfortunately we don\'t have this animal.')

        # def is_quarantined(self, on_quarantine = True):


class Visitor:

    def __init__(self, name, age, sex, income):
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

    def __repr__(self):
        if self.sex == 'Male':
            return 'Our new visitor is {name}. He is {age} years old. Greetings!\n'.format(name=self.name, age=self.age)
        else:
            return 'Our new visitor is {name}. She is {age} years old. Greetings!\n'.format(name=self.name, age=self.age)

    def adopt_animal(self):
        animal_choice = input(
            'Hello {name}! I see you are {age} years old. You have {income} income, that might be important.\nWe have many animals to adopt. Which one do you like: '.format(
                name=self.name, age=self.age, income=self.income_level) + ', '.join(animal_names_list) + '? \n')
        while animal_choice not in animal_names_list:
            animal_choice = input('We don\'t seem to have this animal. It\'s an animal, right? Please choose from the ones we have.\n')
        if animal_choice in animal_names_list:
            choice = input('I see you have chosen to adopt a {animal}. Would you like to proceed? Yes/No \n'.format(animal=animal_choice))
            if choice == 'no' or choice == 'No':
                print('I\'m sorry to hear that. Good luck!')
            elif choice == 'yes' or choice == 'Yes':
                animals_dict[animal_choice].can_adopt()
            else:
                print('Error.')

    # def become_sponsor(self)


dog_bucky = Animal('dog', 'chihuahua', 'Bucky', 6, 'small', 'neutral')
cat_liz = Animal('cat', 'tabby', 'Liz', 2, 'small', 'friendly')
giraffe_brian = Animal('giraffe', 'northern giraffe', 'Tower', 10, 'large', 'aggressive')
croc_jumbo = Animal('crocodile', 'cmerican alligator', 'Jumbo', 4, 'large', 'aggressive')
chameleon_shadow = Animal('chameleon', 'carpet chameleon', 'Shadow', 3, 'medium', 'neutral')
eagle_stripes = Animal('eagle', 'bald eagle', 'Stripes', 6, 'large', 'neutral')
hamster_buncho = Animal('hamster', 'domestic hamster', 'Buncho', 2, 'small', 'friendly')
fish_ponyo = Animal('aquarium fish', 'guppies', 'Ponyo', 1, 'small', 'neutral')
snake_snakey = Animal('snake', 'cobra', 'Ssssisy', 12, 'medium', 'aggressive')
monkey_bananaman = Animal('monkey', 'chimpanzee', 'Bananaman', 6, 'medium', 'friendly')

animals_dict = {dog_bucky.species: dog_bucky, cat_liz.species: cat_liz, giraffe_brian.species: giraffe_brian,
                croc_jumbo.species: croc_jumbo, chameleon_shadow.species: chameleon_shadow,
                eagle_stripes.species: eagle_stripes, hamster_buncho.species: hamster_buncho,
                fish_ponyo.species: fish_ponyo, snake_snakey.species: snake_snakey, monkey_bananaman.species: monkey_bananaman}

animal_names_list = [dog_bucky.species, cat_liz.species, giraffe_brian.species, croc_jumbo.species,
                     chameleon_shadow.species, eagle_stripes.species, hamster_buncho.species, fish_ponyo.species, snake_snakey.species, monkey_bananaman.species]

visitor_one = Visitor('Alexei', 37, 'Male', 60000)
visitor_two = Visitor('Sheila', 21, 'Female', 140000)

print(visitor_two)
visitor_two.adopt_animal()
