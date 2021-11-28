from flask import Response
import json
from app.models.conference import Conference


def create_conference(request_data):
    conf_object = Conference(conference_data=request_data)
    conf_object.create()
    return Response(
        response=json.dumps({"message": "conference added successfully", "data": conf_object.id, "success": True}),
        status=200,
        headers={"Content-Type": "application/json"},
    )

def modify_conference(confid_id, request_data):
    Conference().update(update_data=request_data)
    return Response(
        response=json.dumps({"message": "conference modified successfully", "data": confid_id, "success": True}),
        status=200,
        headers={"Content-Type": "application/json"},
    )

def fetch_conference(_filter):
    if _filter == "all":
        data = Conference().fetch()
    
    return Response(
        response=json.dumps({"message": "conference modified successfully", "data": data, "success": True}),
        status=200,
        headers={"Content-Type": "application/json"},
    )