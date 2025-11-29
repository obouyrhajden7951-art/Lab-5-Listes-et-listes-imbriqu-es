# mini_projet_simple.py

# --- Classe initiale ---
classe = [
    ["Alice", 20, 15.5],
    ["Bob", 19, 12.0],
    ["Charlie", 22, 16.0]
]

# --- Fonctions simples ---
def afficher_classe(classe):
    if not classe:
        print("La classe est vide.")
        return
    for i, etudiant in enumerate(classe, start=1):
        print(f"{i}. {etudiant[0]} — {etudiant[1]} ans — note {etudiant[2]}")

def ajouter_etudiant(classe):
    nom = input("Nom : ").strip()
    try:
        age = int(input("Âge : "))
        note = float(input("Note : "))
    except ValueError:
        print("Saisie invalide.")
        return
    classe.append([nom, age, note])
    print(f"{nom} ajouté.")

def supprimer_etudiant(classe):
    if not classe:
        print("Rien à supprimer.")
        return
    try:
        index = int(input("Numéro à supprimer : ")) - 1
        etudiant = classe.pop(index)
        print(f"{etudiant[0]} supprimé.")
    except (ValueError, IndexError):
        print("Index invalide.")

def modifier_etudiant(classe):
    if not classe:
        print("Classe vide.")
        return
    try:
        index = int(input("Numéro à modifier : ")) - 1
        etudiant = classe[index]
    except (ValueError, IndexError):
        print("Index invalide.")
        return

    nouveau_nom = input(f"Nouveau nom ({etudiant[0]}) : ").strip()
    if nouveau_nom:
        etudiant[0] = nouveau_nom

    age_str = input(f"Nouvel âge ({etudiant[1]}) : ").strip()
    if age_str:
        try:
            etudiant[1] = int(age_str)
        except ValueError:
            print("Âge ignoré.")

    note_str = input(f"Nouvelle note ({etudiant[2]}) : ").strip()
    if note_str:
        try:
            etudiant[2] = float(note_str)
        except ValueError:
            print("Note ignorée.")

def statistiques(classe):
    if not classe:
        print("Pas de données.")
        return
    notes = [e[2] for e in classe]
    moyenne = sum(notes)/len(notes)
    meilleure = max(classe, key=lambda e: e[2])
    pire = min(classe, key=lambda e: e[2])
    print(f"Moyenne : {moyenne:.2f}")
    print(f"Meilleure note : {meilleure[2]} ({meilleure[0]})")
    print(f"Plus faible note : {pire[2]} ({pir
