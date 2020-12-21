import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


app = Flask(__name__)

#############################################################################

# export SECRET_KEY=mysecret

app.config['SECRET_KEY'] = 'mysecret'


### DATABASE SETUPS ############


basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
Migrate(app,db)



#### LOGIN CONFIGS #######


login_manager = LoginManager()


login_manager.init_app(app)


login_manager.login_view = "users.login"



#### BLUEPRINT CONFIGS #######


from ciceropage.core.views import core
from ciceropage.users.views import users
from ciceropage.tour_posts.views import tour_posts
from ciceropage.error_pages.handlers import error_pages


app.register_blueprint(users)
app.register_blueprint(tour_posts)
app.register_blueprint(core)
app.register_blueprint(error_pages)
