import googletrans
import requests
from bs4 import BeautifulSoup

# Url da página
url = 'https://www.techworld-with-nana.com/post/what-is-sre'

# Realizando um request usando request lib
page = requests.get(url)

# Parsing page using bs4
soup = BeautifulSoup(page.content, "html.parser")

# Pegando todos os header da página
headers = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

# Tradução apra espanhol
translator = googletrans.Translator()
spanish_header = []
for header in headers:
    translated_headers = {
        "text": translator.translate(header.text, dest='es').text,
        "name": header.name
    }
    spanish_header.append(translated_headers)

# Criando um arquivo HTML com os headers traduzidos para espanhol
with open("header_espanhol.html", "w", encoding="utf-8") as file:
    file.write('<html>\n')
    for header in spanish_header:
        file.write(f'<{header["name"]}>{header["text"]}</{header["name"]}>\n')
    file.write('</html>\n')


def df_constructor ():
    pass

def insert_into_db ():
    pass
