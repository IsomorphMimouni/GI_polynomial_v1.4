# -*- coding:utf-8 -*-
import head
import subprocess

cur = head.cur
con = head.con
os = head.os

print("12_fin")
print("~" * 30)

# update 
cur.execute("update labels1 set fait='oui'")
con.commit()# Sauvgarde




# Vérifier l'état final
cur.execute("SELECT COUNT(id) FROM graphe2 WHERE fait='non'")
cnt_fait = cur.fetchone()[0]

if cnt_fait == 0:
	print("❌ Les deux graphes ne sont pas isomorphes.")
else:
	print("✅ Les deux graphes sont isomorphes.")
	# multiples solutions
	cur.execute("SELECT sommet FROM graphe1")
	sommets1 = cur.fetchall()
	fichier_solutions = "solutions.txt"
	with open(fichier_solutions, "w", encoding="utf-8") as f:
		for sommet in sommets1:
			sommet_1 = sommet[0]
			# Récupérer son étiquette dans labels1
			cur.execute("SELECT etiquette FROM labels1 WHERE sommet=?", (sommet_1,))
			etiquette1 = cur.fetchone()[0]
			# Rechercher les sommets de labels2 ayant la même étiquette
			cur.execute("SELECT sommet FROM labels2 WHERE etiquette=?", (etiquette1,))
			sommets_2 = [str(row[0]) for row in cur.fetchall()]
			ligne_txt = f"{sommet_1} : {', '.join(sommets_2)}\n"
			#print(ligne_txt.strip())
			f.write(ligne_txt)
	print(f"📄 Résultats enregistrés dans : {fichier_solutions}")
	# solution unique pour chaque sommet
	fichier_solution = "solution.txt"
	with open(fichier_solution, "a", encoding="utf-8") as f2:
		etat = True
		while etat:
			cur.execute("SELECT etiquette, count(id) FROM labels1 WHERE fait='oui' limit 0, 1")
			ligne = cur.fetchone()
			etiquette1 = ligne[0]
			cnt_etiquette = ligne[1]
			if cnt_etiquette ==0:
				break
			print(f"etiquette1:{etiquette1}({cnt_etiquette})")
			#graphe1
			cur.execute("SELECT sommet FROM labels1 WHERE etiquette=?",(etiquette1,))
			sommets1 = cur.fetchall()
			list_1 = list()
			for smt1 in sommets1:
				list_1.append(smt1[0])
			print(list_1)
			#graphe2
			cur.execute("SELECT sommet FROM labels2 WHERE etiquette=?",(etiquette1,))
			sommets2 = cur.fetchall()
			list_2 = list()
			for smt2 in sommets2:
				list_2.append(smt2[0])
			print(list_2)
			for k in range(len(list_1)):
				print(f"{list_1[k]}:{list_2[k]}")
				f2.write(f"{list_1[k]}:{list_2[k]}\n")
			print(10*"-")
			#update fait = 'non'
			cur.execute("update labels1 set fait='non' where etiquette=?", (etiquette1,))
			con.commit()# Sauvgarde
			print(f"📄 Résultats enregistrés dans : {fichier_solution}")
con.close()