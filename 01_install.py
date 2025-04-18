import head
import subprocess
cur=head.cur
con=head.con
os=head.os

os.system("cls")#effacer l'ecran 
# tables 
#-------------------------------------------------------------------------------------
#table aretes1
cur.execute("""
CREATE TABLE IF NOT EXISTS aretes1 (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	a INTEGER NOT NULL,
	b INTEGER NOT NULL,
	etiquette TEXT DEFAULT '-',
	fait TEXT DEFAULT 'non'
)
""")
#-------------------------------------------------------------------------------------
#table aretes2
cur.execute("""
CREATE TABLE IF NOT EXISTS aretes2 (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	a INTEGER NOT NULL,
	b INTEGER NOT NULL,
	etiquette TEXT DEFAULT '-',
	fait TEXT DEFAULT 'non'
)
""")
#-------------------------------------------------------------------------------------
#table graphe1
cur.execute("""
CREATE TABLE IF NOT EXISTS graphe1 (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	sommet INTEGER NOT NULL,
	adjacents TEXT NOT NULL
)
""")
#-------------------------------------------------------------------------------------
#table graphe2
cur.execute("""
CREATE TABLE IF NOT EXISTS graphe2 (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	sommet INTEGER NOT NULL,
	adjacents TEXT NOT NULL,
	fait TEXT DEFAULT 'non'
)
""")
#-------------------------------------------------------------------------------------
#table arbre1
cur.execute("""
CREATE TABLE IF NOT EXISTS arbre1 (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	niveau INTEGER NOT NULL,
	sommets TEXT NOT NULL,
	tete INTEGER NOT NULL,
	fait TEXT DEFAULT 'non'
)
""")
#-------------------------------------------------------------------------------------
#table arbre2
cur.execute("""
CREATE TABLE IF NOT EXISTS arbre2 (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	niveau INTEGER NOT NULL,
	sommets TEXT NOT NULL,
	tete INTEGER NOT NULL,
	fait TEXT DEFAULT 'non'
)
""")
#-------------------------------------------------------------------------------------
#table labels1
cur.execute("""
CREATE TABLE IF NOT EXISTS labels1 (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	sommet INTEGER NOT NULL,
	etiquette TEXT NOT NULL,
	fait TEXT DEFAULT 'non'
)
""")
#-------------------------------------------------------------------------------------
#table labels2
cur.execute("""
CREATE TABLE IF NOT EXISTS labels2 (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	sommet INTEGER NOT NULL,
	etiquette TEXT NOT NULL,
	fait TEXT DEFAULT 'non'
)
""")
#-------------------------------------------------------------------------------------
#table solutions
cur.execute("""
CREATE TABLE IF NOT EXISTS solutions (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	sommet INTEGER NOT NULL,
	image INTEGER NOT NULL,
	images TEXT NOT NULL,
	tete INTEGER NOT NULL
)
""")
#-------------------------------------------------------------------------------------
con.commit()
con.close()#fermer data base
#-------------------------------------------------------------------------------------
cmd = '02_adjacents1.py'
print(cmd)
subprocess.call(["python", cmd])