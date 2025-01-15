import requests

# Función que obtiene la ubicación geográfica a partir de una dirección IP
def get_location(ip):
    """
    Esta función recibe una dirección IP y devuelve la ubicación geográfica asociada a esa IP
    utilizando la API de FreeIPAPI. La API devuelve información sobre el país, la región y la ciudad
    donde se encuentra la IP.
    
    Parámetros:
    - ip: Dirección IP de la que se desea obtener la información geográfica
    
    Retorna:
    - Un diccionario con el país, la región y la ciudad asociados con la IP.

    Ejemplo de uso:
    >>> get_location('8.8.8.8')
    {'country': 'United States', 'region': 'California', 'city': 'Mountain View'}
    """
    
    # Construcción de la URL para la API utilizando la IP proporcionada
    url = f"https://freeipapi.com/api/json/{ip}"
    
    # Realizamos la solicitud GET a la API
    response = requests.get(url)
    
    # Verificamos si la solicitud fue exitosa (código de estado 2xx)
    response.raise_for_status()
    
    # Convertimos la respuesta de la API en formato JSON
    data = response.json()
    
    # Devolvemos un diccionario con los detalles de la ubicación
    return {
        "country": data["countryName"],  # Nombre del país
        "region": data["regionName"],    # Nombre de la región o estado
        "city": data["cityName"]         # Nombre de la ciudad
    }