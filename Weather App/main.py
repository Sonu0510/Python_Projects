import requests
import json
import win32com.client as wincom

while True:
    city = input("Enter city name to get weather information \n") #when prompt is given enter city name and you will get weather information on that specific city
    if city == "":
        break
    url = f"https://api.weatherapi.com/v1/current.json?key=5f0a0ae4ac414fabb6473818231307&q={city}"
    response = requests.get(url)
    weatherDict = json.loads(response.text)
    temp = weatherDict["current"]["temp_c"]
    print(temp)
    speak = wincom.Dispatch("SAPI.SpVoice")
    speak.Speak(f"The current temperature in {city} is {temp} degree celsius")
