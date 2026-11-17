import requests

def obter_previsao():
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": -8.0539,
    	"longitude": -34.8811,
    	"daily": "weather_code",
    	"timezone": "America/Sao_Paulo",
        "forecast_days": 16,
    }

    try:
        resposta = requests.get(url, params)

        resposta.raise_for_status()

        return(resposta.json())
    except requests.RequestException:
        print("Aviso: Não foi possível consultar o clima no momento (verifique sua conexão).")
        return None