import spacy

# Load English NLP model
nlp = spacy.load("en_core_web_sm")

# User input – simulating a chatbot-style prompt
text = input("Hi Adithya! What did you work on today and for how many hours? ")

# Process the input text
doc = nlp(text)

# Initialize project and hours
project = None
hours = None

# Extract hours and project name intelligently
for token in doc:
    if token.like_num:
        hours = token.text

    # Project detection logic using POS and DEP
    if token.pos_ in ["NOUN", "PROPN"] and token.dep_ in ["dobj", "pobj", "attr"]:
        project = token.text

# Output
print("\n✅ Timesheet Entry Captured:")
print("📌 Project:", project if project else "Not Found")
print("⏱️ Hours  :", hours if hours else "Not Found")
