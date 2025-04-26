import spacy
from datetime import datetime   

# Load English NLP model
nlp = spacy.load("en_core_web_sm")

# Store tasks
tasks = []
total_hours = 0

now = datetime.now()
formatted_datetime = now.strftime("%Y-%m-%d %H:%M:%S")

# Collect user info
name = input("Hi user! Please enter your Name: ")
emp_id = input("Can you confirm your Employee ID: ")

# Keep asking until total hours >= 8 or user aborts
while total_hours < 8:
    text = input(f"Hi {name}! What did you work on today and for how many hours? ")
    doc = nlp(text)

    project = None
    ticketnumber = None
    hours = 0

    for token in doc:
        if token.like_num:
            hours = int(token.text)
        if token.pos_ in ["NOUN", "PROPN"] and token.dep_ in ["dobj", "pobj", "attr"]:
            if not project:
                project = token.text
            elif not ticketnumber:
                ticketnumber = token.text

    tasks.append((project, ticketnumber, hours))
    total_hours += hours

    if total_hours < 8:
        cont = input(f"🕒 Total is {total_hours} hours. Do you have more tasks to add? (yes/no): ").lower()
        if cont != "yes":
            break

# If still less than 8, ask reason
if total_hours < 8:
    reason = input("🧐 You've logged less than 8 hours. Can you confirm the reason? ")
    print(f"📝 Reason noted: {reason}")

# Final Output
print("\n✅ Timesheet Summary:")
print(f"👤 Name: {name}, 🆔 Employee ID: {emp_id}")
for i, task in enumerate(tasks, 1):
    print(f"🔹 Task {i}: Project: {task[0]}, Ticket: {task[1]}, Hours: {task[2]}")
print(f"📊 Total Hours Worked: {total_hours}")
print("📅 Timesheet recorded on:", formatted_datetime)
