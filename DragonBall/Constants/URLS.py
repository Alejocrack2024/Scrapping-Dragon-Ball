class URL:
    URL_BASE = "https://dragonball.fandom.com/"
    URL_WIKI = "https://dragonball.fandom.com/es/wiki/"

    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3"
    }

    URL_LIST_CHARACTERS = URL_WIKI + "Lista_de_personajes"
    URL_LIST_FUSIONS = URL_WIKI + "Lista_de_fusiones"
    URL_LIST_PLANETS = URL_WIKI + "Lista_de_planetas"
    URL_LIST_CHRONO = URL_WIKI + "Cronología"
    URL_LIST_GAMES = URL_WIKI + "Lista_de_videojuegos"