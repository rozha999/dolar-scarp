import requests
from bs4 import BeautifulSoup

URL = "https://www.dolar-scraping.docker.sulbaranjc.com/"


def obtener_valor() -> str:
    #1. descargar el html que sirve la pagina local
    respuesta = requests.get(URL, timeout=5)
    respuesta.raise_for_status()

    #2. buscar el elemento que contiene el cambio destactado 
    sopa = BeautifulSoup(respuesta.text, "html.parser")
    elemento = sopa.find(id = "usd-eur-rate")
    if elemento is None:
        raise ValueError("No se encontró el elemento con id 'usd-eur-rate' en la página.")

    #3. devolver solo el texto del valor , sin etiquetas html
    return elemento.get_text(strip=True)




if __name__ == "__main__":
    try:
        print(f"1 USD = {obtener_valor()} EUR")
    except (requests.RequestException, ValueError) as error:
        print(f"Error al obtener el valor del dólar: {error}")
        raise SystemExit(1)