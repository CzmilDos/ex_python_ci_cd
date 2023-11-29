* Créer un répertoir git documenté avec des markdowns
* Cloner
* Créer une github action avec un linter et pytest
* Créer 2 fichier : run.py, test_run.py
* Créer un répertoire data
* Y insérer le fichier iris.csv
* Créer dans run .py:
    * Une fonction qui importe le fichier csv en Dataframe et qui renomme les colonnes en : [sepal_length, sepal_width,	petal_length, petal_width, variety]
    * Une fonction qui prend une partie du Dataset (sample) de 50 lignes
    * Une fonction qui qui multiplie le dataset sample par 3 avec un pd.concat (on devrait avoir 150 lignes après cette fonction)
    * Une fonction qui créé qui colonne "total_sepal" qui est l'addition de sepal_length et sepal_width
    * De mmême pour "total_petal"

* Créer dans test_run.py les tests associés

* dans la fonction main():
(Appeler les fonctions écrites précédement)
    * Importer les données et renommer les col
    * Prendre 50 lignes aléatoirement
    * Multiplie les données par 3
    * Ajout les colonnes total_sepal et total_petal
    * Print la shape du dataframe
    * Print les 2 premières lignes du dataframe

push sur github et m'envoyer le lien vers le repertoire