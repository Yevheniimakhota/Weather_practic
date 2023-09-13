import requests


cities = ['svo', 'Лондон','Череповец']
for city in cities :
    url1 = f'https://wttr.in/{city}?mMnqT&lang=ru'
    response = requests.get(url1)
    print(response.text)