import scrapy
import pandas as pd
import time

class JobSpider(scrapy.Spider):
    name = "jobspider"
    allowed_domains = ["www.hellowork.com"]
    start_urls = ["https://www.hellowork.com/fr-fr/emploi/recherche.html?k=D%C3%A9veloppeur+logiciel"]
    custom_settings = {
        'ROBOTSTXT_OBEY': False,
        'DOWNLOAD_DELAY': 20  # Ajoutez un délai de 3 secondes entre chaque requête
    }

    def parse(self, response):
        # Liste pour stocker les données extraites
        data = []

        # Utilisez les sélecteurs CSS ou XPath pour cibler les balises h3 contenant les offres d'emploi
        job_elements = response.css('h3')

        for job_element in job_elements:
            # Accédez à la balise <a> contenant le titre de l'offre d'emploi
            title_element = job_element.css('a')

            # Extrayez le titre de l'offre d'emploi s'il existe
            if title_element:
                title = title_element.attrib['title']
            else:
                title = None

            # Ajoutez les données extraites à la liste
            data.append({
                'Title': title
            })

        # Créez un DataFrame pandas à partir des données extraites
        df = pd.DataFrame(data)

        # Affichez le DataFrame
        print(df)
