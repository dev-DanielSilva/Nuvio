import requests
from flask import render_template, request, redirect, url_for, flash

# Configuração para WeatherAPI
WEATHERAPI_KEY = "c011d70a389a4fa6970214743252008" 
WEATHERAPI_URL = "http://api.weatherapi.com/v1/current.json"

def init_app(app):

    @app.route('/', methods=['GET', 'POST'])
    def home():
        if request.method == "POST":
            city = request.form.get("city")
            if city:
                return redirect(url_for("weather", city=city))
        return render_template("home.html")

    @app.route('/weather/<city>')
    def weather(city):
        params = {
            "key": WEATHERAPI_KEY,
            "q": city,
            "lang": "pt"
        }
        
        try:
            response = requests.get(WEATHERAPI_URL, params=params, timeout=10)
            data = response.json()
            
            if response.status_code == 200:
                weather_data = {
                    "city": data["location"]["name"],
                    "temperature": data["current"]["temp_c"],
                    "humidity": data["current"]["humidity"],
                    "wind": data["current"]["wind_kph"],
                    "description": data["current"]["condition"]["text"],
                    "icon": data["current"]["condition"]["icon"],
                    "feels_like": data["current"]["feelslike_c"]
                }
                return render_template("weather.html", weather=weather_data)
            else:
                error_msg = data.get("error", {}).get("message", "Erro desconhecido")
                return render_template("weather.html", error=error_msg, city=city)
                
        except Exception as e:
            return render_template("weather.html", error=f"Erro: {str(e)}", city=city)