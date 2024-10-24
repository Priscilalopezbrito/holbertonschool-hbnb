#!/usr/bin/python3
from datetime import datetime

from part2.hbnb.app.models.base import BaseModel


class Review(BaseModel):
    def __init__(self, text, rating, place, user):
        super().__init__()
        self.text = text
        self.rating = rating
        self.place = place
        self.user = user
