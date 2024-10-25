#!/usr/bin/python3
from part2.hbnb.app.models.base import BaseModel
from part2.hbnb.app.models.user import User


class Place(BaseModel):
    def __init__(self, title, description, price, latitude, longitude, owner, amenities):
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
        self.validations()

    def validations(self):
        # Validates required length of title
        if not self.title or len(self.title) > 100:
            raise ValueError('Maximum length of 100 characters')

        # Ensures the owner exists
        if not isinstance(self.owner, User):
            raise ValueError('Owner must be a User')

        # Price must be a positive value
        if self.price < 1:
            raise ValueError('Price must be greater than 0')

        # Latitude must be within the range of -90.0 to 90.0.
        if not (-90.0 <= self.latitude <= 90.0):
            raise ValueError('Latitude must be between -90 and 90')
        # Longitude must be within the range of -180.0 to 180.0.
        if not (-180.0 <= self.longitude <= 180.0):
            raise ValueError('Longitude must be between -180 and 180')

    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        self.amenities.append(amenity)
