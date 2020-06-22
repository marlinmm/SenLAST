import os

directory = "C:/Users/jz199/Documents/Studium/Master/2. Semester/Vorlesungsmitschriften/GEO411 - Landschaftsmanagement und Fernerkundung/Sentinel 3 Daten Uni Jena/S3_Daten-20200622T143538Z-001/S3_Daten"
for filename in os.listdir(directory):
    if filename.endswith(".tif"):
        print(os.path.join(directory, filename))
    else:
        continue
