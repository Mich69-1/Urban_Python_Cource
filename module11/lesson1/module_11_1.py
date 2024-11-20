# Домашнее задание по теме "Обзор сторонних библиотек Python"

import requests
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# URL для получения прогноза от API open-meteo
url = "https://api.open-meteo.com/v1/forecast"

# Географические координаты любой точки, например, Москва
latitude = 55.7558
longitude = 37.6176

# Параметры запроса
params = {
    "latitude": latitude,
    "longitude": longitude,
    "hourly": "temperature_2m"
}

# Отправляем GET-запрос к API open-meteo
response = requests.get(url, params=params)

# Проверяем успешность запроса
if response.status_code == 200:
    data = response.json()
    # Преобразуем полученные данные в словарь
    time_data_dict = dict(zip(data["hourly"]["time"], data["hourly"]["temperature_2m"]))
else:
    print("Ошибка при выполнении запроса:", response.status_code)

# Преобразование строковых дат в объекты datetime
dates = [datetime.fromisoformat(date) for date in time_data_dict.keys()]
temperatures = list(time_data_dict.values())

# Создание графика
plt.figure(figsize=(12, 6))
plt.plot(dates, temperatures, marker='o', color='b', linestyle='-')

# Настройки осей и формат дат
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))
plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval=5))
plt.gcf().autofmt_xdate()

# Наименования осей и заголовок графика
plt.xlabel('Дата и время')
plt.ylabel('Температура, ℃')
plt.title('График температур')

# Отображение графика
plt.grid(True)
plt.tight_layout()
plt.show()
