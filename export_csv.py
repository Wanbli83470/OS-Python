import csv

en_tetes = ['Symbol','Prix','Date','Heure','Change','Vol']
lignes = [('AB', 30, '6/2/2018', '8:11am', -0.28, 15500),
        ('KJL', 55, '6/2/2018', '8:11am', -0.95, 445500),
        ('MMP', 88, '6/2/2018', '8:11am', -0.26, 966000),
       ]

with open('rapport.csv','w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow( ('ftp', 'Référence') )
    for x in lignes:
        writer.writerow(x)