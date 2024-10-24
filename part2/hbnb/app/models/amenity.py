#!/usr/bin/python3
from part2.hbnb.app.models.base import BaseModel


class Amenity(BaseModel):
    def __init__(self, name):
        super().__init__()
        self.name = name
