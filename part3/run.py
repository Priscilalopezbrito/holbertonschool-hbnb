#!/usr/bin/python3
from part3.hbnb.app import create_app, db

app = create_app()
with app.app_context():
    db.create_all()

if __name__ == '__main__':

    app.run(debug=True, host='0.0.0.0', port=5050)
