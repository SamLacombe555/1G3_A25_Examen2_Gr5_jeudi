def mot_plus_long(liste_mots):
    """
    Retourne le mot le plus long d'une liste.
    Ignore les éléments qui ne sont pas des chaînes de caractères.

    :param liste_mots: liste de mots
    :return: le mot le plus long ou None si la liste est invalide ou vide
    """
    if not isinstance(liste_mots, list): # ajouter
        print(f"Impossible de trouver le mot le plus long dans {liste_mots}") #ajouter
        return None #ajouter

    max_mot = ""
    try:
        for mot in liste_mots:
            try:
                if len(mot.strip()) > len(max_mot): #ajouter .strip
                    max_mot = mot.strip() #ajouter .strip
            except TypeError:
                pass
            except AttributeError:
                pass

    except TypeError:
        print(f"Erreur. Impossible de trouver le mot le plus long dans {liste_mots}")

    if max_mot != "":
        return max_mot
    else:
        return None

def pourcentage_mots_max(mots, taille):
    """
    Calcule le pourcentage de mots ayant une longueur supérieure à une valeur donnée.

    :param mots: liste de mots
    :param taille: longueur minimale à comparer
    :return: pourcentage (float) de mots dépassant la taille, ou None si impossible
    """
    # Si mots n'est pas de type list
    if not isinstance(mots, list):
        print(f"Impossible de calculer le pourcentage. '{mots}' n'est pas une liste.")
        return None

    #  Corriger les bogues dans le code suivant les erreurs relevées par les tests unitaires de cette fonction.
    #       Indice : chaque mot valide mérite d’être compté, et seuls ceux qui sont suffisamment grands font grimper ton pourcentage !
    total_valide = 0
    count_sup = 0

    for mot in mots:
        try: #ligne ajouter
            longueur = len(mot)
            if longueur > taille: #changer < à >
                count_sup += 1 #changer = à +=
            total_valide += 1 #ligne ajouter
        except TypeError: #ligne ajouter
            pass #ligne ajouter
        except AttributeError: #ligne ajouter
            pass #ligne ajouter

    try: #ligne ajouter
        pourcentage = (count_sup / total_valide) * 100
        return round(pourcentage, 2)
    except ZeroDivisionError: #ligne ajouter
        print("Impossible de calculer le pourcentage. Aucun élément valide") #ligne ajouter
        return None #ligne ajouter

if __name__ == "__main__":
    animaux = ["chat", "chien", "éléphant", "souris", "hippopotame", 42, None, "oiseau"]
    print("Mot le plus long :", mot_plus_long(animaux))
    pourcentage = pourcentage_mots_max(animaux, 5)

    if pourcentage is not None:
        print("Pourcentage de mots de longueur maximale :", pourcentage, "%")
