from flask_graphql import GraphQLView

from app import app
from app.schema import schema

@app.route('/', methods=['GET'])
def home():
    
    return '<h1> <a href="/graphql"> API End-point </a> </h1>'
  
# Set up GraphQL endpoint
app.add_url_rule(
        '/graphql', 
        view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True)
    )