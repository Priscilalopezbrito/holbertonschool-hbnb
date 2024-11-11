#!/usr/bin/python3
from part3.hbnb.app.models.base import BaseModel
from part3.hbnb.app import bcrypt  # Import here to avoid circular import


class User(BaseModel):
    # emails = set()  # Class-level set to store unique emails

    def __init__(self, first_name, last_name, email, is_admin=False, password=None):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin
        self.password = password

        # Validations
        self.validate_name()
        self.validate_email()

    def validate_name(self):
        # First name length validation
        if not self.first_name or len(self.first_name) > 50:
            raise ValueError('First name must be less than 50 characters.')
        # Last name length validation
        if not self.last_name or len(self.last_name) > 50:
            raise ValueError('Last name must be less than 50 characters.')

    def validate_email(self):
        # Checks valid email format  verify
        if not self.email or "@" not in self.email or "." not in self.email:
            raise ValueError('Invalid email format.')

        # Checks email uniqueness
        """
        if self.email in User.emails:
            raise ValueError('Email already exists.')

            # If valid and unique, add to the set of emails
        User.emails.add(self.email)
        
        
        **************************************************************************
        nota: usar get_user_by_email() para validar si el email ya esta registrado
        **************************************************************************
        
        """

    # This function should take a plaintext password,
    # hash it using bcrypt,
    # and store the hashed version in
    # the password field.

    def hash_password(self, password):
        """Hashes the password before storing it."""
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    # compare a plaintext password with the hashed
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
        if email:  # Cambio en validacion email unico
            old_email = self.email
            self.email = email
            User.emails.discard(old_email)
            self.validate_email()

        if is_admin is not None:
            self.is_admin = is_admin

        # Update timestamp
        self.save()
