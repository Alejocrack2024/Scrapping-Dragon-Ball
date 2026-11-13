import pytest

from DragonBall.Data.Characters import Characters
from DragonBall.Data.Fusions import Fusions
from DragonBall.Data.Planets import Planets
from DragonBall.Data.Sagas import Sagas
from DragonBall.Data.VideoGames import VideoGames


@pytest.mark.parametrize("cls, name, method", [
    (Characters, "Goku", "character_information"),
    (Fusions, "Gogeta", "fusion_information"),
    (Planets, "Planeta_Vegeta", "planet_information"),
    (Sagas, "Saga_de_Freezer", "saga_information"),
    (VideoGames, "Dragon_Ball_FighterZ", "game_information"),
])
def test_scraping_no_crash(cls, name, method):
    result = getattr(cls(name), method)()
    assert isinstance(result, dict)
    assert "name" in result


def test_personaje_inexistente_no_crash():
    """Un personaje que no existe no debe lanzar excepción, solo devolver dict vacío o sin datos."""
    result = Characters("PersonajeQueNoExiste123ABC").character_information()
    assert isinstance(result, dict)


def test_all_data_flag():
    """Con all_data=True no debe eliminar las claves 'Not Found In Web'."""
    result = Characters("Goku", all_data=True).character_information()
    assert isinstance(result, dict)
    assert "name" in result
    assert "url_scrap" in result


def test_list_devuelve_dict():
    assert isinstance(Characters.list(), dict)