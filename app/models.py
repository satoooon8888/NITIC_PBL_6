from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin
from flask_dance.consumer.storage.sqla import OAuthConsumerMixin


db = SQLAlchemy()


class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(256), unique=True)
    location_id = db.Column(db.Integer,db.ForeignKey('location.id'))

class Location(db.Model):
    __tablename__ = 'location'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    location = db.Column(db.String(100))

class OAuth(OAuthConsumerMixin, db.Model):
    __tablename__ = 'oauth'
    provider_user_id = db.Column(db.String(256), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship(User)


# setup login manager
login_manager = LoginManager()
login_manager.login_view = "google.login"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def get_teachers():
    return User.query.all()

def update_teacher_location(teacher, location_name):
    teacher.location = location_name
    db.session.commit()

def get_teacher_locations(teacher):
    return Location.query.filter(Location.user_id == teacher.id).all()

def lookup_location_by_id(location_id):
    location = Location.query.filter(Location.id == location_id).one()
    return location.location