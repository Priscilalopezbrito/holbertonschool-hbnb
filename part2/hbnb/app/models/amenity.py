#!/usr/bin/python3
from part2.hbnb.app.models.base import BaseModel


class Amenity(BaseModel):
    def __init__(self, name):
        super().__init__()
        self.name = name

        # Validations
        self.amenity_validation()

    def amenity_validation(self):
        # Required, maximum length of 50 characters.
        if not self.name or len(self.name) > 50:
            raise ValueError("Amenity name must be less than 50 characters")


