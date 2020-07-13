
import requests 
city = input("What is your city?")

api = "http://api.openweathermap.org/data/2.5/weather?q=London&units=imperial&appid=923718dea61d364f34c9b6c3ae119aca"

data = requests.get(api).json()


temperature = int((data["main"]["temp"]))

def what_to_wear():
    if temperature <= 50:
        return ("Wear a thick jacket")
    if temperature >= 51 and temperature <= 64:
        return ("Wear a thick hoodie")
    if temperature >= 65 and temperature <= 70: 
        return ("Wear a t-shirt!")
    if temperature >= 70 and temperature <= 85: 
        return ("Wear shorts")
    if temperature > 85: 
        return ("Wear a bikini, its beach season :)")

print(what_to_wear())