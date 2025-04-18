import head
import subprocess
cur = head.cur
con = head.con
os = head.os

os.system("cls")#effacer l'ecran 
print("05_labels_aretes1")
print(100 * "~")

# قراءة جميع etiquettes من labels1 في قاموس
cur.execute("SELECT id, etiquette FROM labels1")
labels_dict = dict(cur.fetchall())

# قراءة جميع adjacents من graphe1 في قاموس
cur.execute("SELECT id, adjacents FROM graphe1")
adjacents_dict = dict(cur.fetchall())

# الحصول على أول a حيث fait='non'
cur.execute("SELECT a FROM aretes1 WHERE fait='non' LIMIT 1")
ligne = cur.fetchone()
a = ligne[0]
print("a:", a)

# الحصول على etiquette الخاصة بـ a من القاموس
labels1_a = labels_dict[a]

# الحصول على قائمة المجاورين من القاموس
adj = adjacents_dict[a]
list_adj = adj.split(',')

# جمع التحديثات هنا
updates = []

for i in list_adj:
    i = int(i)  # التأكد من أن i عدد صحيح
    labels1_i = labels_dict[i]
    print(f"{i}:{labels1_i}")
    etiquette_ab = labels1_a + "|" + labels1_i
    updates.append((etiquette_ab, a, i))

# تحديث دفعة واحدة
cur.executemany("UPDATE aretes1 SET etiquette=?, fait='oui' WHERE a=? AND b=?", updates)
con.commit()

# التحقق من الباقي
cur.execute("SELECT COUNT(id) FROM aretes1 WHERE fait='non'")
cnt = cur.fetchone()[0]
print("cnt:", cnt)

if cnt ==0:
    cmd = '06_adjacents2.py'
else:
    cmd = '05_labels_aretes1.py'
print(cmd)
subprocess.call(["python", cmd])