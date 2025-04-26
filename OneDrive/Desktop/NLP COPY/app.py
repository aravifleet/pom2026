from flask import Flask, jsonify
from flask_pymongo import PyMongo

# Import blueprints from their respective departments
from auth.routes import auth_bp
from timesheet.routes import timesheet_bp

from flask import Flask, request, jsonify, render_template


app = Flask(__name__)

# 🎯 Database setup (Your MongoDB office server)
app.config["MONGO_URI"] = "mongodb://localhost:27017/timesheetDB"
mongo = PyMongo(app)

# Making MongoDB accessible to other modules
app.mongo = mongo

# 🛎️ Reception Area - For public greeting
@app.route('/')
def home():
    return "Welcome to the User Management System! Please proceed to /auth or /timesheet."

@app.route('/timesheet', methods=['POST'])
def timesheet_handler():
    data = request.get_json()
    name = data.get("name")
    task = data.get("task")
    hours = data.get("hours")

    print(f"Received timesheet: Name={name}, Task={task}, Hours={hours}")

    # Optional: Save this info to DB if needed
    return jsonify({"message": f"Timesheet saved for {name}, task: {task}, hours: {hours}"})


# 🧑‍💻 Auth building: Registration & Login are handled here
app.register_blueprint(auth_bp, url_prefix='/auth')

# 🗂️ Timesheet building: Add, View, Update, Delete timesheets
app.register_blueprint(timesheet_bp, url_prefix='/timesheet')

# 📡 Running the company server
if __name__ == '__main__':
    app.run(debug=True)
