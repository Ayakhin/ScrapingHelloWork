import scrapy
import pandas as pd

class JobSpider(scrapy.Spider):
    name = "jobspider"
    allowed_domains = ["www.hellowork.com"]
    start_urls = ["https://www.hellowork.com/fr-fr/emploi/recherche.html?k=D%C3%A9veloppeur+logiciel&msa=21000&p=1"]
    custom_settings = {
        'ROBOTSTXT_OBEY': False,
        'DOWNLOAD_DELAY': 20  # Ajoutez un délai de 3 secondes entre chaque requête
    }

    def parse(self, response):
        # Liste pour stocker les données extraites
        data = []

        # Utilisez les sélecteurs CSS ou XPath pour cibler les balises h3 contenant les offres d'emploi
        job_elements = response.css('h3')

        # Utilisez les sélecteurs CSS pour cibler les balises span contenant les informations sur le salaire
        salary_elements = response.css('span.tw-text-jobsCandidacy::text').getall()

        # Utilisez les sélecteurs CSS ou XPath pour cibler les balises div contenant les informations sur la localisation
        location_elements = response.xpath('//span[contains(@class, "tw-text-ellipsis") and contains(@class, "tw-whitespace-nowrap") and contains(@class, "tw-block") and contains(@class, "tw-overflow-hidden") and contains(@class, "2xsOld:tw-max-w-[20ch]")]')

        for job_element, salary_info, location_element in zip(job_elements, salary_elements, location_elements):
            # Accédez à la balise <a> contenant le titre de l'offre d'emploi
            title_element = job_element.css('a')

            # Accédez à la balise contenant les informations sur la localisation
            location_info = location_element.css('::text').get()

            # Remplacer les caractères spéciaux dans les informations sur le salaire
            if salary_info:
                salary_info = salary_info.strip().replace('\u202f', ' ')

            # Extrayez le titre de l'offre d'emploi s'il existe
            if title_element:
                title = title_element.attrib['title']
            else:
                title = None

            # Ajoutez les données extraites à la liste
            data.append({
                'Title': title,
                'Salary': salary_info if salary_info else None,
                'Location': location_info.strip() if location_info else None
            })

        # Créez un DataFrame pandas à partir des données extraites
        df = pd.DataFrame(data)

        # Affichez le DataFrame
        print(df)
