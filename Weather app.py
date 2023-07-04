import pyowm
from tkinter import *
import tkinter as tk

class GUI:
    def __init__(self):
        #Generate window
        self.window = tk.Tk()
        self.window.geometry("500x500")
        self.window.title("Weather app V1")

        self.label = tk.Label(self.window, text="Weather app V1", font= ('Arial, 18'))
        self.label.pack(padx=20, pady =10)

        self.label = tk.Label(self.window, text="Enter your location", font= ('Arial, 14'))
        self.label.pack(padx=20, pady =10)

        self.textbox = tk.Text(self.window, height = 3, font= ('Arial, 10'))
        self.textbox.pack(padx=150)

        #Button which passes the generate function
        self.button = tk.Button(self.window, text = "Get weather", command=self.getWeather)
        self.button.pack(pady=10)
        
        self.label2 = tk.Label(self.window, text = "")
        self.label2.pack(padx=20, pady =30)    

        self.label3 = tk.Label(self.window, text = "")
        self.label3.pack(padx=20, pady =30)    

        self.window.mainloop()

    def getWeather(self):
        self.label2.destroy()
        self.label3.destroy()

        owm = pyowm.OWM('ENTER_PYOWM_API_KEY_HERE')
        weather_mgr = owm.weather_manager()
        place = self.textbox.get('1.0', tk.END)

        observation = weather_mgr.weather_at_place(place)
        temperature = observation.weather.temperature("celsius")["temp"]
        humidity = observation.weather.humidity
        wind = observation.weather.wind()

        self.label2 = tk.Label(self.window, text = (f'Temperature: {temperature}°C', (f'Humidity: {humidity}%'), (f'Wind Speed: {wind["speed"]} m/s')))
        self.label2.pack(padx=10, pady =15)    

        self.label3 = tk.Label(self.window, text = "Weather retrieved from OpenWeatherMap")
        self.label3.pack(padx=5, pady =5)    

GUI()