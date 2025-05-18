class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Can only add instances of Pet.")
        pet.owner = self

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if not isinstance(name, str):
            raise Exception("Name must be a string.")
        if pet_type not in Pet.PET_TYPES:
            raise Exception("Type must be among PET_TYPES!")
        if owner is not None and not isinstance(owner, Owner):
            raise Exception("Owner must be an instance of Owner or None.")

        self.name = name
        self.pet_type = pet_type
        self.owner = owner

        Pet.all.append(self)
