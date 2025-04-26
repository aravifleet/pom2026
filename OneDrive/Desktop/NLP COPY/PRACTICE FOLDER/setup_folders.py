import os

#We are creating different folders
folders = ['auth', 'core', 'db', 'nlp_engine', 'ui', 'notifications']

#We are creating directories
for folder in folders:
    if not os.path.exists(folder):
        os.makedirs(folder)
        print(f"Created folder: {folder}")
    else:
        print(f"Folder {folder} already exists.")
