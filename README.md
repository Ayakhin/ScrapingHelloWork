# Projet de Scraping avec Scrapy

Ce projet contient deux spiders Scrapy conçus pour extraire des données du site www.hellowork.com.

## Spider 1 : MonSpider

Ce spider extrait le texte des balises `<h1>` situées dans la page d'accueil du site.

### Utilisation

Pour exécuter ce spider, assurez-vous d'avoir Scrapy installé et exécutez la commande suivante dans le terminal :


- !scrapy crawl mon_spider


Cela lancera le spider qui collectera les données et les enregistrera dans un fichier JSON nommé `output.json`.

## Spider 2 : Jobspider

Ce spider extrait des informations sur les offres d'emploi pour le poste de développeur logiciel à partir de la page de recherche du site.

### Utilisation

Pour exécuter ce spider, utilisez la même procédure que pour le premier spider :


- !scrapy crawl jobspider


Les données extraites seront enregistrées dans un fichier JSON nommé `jobs.json`.

### Installation

Pour exécuter ces spiders, vous aurez besoin de Python et de Scrapy installés sur votre machine. Vous pouvez les installer en exécutant la commande suivante :


Les données extraites seront enregistrées dans un fichier JSON nommé `jobs.json`.

### Installation

Pour exécuter ces spiders, vous aurez besoin de Python, Scrapy et de pandas installés sur votre machine. Vous pouvez les installer en exécutant la commande suivante :

- pip install scrapy
- pip install pandas

