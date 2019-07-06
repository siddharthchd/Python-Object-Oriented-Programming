class Dog():
    def __init__(self, breed, name, spots):
        self.breed = breed
        self.name = name
        self.spots = spots

my_dog = Dog(breed='Huskie', name='Sam', spots=False)

print(my_dog.breed + ' ' + my_dog.name + ' ' + my_dog.spots)