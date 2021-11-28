from flask import Flask, request
from flask_restx import Resource, fields, Namespace
from app.service import conference_manager


conference_ns = Namespace("/v1/conference", description="Conference Management")

create_conference_model = conference_ns.model(
    "Conference Create",
    {
        "title": fields.String(required=True),
        "description": fields.String(required=True),
        "start_date": fields.DateTime(required=True),
        "end_date": fields.DateTime(required=True),
    },
)

modify_conference_model = conference_ns.model(
    "Conference Modify",
    {
        "title": fields.String(),
        "description": fields.String(),
        "start_date": fields.DateTime(),
        "end_date": fields.DateTime(),
    },
)

fetch_conference_model = conference_ns.model(
    "Conference_fetch",
    {
        "filter": fields.String()
    }
)

fetch_talk_model = conference_ns.model(
    "Talk fetch", {
        "filter": fields.String()
    }
)

create_talk_model = conference_ns.model(
    "Create Talk", {
        "title": fields.String(required=True),
        "description": fields.String(required=True),
        "duration": fields.Integer(required=True),
        "datetime": fields.DateTime(required=True),
        "speakers": fields.List(fields.String(required=True)),  
        "participants": fields.List(fields.String(required=True)),
    }
)

modify_talk_model = conference_ns.model(
    "Modify Talk", {
        "title": fields.String(),
        "description": fields.String(),
        "duration": fields.Integer(),
        "datetime": fields.DateTime(),
        "speakers": fields.List(fields.String()),  
        "participants": fields.List(fields.String()),
    }
)



@conference_ns.route("")
class ConferenceManager(Resource):
    @conference_ns.expect(create_conference_model, validate=False)
    def post(self):
        """Create a new conference"""
        data = request.get_json()
        return conference_manager.create_conference(data)

    @conference_ns.expect(fetch_conference_model)
    def get(self):
        """
        Filter conference
        """
        filter_data = request.args.get("filter")
        return conference_manager.fetch_conference(filter_data)


@conference_ns.route("/<int:conf_id>")
class ConferenceModify(Resource):
    @conference_ns.expect(modify_conference_model, validate=False)
    def put(self, conf_id):
        """
        Modify a conference
        """
        data = request.get_json()
        return conference_manager.modify_conference(conf_id, data)


@conference_ns.route("/talk")
class ConferenceTalk(Resource):
    @conference_ns.expect(create_talk_model)
    def post(self):
        """
        Add a talk into conference
        """
        talk_data = request.get_json()
        return conference_manager.create_talk(talk_data)

    @conference_ns.expect(fetch_talk_model)
    def get(self):
        """
        Filter talks in the conference
        """
        talk_filter = request.args.get("filter")
        return conference_manager.fetch_talk(talk_filter)


@conference_ns.route("/talk/<int:talk_id>")
class ConferenceTalkModifier(Resource):
    @conference_ns.expect(modify_talk_model)
    def put(self, talk_id):
        """
        Modify a talk
        """
        talk_data = request.get_json()
        return conference_manager.modify_talk(talk_id, talk_data)
