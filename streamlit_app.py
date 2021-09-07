import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import requests
import time
st.title('Weather Api using Streamlit ,python')

 

def getWeather(path):
    city = path
    api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=56622db96b5640dd7d721d1d57524d71"
    
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    
    temp = int(json_data['main']['temp'] - 273.15)

    min_temp = int(json_data['main']['temp_min'] - 273.15)
    
    max_temp = int(json_data['main']['temp_max'] - 273.15)
   
    pressure = json_data['main']['pressure']

    humidity = json_data['main']['humidity']

    wind = json_data['wind']['speed']
 
    sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))

    sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600))
 

    final_info = condition + "\n" + str(temp) + "°C"
    st.write(final_info) 
    final_data = "\n"+ "Min Temp: " + str(min_temp) + "°C" + "\n" + "Max Temp: " + str(max_temp) + "°C" +"\n" + "Pressure: " + str(pressure) + "\n" +"Humidity: " + str(humidity) + "\n" +"Wind Speed: " + str(wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset
    st.write(final_data)
    df = pd.DataFrame(columns=['condition', 'temp', 'min_temp', 'max_temp','pressure','humidity','wind','sunrise','sunset'])
    
    
    # label1.config(text = final_info)
    #label2.config(text = final_data)


path = st.text_input('Enter City  Name')
if st.button('Get Weather'):
#getWeather(path)
    if path=="":
        st.error("Please enter a valid city name")
    else:
        st.write(getWeather(path))
