"""
Server Running and Serving file
"""

from flask_restx import Api
from app.controllers.conference import conference_ns
from app.models.conference import Conference
from app.models.talk import Talk
from factory import create_app

app = create_app()
api = Api(
    app,
    version="1.0",
    title="Conference API",
    description="A simple Conference Management API",
)
api.add_namespace(conference_ns)

if __name__ == "__main__":
    app.run(debug=True)
