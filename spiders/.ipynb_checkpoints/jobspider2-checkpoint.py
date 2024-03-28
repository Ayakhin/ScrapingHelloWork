import scrapy
import pandas as pd
import time


class Jobspider2Spider(scrapy.Spider):
    name = "jobspider2"
    allowed_domains = ["www.hellowork.com"]
    start_urls = ["https://www.hellowork.com/fr-fr/emploi/recherche.html?k=D%C3%A9veloppeur+logiciel"]
    custom_settings = {
        'ROBOTSTXT_OBEY': False,
        'DOWNLOAD_DELAY': 20  # Ajout d'un de 3 secondes entre chaque requête
    }

    def parse(self, response):
        # Liste pour stocker les données extraites
        data = []

        #Utilisation des sélecteurs CSS ou XPath pour cibler les balises h3 contenant les offres d'emploi
        job_elements = response.css('h3')

        # Utilisation des sélecteurs CSS ou XPath pour cibler les balises div contenant les informations sur le salaire
        salary_elements = response.css('div.otherinfo')

        for job_element, salary_element in zip(job_elements, salary_elements):
            # Accédez à la balise <a> contenant le titre de l'offre d'emploi
            title_element = job_element.css('a')

            # Accédez à la balise span contenant les informations sur le salaire
            salary_info = salary_element.css('span[data-cy="salaryInfo"]::text').get()

            # Remplacement des caractères spéciaux dans les informations sur le salaire
            if salary_info:
                salary_info = salary_info.replace('\u202f', ' ').strip()

            # Extraction du titre de l'offre d'emploi s'il existe
            if title_element:
                title = title_element.attrib['title']
            else:
                title = None

            # Ajout des données extraites à la liste
            data.append({
                'Title': title,
                'Salary': salary_info if salary_info else None
            })

        # Création d'un DataFrame pandas à partir des données extraites
        df = pd.DataFrame(data)

        # Affichez le DataFrame
        print(df)