# Animal management in a pet store

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.fed = False

    def sold(self):
        self.fed = False

    def __str__(self):
        return f"{self.name} is a {self.species} - {"is fed" if self.fed else "is hungry"}"


class PetStore:
    def __init__(self, name):
        self.name = name
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def show_animals(self):
        for animal in self.animals:
            print(animal)

    def feed_animals(self):
        for animal in self.animals:
            animal.fed = True
            print(f"{animal.name} is fed")

    def sell_animal(self, name):
        for animal in self.animals:
            if animal.name == name:
                animal.sold()
                self.animals.remove(animal)
                print(f"\n{animal.name} is sold to a new owner\n")
                break

            print(f"\n[!] {animal.name} is not available")

    def __str__(self):
        return f"\n{self.name}: has {len(self.animals)} animals"


if __name__ == '__main__':

    store = PetStore("Pet Store")

    dog = Animal("Max", "Dog")
    cat = Animal("Tom", "Cat")

    store.add_animal(dog)
    store.add_animal(cat)

    store.show_animals()

    store.feed_animals()

    store.show_animals()

    print(store)

    store.sell_animal("Max")

    store.show_animals()

    print(store)
