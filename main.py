lazy import requests
from agenda import agenda
from codes_weather import traducao_codigo

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

calendario = agenda()
calendario.adicionarEvento('Almoço em familia', '2026-11-17')
calendario.mostrarCalendario()