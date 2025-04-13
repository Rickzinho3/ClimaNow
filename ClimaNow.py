#Fazendo o consumo de uma API
from requests import *
from math import *
from Rich import color, format
import os
import time
import tqdm

key = 'a4a46591cde2403cee5974af4a061503'

print(f"\n⚙️  {color.amarelo}System{color.end}: digite {format.bold}sair{format.end} para encerrar o programa. \n")

def load():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\nBucando informações...')
    for _ in tqdm.tqdm(range(100), desc="Buscando", ncols=70):
        time.sleep(0.01)

def request(city):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&lang=pt_br&units=metric'
    response = get(url)
    data = response.json()

    if city.isspace() or city == '':
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'{color.vermelho}Erro: Campo vazio{color.end}')
    elif city.isnumeric():
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'{color.vermelho}Erro. Digite o nome de uma {format.bold}{format.ul}cidade{color.end}')
    elif  response.status_code != 200 or response.status_code == 404:
        # load()
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'{color.vermelho}●{color.end} Status: {response.status_code}\n')
        print(f'{color.vermelho}Erro: Cidade não encontrada{color.end}')
    else:
        load()
        temp = floor(data['main']['temp'])
        
        temperatura = f'Temperatura: {color.ciano}{temp}°C{color.end}'
        clima = f'Clima: {color.ciano}{data['weather'][0]['description']}{color.end}'
        umidade = f'Umidade: {color.ciano}{data['main']['humidity']}%{color.end}'
        pressao = f'Pressão: {color.ciano}{data['main']['pressure']} hPa{color.end}'
        vento = f'Vento: {color.ciano}{data['wind']['speed']} m/s{color.end}'
        feels = f'Sensação térmica: {color.ciano}{floor(data['main']['feels_like'])}°C{color.end}'
        
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'\n{color.verde}●{color.end} Status: {response.status_code}\n')
        print('-'*(len(temperatura) - 10), city, '-'*(len(temperatura) - 10))
        print(f'🌡️  {temperatura}', 
            f'\n☁️  {clima}', 
            f'\n💧  {umidade}',
            f'\n📈  {pressao}',
            f'\n🌬️  {vento}',
            f'\n🔥  {feels}'),
        
while True:
    city = input("\nDigite o nome da cidade, estado ou país: ").capitalize()
    
    if city.lower() == 'sair':
        break
    
    request(city)

print("olá mundo")
