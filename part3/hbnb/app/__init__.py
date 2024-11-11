#!/usr/bin/python3
from flask import Flask
from flask_restx import Api
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt() # To avoid circular dependency
from part3.hbnb.app.api.v1.users import api as users_ns
from part3.hbnb.app.api.v1.places import api as places_ns
from part3.hbnb.app.api.v1.amenities import api as amenities_ns
from part3.hbnb.app.api.v1.reviews import api as reviews_ns



def create_app(config_class="config.DevelopmentConfig"):
    app = Flask(__name__)
    app.config.from_object(config_class)

    api = Api(app, version='1.0', title='HBnB API', description='HBnB Application API')

    # Register the users namespace
    api.add_namespace(users_ns, path='/api/v1/users')
    api.add_namespace(places_ns, path='/api/v1/places')
    api.add_namespace(amenities_ns, path='/api/v1/amenities')
    api.add_namespace(reviews_ns, path='/api/v1/reviews')
    bcrypt.init_app(app)

    return app
