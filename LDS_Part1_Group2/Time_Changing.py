
import csv
from calendar import weekday 

# apertura e lettura csv 
csvfile = open("time.csv", "r")
reader = csv.DictReader(csvfile)

# apertura del nuovo csv
time_new = open("time_new.csv", "w", newline='')
output = csv.writer(time_new)

# scrittura dell'header
header = ["time_code", "year", "month", "day", "week", "quarter", "day_of_week"]
output.writerow(header)
 
# utilizzo funzione weekday della libreria calendar: restituisce un numero da 0 (Monday) a 6 (Sunday)

day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


   
for row in reader:
    
    # calcolo del giorno 
    wd = day_names[weekday(int(row["year"]), int(row["month"]), int(row["day"]))]  
    
    # calcolo del quadrimestre in base al mese Q1(da 1 a 3), ... Q4(da 10 a 12)
    if int(row["month"]) < 4: 
        qt = "Q1"
        
    elif int(row["month"])< 7: 
        qt = "Q2"
    
    elif int(row["month"]) < 10:
        qt = "Q3"
    
    else:
        qt = "Q4"
    
    # salvataggio dei dati su una stringa e scrittura della nuova stringa
    newline = [row["time_code"], row["year"], row["month"], row["day"], row["week"], qt, wd]
    output.writerow(newline)
    
    
csvfile.close()
time_new.close()
    
    
    
        
        


        
        
        
        
        
        
        
        
