import requests as requests
from bs4 import BeautifulSoup

from DragonBall.Constants.ScrapSagas import ScrapSagas
from DragonBall.Constants.URLS import URL
from DragonBall.Data.OutInformation import OutInformation
from DragonBall.Soup.section import Section
from DragonBall.Soup.summary import Summary
from DragonBall.Soup.tags import Tags


class Sagas:
    def __init__(self, name: str, all_data=False):
        self.name = name
        self.all_data = all_data

    @classmethod
    def saga_list(cls, saga_list: list):
        return [Sagas(i).saga_information() for i in saga_list]

    @staticmethod
    def list():
        request = requests.get(URL.URL_LIST_CHRONO, headers=URL.HEADERS)
        soup = BeautifulSoup(request.content.decode('utf-8'), "html.parser")
        toc = soup.find("div", {"id": "toc"})
        if not toc:
            return {}
        summary_data = toc.text.strip().splitlines()
        return Summary.clean_list_summary(summary_data, [1, -2])

    def saga_information(self):
        url = URL.URL_WIKI + self.name.replace(" ", "_")
        request = requests.get(url, headers=URL.HEADERS)
        soup = BeautifulSoup(request.content.decode('utf-8'), "html.parser")
        list_section = Section.obtain_section_data(soup, 'aside')
        basic_dict = self.__obtain_basic_data(soup, url)
        section_dict = self.__evaluate_scrapper_section(list_section, list(list_section.keys()), ScrapSagas)
        return self.__show_information(basic_dict, section_dict)

    def __obtain_basic_data(self, soup: BeautifulSoup, url: str):
        name = self.__get_official_name(soup, "h1", "id", "firstHeading")
        image = self.__get_image(soup, "a", "class", "image image-thumbnail")
        description = self.__get_description_saga(soup)
        return {"url": url, "name": name, "image": image, "descripcion": description}

    @staticmethod
    def __get_official_name(soup: BeautifulSoup, tag: str, identification: str, element: str):
        # Intento 1: Buscar el h1 con el id exacto
        official_name = Tags.custom_catch_error(soup, tag, identification, element)
        if official_name != OutInformation.RESOURCE_NOT_FOUND:
            return official_name.get_text(strip=True)
        
        # Intento 2: Buscar CUALQUIER etiqueta <h1> en la página
        h1 = soup.find("h1")
        if h1:
            return h1.get_text(strip=True)
            
        # Intento 3: Usar el título de la pestaña del navegador
        if soup.title:
            return soup.title.text.split("|")[0].strip()
            
        return OutInformation.RESOURCE_NOT_FOUND

    @staticmethod
    def __get_image(soup: BeautifulSoup, tag: str, identification: str, name: str):
        found = soup.find(tag, attrs={identification: name})
        if found:
            return found.get("href")
        return OutInformation.RESOURCE_NOT_FOUND

    @staticmethod
    def __get_description_saga(soup: BeautifulSoup):
        [remove_sup.extract() for remove_sup in soup.find_all('sup')]
        try:
            return next(
                p.text.strip() for header in soup.find_all(['h2', 'h3']) if (p := header.find_next_sibling('p')))
        except StopIteration:
            return OutInformation.RESOURCE_NOT_FOUND

    def __evaluate_scrapper_section(self, list_dict, list_search, tag_found: ScrapSagas):
        empty = self.__return_empty_section(list_dict)
        if empty:
            return empty

        section_names = list(tag_found.sections.values())
        names = list_dict.get(section_names[0], OutInformation.RESOURCE_NOT_FOUND)
        data = list_dict.get(section_names[1], OutInformation.RESOURCE_NOT_FOUND)
        serialization = list_dict.get(section_names[2], OutInformation.RESOURCE_NOT_FOUND)

        return {
            "nombres": self.__names_section(names, tag_found.names) if section_names[0] in list_search else names,
            "data": self.__data_section(data, tag_found.data) if section_names[1] in list_search else data,
            "serializacion": self.__serialization_section(serialization, tag_found.serialization) if section_names[2] in list_search else serialization,
        }

    @staticmethod
    def __return_empty_section(list_dict: dict):
        if not list_dict:
            return {
                "nombres": OutInformation.RESOURCE_NOT_FOUND,
                "data": OutInformation.RESOURCE_NOT_FOUND,
                "serializacion": OutInformation.RESOURCE_NOT_FOUND,
            }
        return None

    @staticmethod
    def __names_section(name, lista_tags):
        return {key: Tags.clean_text(Tags.catch_error(name, value)) for key, value in lista_tags.items()}

    @staticmethod
    def __data_section(data, lista_tags):
        return {key: Tags.clean_text(Tags.catch_error(data, value)) for key, value in lista_tags.items()}

    @staticmethod
    def __serialization_section(serialization, lista_tags):
        return {key: Tags.clean_text(Tags.catch_error(serialization, value)) for key, value in lista_tags.items()}

    def __show_information(self, dictionary_basic, dictionary_sections):
        dictionary = {
            "name": dictionary_basic['name'],
            "image": dictionary_basic['image'],
            "description": dictionary_basic['descripcion'],
            "names": dictionary_sections['nombres'],
            "data": dictionary_sections['data'],
            "serialization": dictionary_sections['serializacion'],
            "url_scrap": dictionary_basic['url']
        }
        if self.all_data:
            return dictionary
        return OutInformation.clean_not_found_scrape(dictionary)