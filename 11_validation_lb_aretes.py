import head
import subprocess
cur=head.cur
con=head.con
os=head.os
#-------------------------------------------------------------------------------------
os.system("cls")#effacer l'ecran 
print("11_validation_lb_aretes")
print(100*"~")
# etiquette d une arete
cur.execute(
    "select etiquette, count(id) from aretes1 where fait='oui' limit 0 , 1")
ligne = cur.fetchone()
etiquette = ligne[0]
id_c = ligne[1]
if id_c ==0 :
    print("Verification terminer")
    cmd = "12_fin.py"
else:
    print(f"etiquette : {etiquette}")
    #les aretes1 dont etiquette = etiquette
    cur.execute(
        "select count(id) from aretes1 where etiquette=? limit 0 , 1",(etiquette,))
    ligne = cur.fetchone()
    etiquette_cnt1 = ligne[0]
    print(f"il y a  : {etiquette_cnt1} arretes avec etiquette {etiquette} dans aretes1")
    #les aretes2 dont etiquette = etiquette
    cur.execute(
        "select count(id) from aretes2 where etiquette=? limit 0 , 1",(etiquette,))
    ligne = cur.fetchone()
    etiquette_cnt2 = ligne[0]
    print(f"il y a  : {etiquette_cnt2} arretes avec etiquette {etiquette} dans aretes2")
    #comparaison
    if etiquette_cnt1==etiquette_cnt2:
        print("les nombres sont egals")
        #update fait = 'non'
        cur.execute("update aretes1 set fait='non' where etiquette=?", (etiquette,))
        con.commit()# Sauvgarde
        cmd = "11_validation_lb_aretes.py"
    else:
        print("les nombres ne sont pas egals")
        #update fait = 'non'
        cur.execute("update aretes1 set fait='non'")
        con.commit()# Sauvgarde
        # fait='oui' dans graphe2
        cur.execute("select sommets from arbre2 where niveau=0")
        ligne = cur.fetchone()
        sommet=ligne[0]
        cur.execute("update graphe2 set fait='oui' where sommet=?", (sommet,))
        con.commit()# Sauvgarde
        #vider les tableaux de graphe2    
        cur.execute("DELETE FROM arbre2")
        cur.execute("delete from sqlite_sequence where name='arbre2'")# pour id=1
        cur.execute("update aretes2 set fait='non', etiquette='-' ")
        cur.execute("DELETE FROM labels2")
        cur.execute("delete from sqlite_sequence where name='labels2'")# pour id=1
        con.commit()# Sauvgarde
        cmd = "07_arbres2.py"
print(cmd)
subprocess.call(["python", cmd])