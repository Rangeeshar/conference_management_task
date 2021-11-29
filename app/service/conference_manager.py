"""
Service Layer for conference which contacts database and does serialization and other works
"""


from flask import Response
import json
from app.models.conference import Conference
from app.models.talk import Talk
from app.utils.helper_utils import check_overlap
from datetime import timedelta
from dateutil.parser import parse


def create_conference(request_data):
    conf_object = Conference(conference_data=request_data)
    conf_object.create()
    return Response(
        response=json.dumps(
            {
                "message": "conference added successfully",
                "data": conf_object.id,
                "success": True,
            }
        ),
        status=200,
        headers={"Content-Type": "application/json"},
    )


def modify_conference(confid_id, request_data):
    Conference().update(update_data=request_data)
    return Response(
        response=json.dumps(
            {
                "message": "conference modified successfully",
                "data": confid_id,
                "success": True,
            }
        ),
        status=200,
        headers={"Content-Type": "application/json"},
    )


def create_talk(talk_data):
    temp_start_time = parse(talk_data.get("datetime"))
    temp_end_time = temp_start_time + timedelta(hours=talk_data.get("duration"))
    talk_data["start_time"] = temp_start_time.strftime("%Y-%m-%dT%H:%M:%S")
    talk_data["end_time"] = temp_end_time.strftime("%Y-%m-%dT%H:%M:%S")
    return check_overlap_action(talk_data, action="create")


def modify_talk(talk_id, talk_data):
    if "datetime" in talk_data:
        talk_data["talk_id"] = talk_id
        talk_info = Talk().fetch(filters={"id": talk_id})
        talk_data["conference_id"] = talk_info[0].get("conference_id")
        print(talk_info)
        start_time = parse(talk_data.get("datetime"))
        end_time = start_time + timedelta(hours=talk_data.get("duration"))
        talk_data["start_time"] = start_time.strftime("%Y-%m-%dT%H:%M:%S")
        talk_data["end_time"] = end_time.strftime("%Y-%m-%dT%H:%M:%S")
        return check_overlap_action(talk_data, "update")
    else:
        Talk().update(update_data=talk_data, filter={"id": talk_id})
        return Response(
            response=json.dumps({"message": "update successfull", "success": True, "data": talk_id}),
            status=200,
            headers={"Content-Type": "application/json"},
        )


def check_overlap_action(data, action):
    conference_data = Conference().fetch(filters={"id": data.get("conference_id")})
    if conference_data:
        talks_data = Talk().fetch(filters={"conference_id": data.get("conference_id")})
        current_interval = [data.get("start_time"), data.get("end_time")]
        if check_overlap(
            current_interval,
            [
                {
                    "start_time": conference_data[0].get("start_date"),
                    "end_time": conference_data[0].get("end_date"),
                }
            ],
        ):
            if not check_overlap(current_interval, talks_data):
                if action == "create":
                    talk_object = Talk(data)
                    talk_object.create()
                    data, message, status = talk_object.id, "create success", 200
                elif action == "update":
                    talk_id = data.pop("talk_id", None)
                    Talk().update(update_data=data, filter={"id": talk_id})
                    data, message, status = talk_id, "update success", 200
                else:
                    data, message, status = None, "failed", 400
            else:
                data, message, status = (
                    None,
                    "slot already taken, try different one",
                    400,
                )
        else:
            data, message, status = (
                None,
                "not in range of conference start and end date",
                400,
            )
    else:
        data, message, status = None, "conference doesnt exist", 400

    if status != 200:
        return Response(
            response=json.dumps({"error": message, "success": False}),
            status=status,
            headers={"Content-Type": "application/json"},
        )
    else:
        return Response(
            response=json.dumps({"message": message, "success": True, "data": data}),
            status=status,
            headers={"Content-Type": "application/json"},
        )


def fetch_talk(_filter):
    return fetch_from_db(Talk, _filter)


def fetch_conference(_filter):
    return fetch_from_db(Conference, _filter)


def fetch_from_db(class_name, _filter):
    if _filter == "all":
        data = class_name().fetch()
    else:
        _f_dict = json.loads(_filter)
        data = class_name().fetch(filters=_f_dict)

    return Response(
        response=json.dumps(
            {"message": "fetch success", "data": data, "success": True}
        ),
        status=200,
        headers={"Content-Type": "application/json"},
    )
