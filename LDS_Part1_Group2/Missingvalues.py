# -*- coding: utf-8 -*-

import csv 

# Creo una funzione che calcoli il numero di missing values presenti in un file
def MissingValues (file):
    file_i = open(file+".csv") # apro il file 
    file_r=csv.reader(file_i) # leggo il file
    
    s=0 # inizializzo somma valori nulli
    for row in file_r: # analizzo ogni riga del file
        for i in range(len(row)): # analizzo ogni elemento della riga
            if row[i]=="": # se trovo un valore nullo incremento la somma
                s+=1
    print('Nel file',file,'ci sono', s, 'missing values.')
    file_i.close() #chiudo il file

#-----------------------------------------------------------------

# Eseguo la funzione su tutti i file del dataset
    
MissingValues('fact')
MissingValues('cpu')
MissingValues('gpu')
MissingValues('ram')
MissingValues('vendor')
MissingValues('time')
MissingValues('geography')
MissingValues('cpu_sales')
MissingValues('gpu_sales')
MissingValues('ram_sales')



