import requests
from bs4 import BeautifulSoup


result = requests.get("https://amucontrollerexams.com/")
#print(result.status_code)
#print(result.headers)

src = result.content
#print(src)

soup = BeautifulSoup(src, 'html.parser')
#print(soup.prettify())

links = soup.find_all("a")
#print(links)  #python list
#print("\n")

for link in links:
	if "are" in link.text:
		print(link)
		print(link.attrs['href'])
