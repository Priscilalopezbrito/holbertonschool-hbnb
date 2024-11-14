from part3.hbnb.app.models.review import Review
from part3.hbnb.app.persistence.sqlalchemyrepository import SQLAlchemyRepository
from part3.hbnb.app import db


class ReviewRepository(SQLAlchemyRepository):
    def __init__(self):
        super().__init__(Review)
