# Projet Scrapy - Extraction de données depuis HelloWork

Ce projet utilise Scrapy pour extraire des données à partir du site web HelloWork (www.hellowork.com).

## Spiders

Le projet contient trois spiders, chacun ayant un but spécifique :

1. **JobSpider**
    - Ce spider extrait les offres d'emploi disponibles sur HelloWork, y compris le titre de l'offre, le salaire et la localisation.
    - L'URL de départ pour ce spider est : [https://www.hellowork.com/fr-fr/emploi/recherche.html?k=D%C3%A9veloppeur+logiciel&msa=21000&p=1](https://www.hellowork.com/fr-fr/emploi/recherche.html?k=D%C3%A9veloppeur+logiciel&msa=21000&p=1)

2. **JobSpider2**
    - Ce spider extrait également les offres d'emploi pour les développeurs logiciels sur HelloWork, mais il utilise une autre méthode pour extraire les informations de salaire.
    - L'URL de départ pour ce spider est : [https://www.hellowork.com/fr-fr/emploi/recherche.html?k=D%C3%A9veloppeur+logiciel](https://www.hellowork.com/fr-fr/emploi/recherche.html?k=D%C3%A9veloppeur+logiciel)

3. **MonSpider**
    - Ce spider extrait un élément spécifique de la page HelloWork, en l'occurrence le texte contenu dans les balises `h1`.
    - L'URL de départ pour ce spider est : [https://www.hellowork.com/fr-fr/](https://www.hellowork.com/fr-fr/)

## Configuration

Chaque spider est configuré pour respecter un délai de téléchargement entre chaque requête de 20 secondes afin de ne pas surcharger le serveur.

## Utilisation

Pour utiliser ce projet, assurez-vous d'avoir Python et Scrapy installés. Ensuite, suivez ces étapes :

1. Cloner le dépôt : `git clone https://github.com/Ayakhin/ScrapingHelloWork`
2. Accéder au répertoire du projet : `cd helloworkproj`
3. Exécuter le spider souhaité : 
   - Pour le JobSpider : `scrapy crawl jobspider`
   - Pour le JobSpider2 : `scrapy crawl jobspider2`
   - Pour le MonSpider : `scrapy crawl mon_spider`

Les données extraites seront affichées dans la console et peuvent être également enregistrées dans des fichiers ou traitées selon vos besoins.

---
