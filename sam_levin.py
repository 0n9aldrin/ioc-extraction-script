import requests
from bs4 import BeautifulSoup
import csv

a = []
try:
    for y in range(1, 55):
        res = requests.get('https://www.theguardian.com/profile/sam-levin?page=' + str(y))
        html_soup = BeautifulSoup(res.text, 'html.parser')
        
        total = html_soup.findAll('a', class_ = 'u-faux-block-link__overlay js-headline-text')
        for x in range(len(total)):
            a.append([total[x].text,total[x]['href']])
        print("Page " + str(y) + '    ' + str(len(a)))
except:
    print('done')




with open('sam_levin.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(a)
