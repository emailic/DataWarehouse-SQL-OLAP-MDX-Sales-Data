import pyodbc 
import csv

# funzione di upload
def upload(file, table_name):
    
    # apertura dei file e lettura del header
    csvfile = open(file, "r")    
    header = csvfile.readline().replace("\n", "")
    print (header, "\n\n")
    lines = csv.reader(csvfile)
    
    # connessione al server
    server = 'tcp:apa.di.unipi.it' 
    database = 'Group2HWMart' 
    username = 'group2' 
    password = 'i1kgz' 
    connectionString = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password
    cnxn = pyodbc.connect(connectionString)
    cursor = cnxn.cursor()
    
    # conto del numero di colonne e creazione della stringa generica di ?
    n_of_columns = len(header.split(","))
    values = "?"+", ?"*(n_of_columns-1)
    
    sql ="INSERT INTO " + table_name + "(" + str(header) + ") VALUES(" + values + ")"

    print (sql) 
    
    header = header.split(",")
    
    # iterazione sulle linee del csv 
    for line in lines:
        
        # creazione della linea con il casting dei tipi (casting: funzione definita in riga 47) 
        newline = tuple(casting(header, line))  
        
        rows = cursor.execute(sql, newline)
        
    cnxn.commit()
    
    cursor.close()

    cnxn.close()

# funzione di casting per le variabili  
def casting (header, row):
    
    # lista delle posizioni dei code (position_code: funzione definita in riga 76)
    list_position = position_code(header)  
    
    newline = []   # creo la lista della nuova linea modificata per tipo 
    
    for i in range(len(header)):
            
        if i not in list_position:     # se non è attributo code allora si controlla
                
            if is_int(row[i]):                  # è intero? 
                  newline.append(int(row[i]))
                    
            elif is_float(row[i]):              # è float? 
                 newline.append(float(row[i]))
                
            else:                               # altrimenti rimane stringa
                newline.append(str(row[i]))
        
        else:      # se è codice allora si fa diventare stringa: problema nei codici, vedere report
            newline.append(str(int(float(row[i]))))
    
    print (newline, "\n")

    return newline    


# Creazione di una lista per identificare la posizione degli attributi code
def position_code(header):
    
    list_position = []
    
    for i,value in enumerate (header):
        if "code" in value:
            list_position.append(i)
    
    return list_position
            
# controllo del tipo: float o int
def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
    
def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
            
        
# ------------------------------- MAIN -----------------------------------

# esempio di esecuzione, uguale per tutte le tabelle
file = "time_new.csv"
name_table = "Time"
upload(file, name_table)
