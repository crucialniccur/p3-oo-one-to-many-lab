class Pet:

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type):
        if pet_type in Pet.PET_TYPES:
            self.name = name
            self.pet_type = pet_type
        else:
            raise Exception('Type must be among  PET_TYPES!')


class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return Pet.all
