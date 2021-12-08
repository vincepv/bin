import requests
from bs4 import BeautifulSoup
import re

URL = "https://www.meteolanguedoc.com/actualites-meteo-languedoc/r1"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

my_list = soup.select(".page-titre")
my_list = str(my_list)

pattern = '<.*?>'
repl = ''
result = re.sub(pattern, repl, my_list)
print(result)