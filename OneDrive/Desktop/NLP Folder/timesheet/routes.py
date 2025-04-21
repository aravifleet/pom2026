from flask import Blueprint, request, jsonify, current_app
from nlp_engine.task_handler import add_timesheet, update_timesheet, delete_timesheet, view_timesheet

# Create the blueprint
timesheet_bp = Blueprint('timesheet', __name__)

# Route: /timesheet/add
@timesheet_bp.route('/add', methods=['POST'])
def add_entry():
    data = request.get_json()

    # Required fields from client
    name = data.get('name')
    emp_id = data.get('emp_id')
    tasks = data.get('tasks')
    total_hours = data.get('total_hours')
    reason = data.get('reason')
 
    mongo = current_app.mongo
    # Call to engine
    add_timesheet(name, emp_id, tasks, total_hours, reason, mongo)

    return jsonify({"message": "Timesheet entry added successfully!"}), 201


# Route: /timesheet/update
@timesheet_bp.route('/update', methods=['PUT'])
def update_entry():
    data = request.get_json()
    emp_id = data.get('emp_id')

    mongo = current_app.mongo

    update_timesheet(emp_id,mongo)

    return jsonify({"message": "Timesheet entry updated successfully!"}), 200


# Route: /timesheet/delete
@timesheet_bp.route('/delete', methods=['DELETE'])
def delete_entry():
    data = request.get_json()
    emp_id = data.get('emp_id')

    mongo = current_app.mongo

    delete_timesheet(emp_id,mongo)

    return jsonify({"message": "Timesheet entry deleted successfully!"}), 200


# Route: /timesheet/view?emp_id=EMP101
@timesheet_bp.route('/view', methods=['GET'])
def view_entry():
    emp_id = request.args.get('emp_id')  # from query param like /view?emp_id=EMP101
    mongo = current_app.mongo
    result = view_timesheet(emp_id,mongo)

    return jsonify(result), 200
