import csv

with open("text.csv","w") as file:
    writer = csv.writer(file)
    writer.writerow(["Qno","Question Text","Option 1","Option 2","Option 3","Option 4","Error if any","Answer Key","Solution"])
    
    