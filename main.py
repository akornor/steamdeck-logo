import requests
from bs4 import BeautifulSoup
import os.path

if __name__ == '__main__':
	response = requests.get('https://www.steamdeck.com/en/')
	soup = BeautifulSoup(response.text, 'html.parser')
	el = soup.select('.footer-logo img')[0]
	src = el.get('src')
	filename = os.path.basename(src)
	img_data = requests.get(src).content
	with open(f"img/{filename}", 'wb') as f:
		f.write(img_data)
