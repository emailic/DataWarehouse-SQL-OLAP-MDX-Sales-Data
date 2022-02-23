# -*- coding: utf-8 -*-
import csv

# Creo una funzione per scrivere l'header di ogni file
def header(tipowriter, tipo):
    #Scrivo l'header
    tipowriter.writerow([tipo+'_code']+['time_code']+['geo_code']+['vendor_code']+['sales_usd']+['sales_currency'])

#Creo funzione che calcola il numero di righe del file
def LengthFile(file):
    file_i=open(file+".csv",'r') #apro in lettura
    lines=file_i.readlines() #leggo le righe
    return len(lines)-1 #ritorno il numero di righe (eliminando l'header)
    file_i.close() # chiudo il file
#----------------------------------------------------------------

# Apro in lettura il csv origine
factfile = open("fact.csv")
fact_f=csv.DictReader(factfile)

# Apro in scrittura i csv che voglio in output
cpufile= open("cpu_sales.csv",'w',newline="")
cpu_writer = csv.writer(cpufile)
# Scrivo l'header
header(cpu_writer, 'cpu')

gpufile= open("gpu_sales.csv",'w',newline="")
gpu_writer = csv.writer(gpufile)
# Scrivo l'header
header(gpu_writer, 'gpu')

ramfile= open("ram_sales.csv",'w',newline="")
ram_writer = csv.writer(ramfile)
# Scrivo l'header
header(ram_writer, 'ram')

# Divido i csv verificando dove l'attributo x_code è non nullo(con x=cpu,gpu,ram)
for row in fact_f:
    if row['cpu_code']!="":
        cpu_writer.writerow([row['cpu_code']]+[row['time_code']]+[row['geo_code']]+[row['vendor_code']]+[row['sales_uds']]+[row['sales_currency']])
    elif row['gpu_code']!="":
        gpu_writer.writerow([row['gpu_code']]+[row['time_code']]+[row['geo_code']]+[row['vendor_code']]+[row['sales_uds']]+[row['sales_currency']])
    elif row['ram_code']!="":
        ram_writer.writerow([row['ram_code']]+[row['time_code']]+[row['geo_code']]+[row['vendor_code']]+[row['sales_uds']]+[row['sales_currency']])

# Chiudo i file aperti
cpufile.close()
gpufile.close()
ramfile.close()
factfile.close()

# Controllo che il numero di righe dei 3 file creati sia uguale a quello di fact
fact_l=LengthFile ('fact')
cpu_l=LengthFile('cpu_sales')
gpu_l=LengthFile('gpu_sales')
ram_l=LengthFile('ram_sales')

if fact_l !=(cpu_l+gpu_l+ram_l): 
    print('Errore numero di righe')
