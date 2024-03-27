import scrapy

class JobspiderSpider(scrapy.Spider):
    name = "jobspider"
    allowed_domains = ["www.hellowork.com"]
    start_urls = ["https://www.hellowork.com/fr-fr/emploi/recherche.html?k=D%C3%A9veloppeur+logiciel"]
    custom_settings = {
        'ROBOTSTXT_OBEY': False
    }

    def parse(self, response):
        # Sélectionner toutes les balises <li> contenant une balise <ul>
        li_with_ul_elements = response.xpath('//li[ul]')

        # Itérer sur chaque balise <li> sélectionnée
        for li_element in li_with_ul_elements:
            # Extraire le texte de la balise <ul> à l'intérieur de la balise <li>
            ul_text = li_element.xpath('./ul//text()').getall()
            # Concaténer le texte extrait en une seule chaîne
            ul_text_combined = ' '.join(ul_text).strip()

            # Extraction du salaire
            salary = response.css('tw-tag-attractive-s tw-readonly::text').get()

            # Extraction du poste
            job_title = response.css('span[data-cy="jobTitle"]::text').get()

            # Extraction de la localisation
            location = response.css('span.tw-text-grey::text').get()

            # Extraction du type de poste
            job_type = response.css('span.tw-inline-flex.tw-typo-m.tw-text-grey::text').get()

            # Extraction du texte dans la balise <p>
            description = response.css('p::text').get()

            yield {
                'salary': salary.strip() if salary else None,
                'ul_text': ul_text_combined if ul_text_combined else None,
                'job_title': job_title.strip() if job_title else None,
                'location': location.strip() if location else None,
                'job_type': job_type.strip() if job_type else None,
                'description': description.strip() if description else None
            }
