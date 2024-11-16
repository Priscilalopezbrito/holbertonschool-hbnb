#!/usr/bin/python3
from .baseclass import BaseModel
from part3.hbnb.app.models.user import User
from part3.hbnb.app import bcrypt, db
import uuid
import re

# Association Table for Many-to-Many relationship between Place and Amenity  task 9
'''  
place_amenity = db.Table(
    'place_amenity',
    db.Model.metadata,
    db.Column('place_id', db.Integer, db.ForeignKey('places.id'), primary_key=True),
    db.Column('amenity_id', db.Integer, db.ForeignKey('amenities.id'), primary_key=True)
)
'''


class Place(BaseModel):
    __tablename__ = 'places'  # task 8
    # Allow reuse if table already exists in MetaData
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String, nullable=True)
    price = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float, nullable=True)
    longitude = db.Column(db.Float, nullable=True)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # task 9

    # One-to-Many relationship with Review
    reviews = db.relationship('hbnb.app.models.review.Review', backref='place', lazy=True)

    def __init__(self, title, description, price, latitude, longitude, user_id, amenities):
        super().__init__()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.user_id = user_id
        self.reviews = []  # List to store related reviews
        self.amenities = []  # List to store related amenities

        # Validations
        self.validations()

    def validations(self):
        # Validates required length of title
        if not self.title or len(self.title) > 100:
            raise ValueError('Maximum length of 100 characters')

        # Ensures the owner exists
        ''' 
        if not isinstance(self.user_id, User):
            raise ValueError('Owner must be a User')
        '''
        if not db.session.query(User).get(self.user_id):
            raise ValueError('Owner must be a valid User')

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
