#nlp_engine/task_handler.py

from flask import jsonify
from database import init_app

# Initialize the MongoDB instance
mongo = init_app(None)

def add_timesheet(name, emp_id, tasks, total_hours, reason, mongo):
    timesheet_data = {
        "name": name,
        "emp_id": emp_id,
        "tasks": tasks,
        "total_hours": total_hours,
        "reason": reason
    }
    mongo.db.timesheets.insert_one(timesheet_data)

def update_timesheet(emp_id, mongo):
    timesheet = mongo.db.timesheets.find_one({"emp_id": emp_id})
    if timesheet:
        # Perform your update logic here
        mongo.db.timesheets.update_one({"emp_id": emp_id}, {"$set": {"status": "updated"}})
    else:
        return jsonify({"message": "Timesheet not found!"}), 404

def delete_timesheet(emp_id, mongo):
    timesheet = mongo.db.timesheets.find_one({"emp_id": emp_id})
    if timesheet:
        mongo.db.timesheets.delete_one({"emp_id": emp_id})
        return jsonify({"message": "Timesheet deleted successfully!"}), 200
    else:
        return jsonify({"message": "Timesheet not found!"}), 404

def view_timesheet(emp_id, mongo):
    timesheet = mongo.db.timesheets.find_one({"emp_id": emp_id})
    if timesheet:
        return jsonify(timesheet), 200
    else:
        return jsonify({"message": "Timesheet not found!"}), 404
