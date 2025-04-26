from pymongo import MongoClient

# Connect to MongoDB
def init_app(app=None):
    client = MongoClient("mongodb://localhost:27017/")
    db = client["timesheet_app"]
    return db
