# Tests unitaires pour la fonction _mot_plus_long_
- La fonction _mot_plus_long_ ne contient pas de bogues. 
- Créer au plan de tests contenant au moins 5 cas de tests **DIFFÉRENTS/VARIÉS**.
- Créer les tests unitaires pour tous les cas de tests.

| **animaux**                                                                | **Résultat attendu** | **Remarque ou Message afficher**                       |
|----------------------------------------------------------------------------|----------------------|--------------------------------------------------------|
| ["chat", "chien", "éléphant", "souris", "hippopotame", 42, None, "oiseau"] | "hippopotame"        | "42" et None ignorés                                   |
| ["éléphant", "hippopotame", ""]                                            | "hippopotame"        |                                                        |
| []                                                                         | None                 |                                                        |
| "chat"                                                                     | None                 | "Impossible de trouver le mot le plus long dans liste" |
| [" chat ", "chien", "rat"]                                                 | "chien"              | Les espaces dans " chat " sont ignorés                 |
|                                                                            |                      |                                                        |
|                                                                            |                      |                                                        |

# Tests unitaires pour la fonction _pourcentage_mots_max_
| **mots**                                     | **taille** | **Résultat attendu** | **Remarque ou Message affiché**                                      |
|----------------------------------------------|------------|----------------------|----------------------------------------------------------------------|
| ["poney", "girafe", "hippopotame", "chaton"] | 5          | 75.0                 |                                                                      |
| ["éléphant", "hippopotame", "girafe"]        | 4          | 100.0                |                                                                      |
| ["pamplemousse", 42, "cacahuète", None]      | 8          | 100.0                | "42" et None ignorés                                                 |
| []                                           | 5          | None                 | "Impossible de calculer le pourcentage. Aucun élément valide."       |
| ["chat", "chien", "rat"]                     | 5          | 0.0                  |                                                                      |
| "chat"                                       | 3          | None                 | "Impossible de calculer le pourcentage. 'chat' n'est pas une liste." |
