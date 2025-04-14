#Fazendo o consumo de uma API
from requests import *
from math import *

import rich.measure
from Rich import color, format
import os
import time
import tqdm
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich import print as printr
import rich

console = Console()

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
        print(f'{color.vermelho}●{color.end} Status: {response.status_code} Not Found\n')
        print(f'{color.vermelho}Erro: Cidade não encontrada{color.end}')
    else:
        load()
        # temp = floor(data['main']['temp'])
        
        # temperatura = f'Temperatura: {color.ciano}{temp}°C{color.end}'
        clima = f'Clima: {color.ciano}{data['weather'][0]['description']}{color.end}'
        umidade = f'Umidade: {color.ciano}{data['main']['humidity']}%{color.end}'
        pressao = f'Pressão: {color.ciano}{data['main']['pressure']} hPa{color.end}'
        vento = f'Vento: {color.ciano}{data['wind']['speed']} m/s{color.end}'
        feels = f'Sensação térmica: {color.ciano}{floor(data['main']['feels_like'])}°C{color.end}'
        
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'\n{color.verde}●{color.end} Status: {response.status_code}\n')
        # print('-'*(len(temperatura) - 10), data['name'],',', data['sys']['country'], '-'*(len(temperatura) - 10))
        # print(f'🌡️  {temperatura}', 
        #     f'\n☁️  {clima}', 
        #     f'\n💧  {umidade}',
        #     f'\n📈  {pressao}',
        #     f'\n🌬️  {vento}',
        #     f'\n🔥  {feels}'),
        
        info = Text()
        # info.append(f'Temperatura: {floor(data['main']['temp'])}°C')
        # info.append(f'\nClima: {data['weather'][0]['description']}')
        # info.append(f'\nUmidade: {data['main']['humidity']}%')
        # info.append(f'\nPressão: {data['main']['pressure']} hPa')
        # info.append(f'\nVento: {data['wind']['speed']} km/h')
        # info.append(f'\nSensação térmica: {floor(data['main']['feels_like'])}°C')
        info.append("Temperatura: ")
        info.append(f"{floor(data['main']['temp'])}", style="cyan")
        info.append("°C\n")
        
        info.append("Clima: ")
        info.append(f"{data['weather'][0]['description']}\n", style="cyan")

        info.append("Umidade: ")
        info.append(f"{data['main']['humidity']}%\n", style="cyan")

        info.append("Pressão: ")
        info.append(f"{data['main']['pressure']} hPa\n", style="cyan")

        info.append("Vento: ")
        info.append(f"{data['wind']['speed']} km/h\n", style="cyan")

        info.append("Sensação térmica: ")
        info.append(f"{floor(data['main']['feels_like'])}", style="cyan")
        info.append("°C")

        
        panel = Panel(info, width=50, border_style="cyan", title=f'{data['name']}, {data['sys']['country']}')
        printr(panel)
        
while True:
    city = input("\nDigite o nome da cidade, estado ou país: ").capitalize()
    
    if city.lower() == 'sair':
        break
    
    request(city)
