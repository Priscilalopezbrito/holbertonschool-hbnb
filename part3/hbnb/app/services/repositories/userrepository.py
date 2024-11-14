from part3.hbnb.app.models.user import User
from part3.hbnb.app import db
from part3.hbnb.app.persistence.sqlalchemyrepository import SQLAlchemyRepository


class UserRepository(SQLAlchemyRepository):
    def __init__(self):
        super().__init__(User)

    def get_user_by_email(self, email):
        return self.model.query.filter_by(email=email).first()
