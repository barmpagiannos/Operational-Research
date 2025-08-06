# Εργασία Επιχειρησιακή Έρευνα
# Μπαρμπαγιάννος Βασίλειος
# ΑΕΜ: 10685

# 2η άσκηση.

import gurobipy as gp
from gurobipy import GRB
import numpy as np

# Ο πίνακας 2 της εργασίας.
kostos_metaforas = [
    [100, 80, 50, 50, 60, 100, 120, 90, 60, 70, 65, 110], # 1
    [120, 90, 60, 70, 65, 110, 140, 110, 80, 80, 75, 130], # 2
    [140, 110, 80, 80, 75, 130, 160, 125, 100, 100, 80, 150], # 3
    [160, 125, 100, 100, 80, 150, 190, 150, 130, float('inf'), float('inf'), float('inf')], # 4
    [190, 150, 130, float('inf'), float('inf'), float('inf'), 180, 150, 50, 50, 60, 100], # 5
    [200, 180, 150, float('inf'), float('inf'), float('inf'), 100, 120, 90, 60, 75, 110], # 6
    [120, 90, 60, 70, 65, 110, 140, 110, 80, 80, 75, 130], # 7
    [120, 90, 60, 70, 65, 110, 140, 110, 80, 80, 75, 130], # 8
    [140, 110, 80, 80, 75, 130, 160, 125, 100, 100, 80, 150], # 9
    [160, 125, 100, 100, 80, 150, 190, 150, 130, float('inf'), float('inf'), float('inf')], # 10
    [190, 150, 130, float('inf'), float('inf'), float('inf'), 200, 180, 150, float('inf'), float('inf'), float('inf')], # 11
    [200, 180, 150, float('inf'), float('inf'), float('inf'), 100, 80, 50, 50, 60, 100] # 12
]

# Ο πίνακας 3 της εργασίας.
pagia_kosth = [3500, 9000, 10000, 4000, 3000, 9000, 9000, 3000, 4000, 10000, 9000, 3500]
xwrhtikothtes = [300, 250, 100, 180, 275, 300, 200, 220, 270, 250, 230, 180]

# Ο πίνακας 4 της εργασίας.
zhthsh = [120, 80, 75, 100, 110, 100, 90, 60, 30, 150, 95, 120]

apothikes = len(pagia_kosth) # Αριθμός αποθηκών.
kentra = len(zhthsh) # Αριθμός κέντρων πώλησης.

# Υπολογισμός μοναδιαίου κόστους μεταφοράς ανά τόνο.
monadiaio_kostos = []
for i in range(apothikes):
    row = []
    for j in range(kentra):
        if kostos_metaforas[i][j] == float('inf'):
            row.append(float('inf'))
        else:
            row.append(kostos_metaforas[i][j] / zhthsh[j]) # Μοναδιαίο κόστος μεταφοράς.
    monadiaio_kostos.append(row)

model = gp.Model("αποθήκες") # Το μοντέλο μου.

# Δυαδικές μεταβλητές για τη λειτουργία της αποθήκης (δηλαδή αν θα ανοίξω αποθήκη ή όχι).
y = model.addVars(apothikes, vtype=GRB.BINARY, name="Open")

# Συνεχείς μεταβλητές για ποσότητες που παραδίδονται.
x = model.addVars(apothikes, kentra, lb=0.0, name="Ship")

# Η αντικειμενική συνάρτηση.
model.setObjective(
    gp.quicksum(pagia_kosth[i] * y[i] for i in range(apothikes)) +
    gp.quicksum(monadiaio_kostos[i][j] * x[i, j] for i in range(apothikes) for j in range(kentra) if monadiaio_kostos[i][j] < float('inf')),
    GRB.MINIMIZE
)

# Οι περιορισμοί της εκφώνησης.

# Κάθε πελάτης να εξυπηρετείται πλήρως, για όλη του τη ζήτηση.
for j in range(kentra):
    model.addConstr(gp.quicksum(x[i, j] for i in range(apothikes) if monadiaio_kostos[i][j] < float('inf')) == zhthsh[j], name=f"demand_{j}")

# Δεν πρέπει να ξεπερνιέται η χωρητικότητα κάθε αποθήκης.
for i in range(apothikes):
    model.addConstr(gp.quicksum(x[i, j] for j in range(kentra) if monadiaio_kostos[i][j] < float('inf')) <= xwrhtikothtes[i] * y[i], name=f"capacity_{i}")

# Επίλυση του μοντέλου.
model.optimize()

# Το αποτέλεσμα.
if model.status == GRB.OPTIMAL:
    print(f"\nΒέλτιστο συνολικό κόστος: {model.ObjVal:.2f} χιλ. ευρώ\n")
    print("Αποθήκες που θα λειτουργήσουν:")
    for i in range(apothikes):
        if y[i].X > 0.5:
            print(f"Αποθήκη {i + 1}")

    print("\nΤι μεταφέρεται από κάθε αποθήκη σε κάθε κέντρο (σε τόνους):")
    for i in range(apothikes):
        for j in range(kentra):
            if x[i, j].X > 1e-6:
                print(f"Από Αποθήκη {i+1} προς Κέντρο {j+1}: {x[i,j].X:.2f} τόνοι")

else:
    print("Δεν βρέθηκε βέλτιστη λύση.")
