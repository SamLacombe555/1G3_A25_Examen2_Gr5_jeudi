from debogage_mot_long import mot_plus_long, pourcentage_mots_max  # Remplacer par le nom de ton fichier

# ============================
# Tests pour mot_plus_long
# ============================
# Tests unitaires pour la fonction mot_plus_long (maximum 5 différents)
def test_mot_plus_long_1():
    animaux = ["chat", "chien", "éléphant", "souris", "hippopotame", 42, None, "oiseau"]
    resultat = mot_plus_long(animaux)

    assert resultat == "hippopotame"

def test_mot_plus_long_2():
    animaux = ["éléphant", "hippopotame", ""]
    resultat = mot_plus_long(animaux)

    assert resultat == "hippopotame"

def test_mot_plus_long_3():
    animaux = []
    resultat = mot_plus_long(animaux)

    assert resultat == None

def test_mot_plus_long_4():
    animaux = "chat"
    resultat = mot_plus_long(animaux)

    assert resultat == None

def test_mot_plus_long_5():
    animaux = [" chat ", "chien", "rat"]
    resultat = mot_plus_long(animaux)

    assert resultat == "chien"

#def test_pourcentage_mots_max_6():
# ============================
# Tests pour pourcentage_mots_max
# ============================
def test_pourcentage_mots_max_normal():
    mots = ["poney", "girafe", "hippopotame", "chaton"]
    resultat = pourcentage_mots_max(mots, 5)

    assert resultat == 75.0

def test_pourcentage_mots_max_tous_superieur():
    """
    Lorsque tous les mots présents dépassent la taille,
    le pourcentage retourné est 100%.
    """
    # Complèter ce test unitaire.
    mots = ["éléphant", "hippopotame", "girafe"]
    resultat = pourcentage_mots_max(mots, 4)
    assert 100.0

def test_pourcentage_mots_max_elements_invalides():
    mots = ["pamplemousse", 42, "cacahuète", None]
    resultat = pourcentage_mots_max(mots, 8)

    assert resultat == 100.0

def test_pourcentage_mots_max_liste_vide():
    mots = []
    resultat = pourcentage_mots_max(mots, 5)

    assert resultat is None

def test_pourcentage_mots_max_tous_inferieur_1(): #ajouter _1 au nom
    """
    Lorsque tous les mots présents sont
    plus petits que la taille, le pourcentage
    retourné est 0.0%.
    """
    # Ajouter le cas de test correspondant à la description
    #       au plan de tests et complèter ce test unitaire.
    mots = ["chat", "chien", "rat"]
    resultat = pourcentage_mots_max(mots, 5)
    assert resultat == 0.0

def test_pourcentage_mots_max_tous_inferieur_2(): #ajouter _2 au nom
    mots = "chat" #remplacer 7 avec "chat"
    resultat = pourcentage_mots_max(mots, 3)

    assert resultat == None