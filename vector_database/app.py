from flask import Flask
from flask_restful import Api
from weaviatedb import VectorDatabase

# Initialize the Flask app and API
app = Flask(__name__)
api = Api(app)

# Add the resource to the API
api.add_resource(VectorDatabase, '/retriver')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)