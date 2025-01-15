import unittest
import requests
from src.api_client import get_location
from unittest.mock import patch

class ApiClientTests(unittest.TestCase):

    # Usamos el decorador @patch para reemplazar la llamada a requests.get con un objeto simulado
    # Esto evita que se haga una llamada real a la API durante las pruebas
    @patch("src.api_client.requests.get")
    def test_get_location_returns_expected_data(self, mock_get):
        """
        En este test estamos simulando una respuesta exitosa de la API (status_code 200)
        y comprobamos que los datos devueltos son correctos (país, región y ciudad).
        """

        # Configuramos el mock para devolver un estado 200 y un JSON simulado
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "countryName": "USA",
            "regionName": "FLORIDA",
            "cityName": "MIAMI",
        }
        
        # Llamamos a la función get_location con una IP ficticia
        result = get_location("8.8.8.8")

        # Comprobamos que los valores devueltos sean los esperados
        self.assertEqual(result.get("country"), "USA")
        self.assertEqual(result.get("region"), "FLORIDA")
        self.assertEqual(result.get("city"), "MIAMI")

        # Comprobamos que la URL de la API haya sido llamada correctamente
        mock_get.assert_called_once_with("https://freeipapi.com/api/json/8.8.8.8")

    @patch("src.api_client.requests.get")
    def test_get_location_returns_side_effect(self, mock_get):
        """
        En este test estamos simulando un fallo inicial en la llamada a la API (service unavailable),
        seguido de una respuesta exitosa. Se usa side_effect para manejar múltiples comportamientos.
        """

        # Definimos el side_effect, que es una lista de comportamientos a ejecutar secuencialmente
        mock_get.side_effect = [
            requests.exceptions.RequestException("Service Unavailable"),  # Primer error simulado
            unittest.mock.Mock(
                status_code=200,  # Simulamos una respuesta exitosa en la segunda llamada
                json=lambda: {
                    "countryName": "USA",
                    "regionName": "FLORIDA",
                    "cityName": "MIAMI",
                }
            )
        ]
        
        # Comprobamos que la primera llamada lanza una excepción
        with self.assertRaises(requests.exceptions.RequestException):
            get_location("8.8.8.8")

        # Comprobamos que la segunda llamada devuelve los datos esperados
        result = get_location("8.8.8.8")
        self.assertEqual(result.get("country"), "USA")
        self.assertEqual(result.get("region"), "FLORIDA")
        self.assertEqual(result.get("city"), "MIAMI")

        