import requests
from pyfirmata import Arduino
city_name = 'Irbid'
API_key = 'cd79398a8aeca165334351bec5c4aa7c'
url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}'

result = requests.get(url).json()
temp = float(result['main']['temp'])
temp = round(temp - 273.0,2)
print(temp)
board = Arduino('COM3')
RLED = board.digital[13]
GLED = board.digital[12]
BLED = board.digital[11]
if temp >= 25.1 :
    RLED.write(1)
    GLED.write(0)
    BLED.write(0)
elif temp <=10.1 :
    RLED.write(0)
    GLED.write(0)
    BLED.write(1)
elif 25.1 < temp > 10.1 :
    RLED.write(0)
    GLED.write(1)
    BLED.write(0)


