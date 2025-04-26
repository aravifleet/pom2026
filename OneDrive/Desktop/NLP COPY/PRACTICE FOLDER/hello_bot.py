import spacy

nlp = spacy.load("en_core_web_sm")

text = input("Can you explain your task for the day : ")

doc = nlp(text)

project = None
hours = None

for token in doc:
    if token.like_num:
        hours = token.text
    if token.pos_ in ["NOUN", "PROPN"] and token.dep_ in ["dobj", "pobj", "attr"]:
        project = token.text

print("project" , project)
print("hours", hours)
      
