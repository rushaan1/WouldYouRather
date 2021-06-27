from bs4 import BeautifulSoup
import requests
while True:
    link = requests.get('http://either.io/').text
    soup = BeautifulSoup(link, 'lxml')
    op2find = soup.find('div', class_='result result-2')
    option2 = op2find.find('span', class_='option-text').text
    op1 = soup.find('div', class_='result result-1')
    option1 = op1.find('span', class_='option-text').text
    print(f"Would you rather? \n A:{option1} \n OR \n B:{option2}")
    input("Your Choice:")
