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
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'\n{color.verde}●{color.end} Status: {response.status_code}\n')
        
        info = Text()

        info.append("Temperatura: ")
        info.append(f"{floor(data['main']['temp'])}", style="cyan")
        info.append("°C\n")
        
        info.append("Clima: ")
        info.append(f"{data['weather'][0]['description']}\n", style="cyan")

        info.append("Umidade: ")
        info.append(f"{data['main']['humidity']}", style="cyan")
        info.append("%\n")

        info.append("Pressão: ")
        info.append(f"{data['main']['pressure']} ", style="cyan")
        info.append("hPa\n")

        info.append("Vento: ")
        info.append(f"{data['wind']['speed']} ", style="cyan")
        info.append("km/h\n")

        info.append("Sensação térmica: ")
        info.append(f"{floor(data['main']['feels_like'])}", style="cyan")
        info.append("°C")
        
        countryName = data['name']
        country = ''
        
        country = "África" if countryName == "Africa" else data['sys']['country']
        
        panel = Panel(info, width=50, title=f'{data['name']}, {country}')
        printr(panel)
        
while True:
    city = input("\nDigite o nome da cidade, estado ou país: ").capitalize()
    
    if city.lower() == 'sair':
        break
    
    request(city)
