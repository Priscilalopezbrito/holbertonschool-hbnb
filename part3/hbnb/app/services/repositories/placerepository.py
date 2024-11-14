from part3.hbnb.app.models.place import Place
from part3.hbnb.app.persistence.sqlalchemyrepository import SQLAlchemyRepository
from part3.hbnb.app import db


class PlaceRepository(SQLAlchemyRepository):
    def __init__(self):
        super().__init__(Place)
