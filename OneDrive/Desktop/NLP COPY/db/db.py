from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Database and Collections
db = client["timesheet_app"]
users_collection = db["users"]
timesheets_collection = db["timesheets"]
idle_logs_collection = db["idle_logs"]

def test_connection():
    print("Collections in DB:", db.list_collection_names())

if __name__ == "__main__":
    test_connection()
