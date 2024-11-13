from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_graphql import GraphQLView
from .schema import schema

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_envvar('DATABASE_URL', silent=True)
    db.init_app(app)

    app.add_url_rule(
        '/graphql', 
        view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True)
    )

    return app
