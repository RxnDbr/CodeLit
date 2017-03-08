#PROJET CODE LITTÉRAIRE
##Objectifs généraux : 
- Apporter des outils pour nos objets de recherches
- Mettre en valeur les projets de numérisation du CRILQ
- Apprendre la programmation pour apprendre à développer nos propores outils

##Objectifs spécifiques : 
 - Trouver et extraire des textes provenant de journaux stockés dans une BDD en fonction de leur thématique
 - Sectionner des journaux en articles et y attibuer une catégorie (fiction, information, consommation) pour faire des stats dessus, faire des comparaisons.
##Démaches
Dans un premier temps, il faut étudier les articles individuellement. 
 - ETAPE 1 : recherche de vocabulaire/expression regulière (uniquement centré sur le texte brut) dans journal. 
Trouver les journaux qui contiennent REGEX
 - ETAPE 2 : recherche en fonction de champs lexical ( uniquement centré sur le texte brut) . 
Trouver les journaux qui contiennent champs lexical
 - ETAPE 3 : Sectionner journal en articles 
 - ETAPE 4 : Affiner l'étape 1 et 2 en ne faisant ressortir que les articles intéressants
 - ETAPE 5 : Attribution d'une catégorie à un article (F/I/C)
 - ETAPE 6 : annotation automatique d'article 
    a - Titre (le faire à la main ; travaille sur le format)
    b - Sujet (classification - apprentissage automatique)
    c - Mot clef (récup code tout fait)
    
Dans un second temps, on pourra faire de la comparaison, étudier les évolutions des articles, des journaux, des sujets, etc. On verra quand on sera rendu là. 
 
##Bases théoriques nécessaires aux étapes citées précédemment
- Python
 - Algorithmie générale
 - Types et opérations sur les types
 - Conditions et boucles (while et for)
 - Fonctions
 - Traitement de fichier texte
- Base de données
- GitHub
- Traitement automatique du langage : Expression régulière , classification automatique , génération de mot clef / résumé
- Découverte de wordnet

##Materiel : 
 - Fichiers de différents formats : 
    - Format permettant le traitement de texte : HTML, texte, PDF avec analyse de texte possible
    - Format ne permettant pas le traitement de texte : PDF numérisation, JPG, papier
    => pour l'instant se concentrer sur format permettant le traitement de texte, on verra par la suite pour le reste.
 - Issus de bases de données provenant de :
  - Gallica
  - BanQ
  - DolQ
 - Base de données à construire: 
  - ARTICLE : Titre / Sujet / Mot Clef / Journal / Taille de l'article  / Article / Auteur / Type (fiction, info, conso) / Résumé??
  - JOURNAL : Articles / nombre de page / date / orientation politique ou thematique du journal
 - Code
  - librairies existantes
  - code existant
  - code à développer

##Ressources : 
- 2 littéraires purs
- 1 littéraire très sensibilisé aux enjeux du numérique
- 1 ingénieur avec compétences en info
- ça prend un infomaticien en plus??


