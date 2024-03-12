import os

path = ""
ends_with = ""
search = ""
replace = ""

for file in os.listdir(path):
    if file.endswith(ends_with):
        new_file = file.replace(search, replace)
        os.rename(os.path.join(path, file), os.path.join(path, new_file))
