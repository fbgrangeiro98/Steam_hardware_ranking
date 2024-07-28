import requests
import pandas as pd
import json
import time
import pyodbc 
import urllib
import sqlalchemy

##extração dados dos jogos
url = 'https://api.steampowered.com/ISteamApps/GetAppList/v2/'

response = requests.get(url)

data = json.loads(response.text)

df = pd.json_normalize(data['applist']['apps'])

app_sem_nome = df.loc[df['name'] == '','appid'].index

##dropa todos os jogos  sem nome
df = df.drop(app_sem_nome)
