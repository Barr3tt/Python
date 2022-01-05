import requests, sys
from bs4 import BeautifulSoup
class Webscrape():
    def __init__(self):
        r = requests.get('https://sociallydistant.site')
        soup = BeautifulSoup(r.content, 'html.parser')
        output = [soup.title.text]
        self.outfile(output)
    def outfile(self, input):
        sys.stdout = open('output.txt', 'w')
        for ip in input:
            sys.stdout.write(ip + '\n')
        sys.stdout.close()
Webscrape()