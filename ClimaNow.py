from requests import get
from math import floor
import os
import time
import tqdm
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich import print as printr
from Rich import color, format

console = Console()

key = 'a4a46591cde2403cee5974af4a061503'

print(f"\n⚙️  {color.amarelo}System{color.end}: digite {format.bold}sair{format.end} para encerrar o programa. \n")

def load():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\nBuscando informações...')
    for _ in tqdm.tqdm(range(100), desc="Buscando", ncols=70):
        time.sleep(0.01)

def request(city):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&lang=pt_br&units=metric'
    response = get(url)
    data = response.json()

    if city.isspace() or city == '':
        os.system('cls' if os.name == 'nt' else 'clear')
        console.print(f'[bold red]Erro: Campo vazio[/]')
    elif city.isnumeric():
        os.system('cls' if os.name == 'nt' else 'clear')
        console.print(f'[bold red]Erro: Digite o nome de uma [underline]cidade[/][/]')
    elif response.status_code != 200 or response.status_code == 404:
        os.system('cls' if os.name == 'nt' else 'clear')
        console.print(f'[red]● Status: {response.status_code} Not Found[/]')
        console.print(f'[bold red]Erro: Cidade não encontrada[/]')
    else:
        load()
        os.system('cls' if os.name == 'nt' else 'clear')
        temp = floor(data['main']['temp'])

        title = f"{data['name']}, {data['sys']['country']}"
        conteudo = Text()
        conteudo.append(f"🌡️  Temperatura: ", style="bold")
        conteudo.append(f"{temp}°C\n", style="cyan")
        conteudo.append(f"☁️  Clima: ", style="bold")
        conteudo.append(f"{data['weather'][0]['description']}\n", style="cyan")
        conteudo.append(f"💧  Umidade: ", style="bold")
        conteudo.append(f"{data['main']['humidity']}%\n", style="cyan")
        conteudo.append(f"📈  Pressão: ", style="bold")
        conteudo.append(f"{data['main']['pressure']} hPa\n", style="cyan")
        conteudo.append(f"🌬️  Vento: ", style="bold")
        conteudo.append(f"{data['wind']['speed']} m/s\n", style="cyan")
        conteudo.append(f"🔥  Sensação térmica: ", style="bold")
        conteudo.append(f"{floor(data['main']['feels_like'])}°C", style="cyan")

        console.print(f'[green]● Status: {response.status_code}[/]')
        console.print(Panel(conteudo, title=title, border_style="bright_blue"), width=50)

while True:
    city = input("\nDigite o nome da cidade, estado ou país: ").capitalize()
    
    if city.lower() == 'sair':
        break

    request(city)
