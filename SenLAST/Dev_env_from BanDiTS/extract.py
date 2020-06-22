import os

directory = "C:/Users/jz199/Documents/Studium/Master/2. Semester/Vorlesungsmitschriften/GEO411 - Landschaftsmanagement und Fernerkundung/Sentinel 3 Daten Uni Jena/S3_Daten-20200622T143538Z-001/S3_Daten"
new_list = []
for filename in os.listdir(directory):
    if filename.endswith(".tif"):
        new_list.append(os.path.join(directory, filename))
    else:
        continue

print(new_list)