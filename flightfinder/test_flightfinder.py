mport pytest
from flightfinder.models import City

@pytest.mark.django_db
def test_city_str():
    # Tworzymy przykładowe miasto do testów
    honolulu_city = City.objects.create(
        name='Honolulu'
    )

    # Sprawdzamy, czy metoda __str__ zwraca oczekiwany rezultat
    cities = City.objects.all()
    assert len(cities) == 1