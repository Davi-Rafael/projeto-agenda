import requests

url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": -8.0539,
	"longitude": -34.8811,
	"daily": "weather_code",
	"timezone": "America/Sao_Paulo",
    "forecast_days": 16,
}

resposta = requests.get(url, params)
dados = resposta.json()