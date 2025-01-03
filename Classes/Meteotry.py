import requests

class Meteotry:
    def __init__(self):
        """Initialisation de l'URL de l'API et des en-têtes requis"""
        self.api_url = "https://weatherapi-com.p.rapidapi.com/current.json"
        self.api_key = "a1892cd212msh8d5e1cbeb4e4215p1ec1f6jsn839276332c9f"
        self.headers = {
            "X-RapidAPI-Key": self.api_key,
            "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
        }
        
    def getWeather(self):
        latitude = 36.7448043
        longitude = 3.8950017
        querystring = {"q": f"{latitude},{longitude}"}
        response = requests.get(self.api_url, headers=self.headers, params=querystring)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()
    
    def displayWeather(self):
        try:
            weather_data = self.getWeather()
            
            location = weather_data['location']['name']
            region = weather_data['location']['region']
            country = weather_data['location']['country']
            #print(f"Location: {location}, {region}, {country}")

            temp_c = weather_data['current']['temp_c']
            #print(f"Temperature: {temp_c}°C")

            condition = weather_data['current']['condition']['text']
            #print(f"Condition: {condition}")

            # Message en fonction de la température
            if temp_c <= 0:
                message = "Il fait si froid dehors que même les pingouins cherchent des couvertures!"
            elif 0 < temp_c <= 5:
                message = "Un peu frisquet! Le moment est venu de ressortir ce pull moche mais chaud."
            elif 5 < temp_c <= 10:
                message = "Le temps est agréable, une petite veste suffira."
            elif 10 < temp_c <= 15:
                message = "Température agréable! Pas trop chaud, pas trop froid... Juste parfait pour une balade."
            elif 15 < temp_c <= 20:
                message = "Il fait si chaud dehors que votre charisme pourrait provoquer une émeute de lézards."
            elif 20 < temp_c <= 25:
                message = "Le soleil vous fait perdre la tete, pensez à vous changer les idées"
            elif 25 < temp_c <= 30:
                message = "Il fait tellement chaud que même les cactus cherchent de l'ombre!"
            else:
                message = "Il fait très chaud dehors, restez hydraté et évitez le soleil direct."

            print(message)

        except requests.exceptions.RequestException as e:
            print(f"Error fetching weather data: {e}")

    def run(self):
        """Exécuter le processus principal pour obtenir citation traduite."""
        metheo = self.displayWeather()
        if metheo:
            print(metheo)
        else:
            return self.defaultMessage()
        
    def defaultMessage(self):
        """Retourner un message par défaut."""
        return "N'oubliez pas d'etre heureux !"
    
# Example usage:
if __name__ == "__main__":
    weather_api = Meteotry()
    weather_api.run()
