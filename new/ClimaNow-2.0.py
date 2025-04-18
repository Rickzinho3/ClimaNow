""" Clima Now 2.0
    @Author: J Henrique
    @Date: 18.04.2025
    @Version: 1.0
"""

from requests import get
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.progress import Progress, SpinnerColumn, BarColumn, TimeElapsedColumn, TextColumn
from math import *
import datetime
import os
#Horário local
datetime = datetime.datetime.now()
h = datetime.hour
m = datetime.minute
s = datetime.second
day = datetime.day
month = datetime.month

console = Console()

console.print('Tecle [green]Enter[/] para ver o clima da sua localização atual.')

#Pega a localização atual do usuário
def search_local():
    url_local = "http://ip-api.com/json/"
    resposta = get(url_local)
    dados_local = resposta.json()

    if dados_local["status"] == "success":
        return dados_local['city']
    else:
        print("Não foi possível obter a localização.")
#Buscando dados
def search_clima(city):
    try:
        #formatando o nome da cidade
        url_city = f'https://geocoding-api.open-meteo.com/v1/search?name={city}'
        cityF = get(url_city).json()
        city = cityF['results'][0]['name']
        
        if not cityF:
            console.print('erro')
            return
        
        with Progress(
        SpinnerColumn(),
        TextColumn("[bold blue]{task.description}"),
        BarColumn(bar_width=None),
        TimeElapsedColumn(),
        console=console
        ) as progress:
            task = progress.add_task("[cyan]Buscando coordenadas...", total=3)
            #convertendo a localização para latitude e longitude
            url = f'https://nominatim.openstreetmap.org/search?q={city}&format=json'

            headers = {
                "User-Agent": "clima/1.0 (henriqueferreiraaf56@gmail.com)"
            }

            response = get(url, headers=headers)
            data = response.json()
            
            progress.update(task, advance=1, description="[cyan]Buscando clima...")

            lat = data[0]['lat']
            lon = data[0]['lon']
            #Fazendo a busca dos dados
            url_clima = f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&lang=pt_br&current=apparent_temperature,is_day,precipitation,rain,surface_pressure,wind_speed_10m,cloud_cover,wind_direction_10m,relative_humidity_2m'
            responseClima = get(url_clima)
            dataClima = responseClima.json()
            
            
            temp = trunc(dataClima['current']['apparent_temperature'])
            dia_noite = ''
            vento = trunc(dataClima['current']['wind_speed_10m'])
            direcao_vento = dataClima['current']['wind_direction_10m']
            umidade = dataClima['current']['relative_humidity_2m']
            pressao = dataClima['current']['surface_pressure']
            precp = trunc(dataClima['current']['precipitation'])
            chuva = trunc(dataClima['current']['rain'])
            nuvens = ''
            #para nuvens
            if dataClima['current']['cloud_cover'] <= 20:
                nuvens = 'Céu limpo'
            elif dataClima['current']['cloud_cover'] <= 50:
                nuvens = 'Parcialmente nublado'
            elif dataClima['current']['cloud_cover'] <= 60:
                nuvens = 'Nublado'
            elif dataClima['current']['cloud_cover'] <= 100:
                nuvens = 'Coberto de nuvens'
            #Para dia/noite
            dia_noite = 'Dia' if dataClima['current']['is_day'] != 0 else 'Noite'
            progress.update(task, advance=2, description="[green]Processando dados...")
            # time.sleep(1)
            
        info = Text()

        info.append('Temperatura: ')
        info.append(f'{temp}', style='cyan')
        info.append('°C\n')
        
        info.append('Horário: ')
        info.append(f'{dia_noite}, ', style='cyan')
        info.append(f'{day}/{month} - ', style='green')
        info.append(f'{h}:{m}:{s}\n', style='green')
        
        info.append('Vento: ')
        info.append(f'{vento}', style='cyan')
        info.append(' km/h\n')
        
        info.append('Direção do vento: ')
        info.append(f'{direcao_vento}', style='cyan')
        info.append('°\n')
        
        info.append('Pressão: ')
        info.append(f'{pressao}', style='cyan')
        info.append(' hPa\n')
        
        info.append('Umidade: ')
        info.append(f'{umidade}', style='cyan')
        info.append('%\n')
        
        info.append('Preciptação: ')
        info.append(f'{precp}', style='cyan')
        info.append('mm\n')
        
        info.append('Chuva: ')
        info.append(f'{chuva}', style='cyan')
        info.append('mm\n')
        
        info.append('Nuvens: ')
        info.append(f'{nuvens}', style='cyan')
        
        os.system('cls' if os.name == 'nt' else 'clear')
        console.print(f'[green]●[/] Status: [green]{responseClima.status_code}[/]')
        panel = Panel(info, title=city, width=50, border_style='cyan')
        console.print(panel)
        
    except Exception as e:
        os.system('cls' if os.name == 'nt' else 'clear')
        console.print(f'\n[red]● Erro: Cidade não encontrada.[/]\n')

while True:
    choice = input('\nDigite o nome de uma cidade, estado ou país: ')
    
    if choice.lower() == 'sair':
        break
    elif choice == '':
        city = search_local()
        search_clima(city)
    else:
        city = choice
        search_clima(city)
