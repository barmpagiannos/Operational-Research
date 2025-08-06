# Εργασία Επιχειρησιακή Έρευνα
# Μπαρμπαγιάννος Βασίλειος
# ΑΕΜ: 10685

# 1η άσκηση.

from gurobipy import *

# Τα δεδομένα της εκφώνησης.
kathigites=['Γεσμανίδης','Ινσουλίνα','Χαρτούλα','Λαθοπράξης','Αντιπαράγωγος','Κιρκοφίδου','Πλατιάζων','Μπρατσάκης','Τρεχαλητούλα']
mathimata=['Αγγλικά','Βιολογία','Ιστορία-Γεωγραφία','Μαθηματικά','Μαθηματικά','Φυσική','Φιλοσοφία','Φυσική Αγωγή','Φυσική Αγωγή']
tmhmata=['1','2']
hmeres=['Δευτέρα','Τρίτη','Τετάρτη','Πέμπτη','Παρασκευή']
zwnes=[1,2,3,4]

# Ώρες.
wres={
('Γεσμανίδης','1'):1,('Γεσμανίδης','2'):1,
('Ινσουλίνα','1'):3,('Ινσουλίνα','2'):3,
('Χαρτούλα','1'):2,('Χαρτούλα','2'):2,
('Λαθοπράξης','1'):0,('Λαθοπράξης','2'):4,
('Αντιπαράγωγος','1'):4,('Αντιπαράγωγος','2'):0,
('Κιρκοφίδου','1'):3,('Κιρκοφίδου','2'):3,
('Πλατιάζων','1'):1,('Πλατιάζων','2'):1,
('Μπρατσάκης','1'):1,('Μπρατσάκης','2'):0,
('Τρεχαλητούλα','1'):0,('Τρεχαλητούλα','2'):1}

model=Model("εβδομαδιαίο_πρόγραμμα") # Το μοντέλο μου.

x=model.addVars(kathigites,tmhmata,hmeres,zwnes,vtype=GRB.BINARY)

# Οι ώρες που διδάσκει ο κάθε καθηγητής δίνονται στον πίνακα 1 της εκφώνησης.
for t in kathigites:
 for c in tmhmata:
  model.addConstr(quicksum(x[t,c,d,s] for d in hmeres for s in zwnes)==wres[(t,c)])

# Ένας καθηγητής ανά ζώνη ανά τμήμα.
for c in tmhmata:
 for d in hmeres:
  for s in zwnes:
   model.addConstr(quicksum(x[t,c,d,s] for t in kathigites)<=1)

# Όχι πάνω από 1 τμήμα ανά καθηγητή σε ίδια ζώνη.
for t in kathigites:
 for d in hmeres:
  for s in zwnes:
   model.addConstr(quicksum(x[t,c,d,s] for c in tmhmata)<=1)

# Φυσική Αγωγή μόνο Πέμπτη 3-4.
for i,t in enumerate(kathigites):
 if mathimata[i]=='Φυσική Αγωγή':
  for d in hmeres:
   for s in zwnes:
    if not (d=='Πέμπτη' and s in [3,4]):
     for c in tmhmata:
      model.addConstr(x[t,c,d,s]==0)

# Δευτέρα 1η ζώνη κρατημένη.
for t in kathigites:
 for c in tmhmata:
  model.addConstr(x[t,c,'Δευτέρα',1]==0)

# Ο κ. Λαθοπράξης δεν διδάσκει Δευτέρα πρωί.
for s in [1,2]:
 for c in tmhmata:
  model.addConstr(x['Λαθοπράξης',c,'Δευτέρα',s]==0)

# Η κ. Ινσουλίνα δεν εργάζεται Τετάρτη.
for s in zwnes:
 for c in tmhmata:
  model.addConstr(x['Ινσουλίνα',c,'Τετάρτη',s]==0)

# Κάθε τμήμα το πολύ 1 δίωρο ανά μάθημα τη μέρα (προς αποφυγήν πλήξεως!).
for c in tmhmata:
 for d in hmeres:
  for subj in set(mathimata):
   model.addConstr(quicksum(x[t,c,d,s] for t in kathigites if mathimata[kathigites.index(t)]==subj for s in zwnes)<=1)

model.setObjective(0,GRB.MINIMIZE)
model.optimize()

if model.status==GRB.OPTIMAL:
 print("\nΠρόγραμμα")
 for d in hmeres:
  for s in zwnes:
   for c in tmhmata:
    for t in kathigites:
     if x[t,c,d,s].x>0.5:
      
      print(f"{c} | {d} ζώνη {s} -> {t}: {mathimata[kathigites.index(t)]}")
else:
 print("Δεν υπάρχει λύση.")
