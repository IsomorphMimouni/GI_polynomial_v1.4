import head
import subprocess
cur=head.cur
con=head.con
os=head.os

os.system("cls")#effacer l'ecran 
#-------------------------------------------------------------------------------------
print("08_avant_label2")
print(100*"~")
#-------------------------------------------------------------------------------------
#sommet et adjacents de graphe2:
cur.execute("select sommet from graphe2 where fait='non' limit 0 , 1")
ligne = cur.fetchone()
sommet=ligne[0]
#comparer les deux arbres:
#arbre2
cur.execute("select sommets from arbre2")
ligne = cur.fetchall()
list2=[]
for t in ligne:
	sommets=t[0]
	#print(sommets)
	list_sommets=sommets.split(',')
	t2=len(list_sommets)
	list2.append(t2)
#recuperer les tetes de graphe1 dont les max sont egaux avec max niveau de graphe2
fichier = open("tetes.txt", "r")
a=fichier.readline()
fichier.close()
list_a=a.split(',')
#arbre1
etat=False
for a_l in list_a:
	cur.execute("select sommets from arbre1 where tete=?", (a_l,))
	ligne = cur.fetchall()
	list1=[]
	for t in ligne:
		sommets=t[0]
		#print(sommets)
		list_sommets=sommets.split(',')
		t1=len(list_sommets)
		list1.append(t1)
	if (list1==list2):
		etat=True
		break
if (etat):
	print("les deux lists sont egaux")
	print("aller calculer les etiquettes ou labels!!!")
	# passer a 09_label2.py
	cmd = '09_label2.py'
else:
	print("les deux lists sont deferent")
	#tete2
	cur.execute("select sommets from arbre2 where niveau=0")
	ligne = cur.fetchone()
	sommet=ligne[0]
	#delete arbre2
	cur.execute("DELETE FROM arbre2")
	cur.execute("delete from sqlite_sequence where name='arbre2'")# pour id=1
	#fait='oui' dans graphe2
	cur.execute("update graphe2 set fait='oui' where sommet=?", (sommet,))
	con.commit()# Sauvgarde
	cur.execute("select count(id) from graphe2 where fait='non'")
	ligne = cur.fetchone()
	cnt=ligne[0]
	if(cnt==0):
		cmd = '12_fin.py'
	else:
		# passer a 07_arbres2.py
		cmd = '07_arbres2.py'
con.close()#fermer data base
print(cmd)
subprocess.call(["python", cmd])