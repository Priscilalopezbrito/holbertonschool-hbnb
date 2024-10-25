from part2.hbnb.app.models.base import BaseModel
from part2.hbnb.app.models.place import Place
from part2.hbnb.app.models.user import User


class Review(BaseModel):
    def __init__(self, text, rating, place, user):
        super().__init__()
        self.text = text
        self.rating = rating
        # Store only the id of Place and User to avoid serialization issues
        self.place_id = place.id if isinstance(place, Place) else place
        self.user_id = user.id if isinstance(user, User) else user

        self.validations()

    def validations(self):
        # Rating validation, must be between 0 and 5
        if self.rating < 0 or self.rating > 5:
            raise ValueError("Rating must be between 0 and 5")

        # Review text can't be empty
        if self.text is None:
            raise ValueError("Review required")

        # Validate place and user ids to ensure they are properly assigned
        if not isinstance(self.place_id, str) or not self.place_id:
            raise ValueError("Place ID must be valid.")

        if not isinstance(self.user_id, str) or not self.user_id:
            raise ValueError("User ID must be valid.")

