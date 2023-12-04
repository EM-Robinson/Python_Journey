#Imports library to allow API requests

import requests
api_key = 'd925c13948d44e51113f27d333d18a91'

#Prompting user for city name
user_input = input("Enter city: ")
#print(user_input) - Testing input

#GET Request - Calling API
weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")
#print(weather_data.status_code) - confirming successful API call

#print(weather_data.json())

#
if weather_data.json()['cod'] == '404':
    print("No City Found")
else:
    #Stores current weather
    weather = weather_data.json()['weather'][0]['main']

    #Stores current temperature and rounds to nearest whole number
    temp = round(weather_data.json()['main']['temp'])
    high = round(weather_data.json()['main']['temp_max'])
    low = round(weather_data.json()['main']['temp_min'])
    #wind = weather_data.json()['wind']['speed']

#Prints results of current weather
    print(f"The weather in {user_input} is: {weather}")
    print(f"The temperature in {user_input} is: {temp} Fahrenheit with a high of {high} and a low of {low}")