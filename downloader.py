import requests

response = requests.get('https://raw.githubusercontent.com/fivethirtyeight/data/master/nba-elo/nbaallelo.csv')

response.raise_for_status()

with open('nba.csv', 'wb') as csv_file: 

    csv_file.write(response.content)

print('archivo descargado')

