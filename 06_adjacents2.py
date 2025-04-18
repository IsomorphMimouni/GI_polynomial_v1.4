import head
import subprocess
cur=head.cur
con=head.con
os=head.os

os.system("cls")#effacer l'ecran 
#fichier graphe2
print("03_adjacents2.py")
print(30*".")
lignedebut=head.lignedebut
set_graphe=set()
with open(head.myfichier2, 'r') as f:
	for ind, line in enumerate(f):
		if ind >= lignedebut-1:
			arete=line.split(' ')#explode php
			a=arete[1]
			b=arete[2]
			b=b.strip()
			a=int(a)
			b=int(b)
			set_graphe.add(a)
			set_graphe.add(b)
			#insert aretes
			cur.execute("INSERT INTO aretes2 (a, b, etiquette, fait) VALUES (?, ?, ?, ?)", (a, b, '-', 'non'))
# Sauvgarde
con.commit()
#print(set_graphe)
#------------------------------------------
i=1
list_graphe=list(set_graphe)
list_graphe.sort()
for k in list_graphe:
	# les adjacents avant de sommet k: b=k
	cur.execute("select a from aretes2 where b=?", (k,))
	avant = cur.fetchall()
	list_avant=list()
	for av in avant:
		str_av=str(av[0])
		list_avant.append(str_av)
	avant=','.join(list_avant)
	# les adjacents apres de sommet k: a=k
	cur.execute("select b from aretes2 where a=?", (k,))
	apres = cur.fetchall()
	list_apres=list()
	for ap in apres:
		str_ap=str(ap[0])
		list_apres.append(str_ap)
	apres=','.join(list_apres)
	adj=avant+","+apres
	adj=adj.strip(",")
	k=int(k)
	print(k,":",adj)
	cur.execute("insert into graphe2 (sommet, adjacents) values (?, ?)", (k, adj))
	i=i+1
# Sauvgarde
con.commit()
# Sauvgarde acomplit
con.commit()
con.close()#fermer data base
#-------------------------------------------------------------------------------------
# passer a 07_arbres2.py
cmd = '07_arbres2.py'
print(cmd)
subprocess.call(["python", cmd])