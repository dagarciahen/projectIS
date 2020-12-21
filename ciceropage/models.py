from ciceropage import db,login_manager
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):

    # Create a table in the db
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    profile_image = db.Column(db.String(20), nullable=False, default='default_profile.png')
    email = db.Column(db.String(64), unique=True, index=True)
    country = db.Column(db.String(64))
    city = db.Column(db.String(64))
    name =db.Column(db.String(64))
    family_name = db.Column(db.String(64))
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    language = db.Column(db.String(64))
    posts = db.relationship('TourPost', backref='author', lazy=True)
    login_type = db.Column(db.String(20))


    def __init__(self, email,country,city,name,family_name, username, password,language,login_type):
        self.email = email
        self.country = country
        self.city = city
        self.name = name
        self.family_name=family_name
        self.username = username
        self.language = language
        self.password_hash = generate_password_hash(password)
        self.login_type=db.Column(db.String(80))

    def check_password(self,password):

        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f"UserName: {self.username}"

class TourPost(db.Model):

    users = db.relationship(User)
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    title = db.Column(db.String(140), nullable=False)
    text = db.Column(db.Text, nullable=False)

    def __init__(self, title, text, user_id):
        self.title = title
        self.text = text
        self.user_id =user_id


    def __repr__(self):
        return f"Tour Id: {self.id} --- Date: {self.date} --- Title: {self.title}"
