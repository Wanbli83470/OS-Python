# coding: utf-8
#!/usr/bin/python
# import
# 1 Récupérer les dossier

import os
import glob
import csv
aromazone = os.listdir("/Volumes/PAO-1/Clients/2168")
# 2) Récupérer tous les fichiers des sous dossiers :
files = []
for l in aromazone :
	try:
		file = os.listdir("/Volumes/PAO-1/Clients/2168/"+l)
		files.append(file)
	except:
		pass

# 3) Extraire les fichiers clients avec une condition au sein de nos dossiers :
saisie = input("Saisir le type : ")
files_pdf = []
dossiers = []
for a in files:
	for b in a :
		if ".PDF" in b:
			dossiers.append(a)
			files_pdf.append(b)
				
print("\n")
print("Nombre de refs clients : {0}".format(len(files_pdf)))
print(dossiers)
print("\n")
print(files_pdf)
print("\n")
# 4) Récupérer les fichiers à comparer
fichiers_clients = os.listdir("/Users/admin/Desktop/AROMAZONE")
print(fichiers_clients)
nb_modifs = 0

for compare in fichiers_clients :
	if compare in files_pdf :
		pass
	elif compare == ".DS_Store":
		pass
	else:
		print("modif:{0}".format(compare))
		nb_modifs += 1

print("nombre modifs = {}".format(nb_modifs))
# ftp = []
# ftp_clients = []
# for i in dossiers :
# 	for j in i :
# 		if "pdf" in j:
# 			print(j)
# 			ftp.append(j)
# 		elif "PDF" in j:
# 			print(j)
# 			ftp_clients.append(j)
# 		else:
# 			print("error")
# print(ftp)
# print(ftp_clients)	

# import csv


# with open('rapport.csv','w') as f:
#     writer = csv.writer(f)
#     writer.writerow( ('ftp') )
#     writer.writerow( ('Référence') )
#     for x in ftp:
#         writer.writerows(ftp)

#     for z in ftp_clients:
#         writer.writerows(ftp_clients)	