"""
Step 1: Create Database & Model
Create a Flask and Flask-SQLAlchemy project, “adopt”.

Create a single model, Pet. This models a pet potentially available for adoption:

id: auto-incrementing integer
name: text, required
species: text, required
photo_url: text, optional
age: integer, optional
notes: text, optional
available: true/false, required, should default to available
While setting up the project, add the Debug Toolbar.
"""
from flask_sqlalchemy import SQLAlchemy

GENERIC_IMAGE = "https://www.google.com/search?q=dog+gifs&sxsrf=ALeKk01K6VzP7WC2tgnFIqrXR0NsqHitFA:1612544479656&tbm=isch&source=iu&ictx=1&fir=e8s4N24_h9yrHM%252Cr_3HjVfs1CXquM%252C_&vet=1&usg=AI4_-kQGhMTG2qGx1UcJhS4Iby7pU_bsFg&sa=X&ved=2ahUKEwiTupOnnNPuAhXKVzABHW5GBa8Q9QF6BAgMEAE#imgrc=e8s4N24_h9yrHM"
db = SQLAlchemy()

class Pet(db.Model):
    """Adoptable pet"""
    __tablename__ = "pets"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)

    def image_url(self):
        "Return image for pet -- bespoke or generic"
        return self.photo_url or GENERIC_IMAGE


def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    db.app = app
    db.init_app(app)
    

    