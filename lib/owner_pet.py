class Pet:

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    def __init__(self, name, pet_type):
        self.name = name
        self.pet_type = pet_type


class Owner:
    def __init__(self, name):
        self.name = name
