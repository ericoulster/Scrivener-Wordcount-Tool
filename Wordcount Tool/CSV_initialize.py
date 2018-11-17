import csv

colnames = [str('Date'), str('Wordcount')]

with open('wordcount_records.csv', 'w', encoding='cp1252') as file:
    filewriter = csv.writer(file)
    filewriter.writerow(colnames)
