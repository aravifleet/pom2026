#from flask import Flask, jsonify
#from flask_pymongo import PyMongo
#from auth.routes import auth_bp  # Import auth blueprint
#from timesheet.routes import timesheet_bp  # Import timesheet blueprint

#app = Flask(__name__)

# Database Configuration
#app.config["MONGO_URI"] = "mongodb://localhost:27017/timesheetDB"
#mongo = PyMongo(app)

#app.mongo = mongo

# Registering Blueprints with URL prefixes
##app.register_blueprint(auth_bp, url_prefix='/auth')  # Auth building with /auth path
#app.register_blueprint(timesheet_bp, url_prefix='/timesheet')  # Timesheet building with /timesheet path

#@app.route('/')
#def home():
 #   return "Welcome to the User Management System!"  # Main reception area for general info

#if __name__ == '__main__':
  #  app.run(debug=True)
