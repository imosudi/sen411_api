from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_graphql import GraphQLView

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_envvar('DATABASE_URL', silent=True)
    
    # Initialize database
    db.init_app(app)
    
    # Import schema here to avoid circular import issues
    from .schema import schema
    
    # Set up GraphQL endpoint
    app.add_url_rule(
        '/graphql', 
        view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True)
    )

    return app
