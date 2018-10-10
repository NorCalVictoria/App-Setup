"""time crunch database model."""

from flask_sqlalchemy import SQLAlchemy
#import 



db = SQLAlchemy()


#----------------------------------------------------------------------#
# defs for model

class User(db.Model):
    """User of time crunch web app."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String(20), nullable=True)
    password = db.Column(db.String(20), nullable=True)
    fname = db.Column(db.String(20), nullable=True)
    lname = db.Column(db.String(20), nullable=True)
    pets = db.Column(db.String(5), nullable=True)
    kids = db.Column(db.String(5), nullable=True)

    def __repr__(self):
        """providing suggestion for free time"""

        return "<User user_id=%s email=%s>" % (self.user_id, self.email)
# list of hobbies here.


class Hobby(db.Model):
    """Hobbies that user chooses from"""
    __tablename__ = "hobbies"

    hobby_id = db.Column(db.Integer, primary_key=True)
    kid_friendly = db.Column(db.Boolean, nullable=False)
    pets_friendly = db.Column(db.Boolean, nullable=False)


class User_Hobby(db.Model):
    """choices user input when signed up"""
    __tablename__ = "user_hobbies"

    user_hobby_id= db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    #another?   = db.Column(db.String, nullable=False)

    def __repr__(self):
        """ add doc string """

        # return "<>" % ()

#-----------------------------------------------------------------------#
# Helper functions

def connect_to_db(app):
    """Connect the database."""

    # Configure PstgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///timeCrunch'
    db.app = app
    db.init_app(app)

if __name__ == "__main__":
  

    from server import app
    connect_to_db(app)
    print ("Connected to DB.")