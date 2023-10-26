from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Users\\Adrian12\\Desktop\\SchoollRossum\\banco\\aplication.sqlite3'
app.config['SECRET_KEY'] = 'senha_cripto'
db = SQLAlchemy(app)

from view import *

if __name__ == '__main__':
    app.run(debug=True)