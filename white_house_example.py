import requests
from bs4 import BeautifulSoup


result = requests.get("https://www.whitehouse.gov/briefings-statements/")

src = result.content
#print(src)

soup = BeautifulSoup(src, 'html.parser')
#print(soup.prettify())

urls = []

for h2_tag in soup.find_all("h2"):
	a_tag = h2_tag.find("a")
	urls.append(a_tag.attrs['href'])

#print(len(urls))
print(urls)
