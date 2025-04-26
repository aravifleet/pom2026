import spacy

# Load the English language model
nlp = spacy.load("en_core_web_sm")

# Your text
text = "Fleet Studio is based in Chennai and specializes in mobile apps."

# Process the text
doc = nlp(text)

# Print each word and its part of speech
for token in doc:
    print(token.text, token.pos_, token.dep_)
