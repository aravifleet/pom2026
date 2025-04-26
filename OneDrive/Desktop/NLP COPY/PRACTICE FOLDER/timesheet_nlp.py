import spacy

# Load English NLP model
nlp = spacy.load("en_core_web_sm")

# User input – simulating a chatbot-style prompt
text1 = input("Hi user can u enter your Name : ")
text2 = input("can u confirm your Employee ID: ?")
text = input(f"Hi {text1} ! What did you work on today and for how many hours? ")



# Process the input text
doc = nlp(text)

# Initialize fields
project = None
hours = None
ticketnumber = None





# Extract hours, project, and ticket number
for token in doc:
    if token.like_num:
        hours = token.text

    if token.pos_ in ["NOUN", "PROPN"] and token.dep_ in ["dobj", "pobj", "attr"]:
        if not project:
            project = token.text
        elif not ticketnumber:
            ticketnumber = token.text

if int (hours) < 8 :
    chatter = input("Could you please confirm, why the hours is less than 8 hours ?")
    print(f"📝 Noted reason for lesser hours: {chatter}")
else:
    print("Nicely done for the day")


# Output
print("\n✅ Timesheet Entry Captured:")
print("📌 Project:", project if project else "Not Found")
print("⏱️ Hours  :", hours if hours else "Not Found")
print("🎫 Ticket Number:", ticketnumber if ticketnumber else "Not Found")
