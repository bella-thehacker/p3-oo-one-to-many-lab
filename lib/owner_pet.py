class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []
    def __init__ (self,name,pet_type,owner=None):
        self.name = name

        if pet_type not in Pet.PET_TYPES:
            raise Exception (f"Invalid pet_type: {pet_type}.")
        self.pet_type = pet_type

        if owner and not isinstance(owner, Owner):
            raise Exception("Owner must be an instance of Owner Class")

        self.owner = owner
        if self.owner:
            self.owner.add_pet(self)
        Pet.all.append(self)

class Owner:
    def __init__(self,name):
        self.name = name
        self._pets = []

    def pets(self):
        return self._pets

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("add_pets only accepts objects of type Pet")

        pet.owner = self
        self._pets.append(pet)

    def get_sorted_pets(self):
        return sorted(self._pets, key=lambda pet: pet.name)



owner1 = Owner("Ben")
pet =Pet("Whiskers", "cat", owner1)
pet1 =Pet("Fido", "dog", owner1)
pet2 = Pet("Clifford", "dog", owner1)


owner2 = Owner("John")
pet1 =Pet("Fido", "dog", owner2)
pet2 = Pet("Clifford", "dog", owner2)
pet3 = Pet("Whiskers", "cat", owner2)
pet4 = Pet("Jerry", "reptile", owner2)

print(f"{owner1.name}'s pets: {[pet.name for pet in owner1.pets()]}")
print(f"{owner1.name}'s sorted pets: {[pet.name for pet in owner1.get_sorted_pets()]}")

# John's pets
print(f"{owner2.name}'s pets: {[pet.name for pet in owner2.pets()]}")
print(f"{owner2.name}'s sorted pets: {[pet.name for pet in owner2.get_sorted_pets()]}")
