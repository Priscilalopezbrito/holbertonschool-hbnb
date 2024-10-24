#!/usr/bin/python3
from part2.hbnb.app.models.base import BaseModel
from part2.hbnb.app.models.user import User


class Place(BaseModel):
    def __init__(self, title, description, price, latitude, longitude, owner):
        super().__init__()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner
        self.reviews = []  # List to store related reviews
        self.amenities = []  # List to store related amenities

        # Validations
        self.title_validation()
        self.owner_validation()

    def title_validation(self):
        # Validates required length of title
        if not self.title or len(self.title) > 100:
            raise ValueError('Maximum length of 100 characters')

    def owner_validation(self):
        # Ensures the owner exists
        if not isinstance(self.owner, User):
            raise ValueError('Owner must be a User')

    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        self.amenities.append(amenity)
