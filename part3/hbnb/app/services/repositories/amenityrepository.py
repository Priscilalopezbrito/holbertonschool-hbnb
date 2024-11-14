from part3.hbnb.app.models.amenity import Amenity
from part3.hbnb.app.persistence.sqlalchemyrepository import SQLAlchemyRepository
from part3.hbnb.app import db


class AmenityRepository(SQLAlchemyRepository):
    def __init__(self):
        super().__init__(Amenity)
