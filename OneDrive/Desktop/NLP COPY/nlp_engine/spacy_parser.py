#nlp_engine/spacy.parser.py

import spacy
from spacy import displacy
from datetime import datetime

# Load the spaCy model (You can download the model using `python -m spacy download en_core_web_sm`)
nlp = spacy.load("en_core_web_sm")

# Function to extract date from the sentence
def extract_date(text):
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "DATE":
            return ent.text
    return None

# Function to extract tasks and hours from the sentence
def extract_task_and_hours(text):
    doc = nlp(text)
    tasks = []
    hours = None
    for ent in doc.ents:
        if ent.label_ == "TIME":
            hours = ent.text
        elif ent.label_ == "ORG" or ent.label_ == "WORK_OF_ART":
            tasks.append(ent.text)
    return tasks, hours

# Function to process the timesheet request (add, update, delete)
def process_timesheet_request(text):
    # Example use of NLP to analyze the text
    doc = nlp(text)
    
    # Extract entities (e.g., date, task, hours)
    date = extract_date(text)
    tasks, hours = extract_task_and_hours(text)
    
    # Example: Extracting person's name (if the sentence includes a name entity)
    name = None
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            name = ent.text

    # Return the extracted details
    return {
        "name": name,
        "tasks": tasks,
        "hours": hours,
        "date": date or datetime.now().strftime("%Y-%m-%d")  # Default to today's date if no date found
    }

# Example function that could be used to analyze user input and create a timesheet entry
def analyze_timesheet_input(text):
    data = process_timesheet_request(text)
    # Here you could use the data to add a timesheet entry
    # For example: add_timesheet(data['name'], data['tasks'], data['hours'], data['date'])
    
    return data  # Returning the data just for demonstration
