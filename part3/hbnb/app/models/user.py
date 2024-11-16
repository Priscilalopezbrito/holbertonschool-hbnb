#!/usr/bin/python3
from .baseclass import BaseModel
from part3.hbnb.app import bcrypt, db
import re


class User(BaseModel):
    __tablename__ = 'user'  # task 7
    __table_args__ = {'extend_existing': True}

    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    def __init__(self, first_name, last_name, email, is_admin=False, password=None):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin
        self.password = password

        # Validations
        self.validate_name()
        #  self.validate_email()

    def validate_name(self):
        # First name length validation
        if not self.first_name or len(self.first_name) > 50:
            raise ValueError('First name must be less than 50 characters.')
        # Last name length validation
        if not self.last_name or len(self.last_name) > 50:
            raise ValueError('Last name must be less than 50 characters.')

    # def validate_email(self):
    #     from part3.hbnb.app.services.facade import HBnBFacade
    #     facade = HBnBFacade()
    #     # Checks valid email format  verify
    #     email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    #     if not self.email or not re.match(email_regex, self.email):
    #         raise ValueError('Invalid email format.')
    #
    #     # Checks email uniqueness
    #     existing_user = facade.get_user_by_email(self.email)
    #     if existing_user:
    #         raise ValueError("A user with this email already exists.")

    # This function should take a plaintext password,
    # hash it using bcrypt,
    # and store the hashed version in
    # the password field.

    def hash_password(self, password):
        """Hashes the password before storing it."""
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    # Compare a plaintext password with the hashed
    # password stored in the password field, returning
    # True if they match and False otherwise

    def verify_password(self, password):
        """Verifies if the provided password matches the hashed password."""
        return bcrypt.check_password_hash(self.password, password)

    def update(self, first_name: str = None, last_name: str = None, email: str = None, is_admin: bool = None):
        if first_name:
            self.first_name = first_name
            self.validate_name()
        if last_name:
            self.last_name = last_name
            self.validate_name()
        if email:
            self.email = email
            self.validate_email()

        if is_admin is not None:
            self.is_admin = is_admin

        # Update timestamp
        self.save()
