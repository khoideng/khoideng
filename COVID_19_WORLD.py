from bs4 import BeautifulSoup
import requests
import random
import csv

page = requests.get("https://www.worldometers.info/coronavirus/")
soup = BeautifulSoup(page.text, 'lxml')

body = soup.find('tbody')
statics = []

for a in body.find_all('tr'):
    statics.append(a.find_all('td'))

csv_file_world = open('cms_world.csv', 'w', encoding='utf-8')
csv_writer_world = csv.writer(csv_file_world)
csv_writer_world.writerow(['Country', 'Cases', 'Deaths', 'Deaths per case'])

class Covid:
    def __init__(self, location, cases, deaths):
        self.location = location
        self.cases = int(cases)
        self.deaths = int(deaths)
        if float(self.deaths) == 0:
            self.percent = 0.0
        else:
            self.percent = round(float(self.deaths) / float(self.cases) * 100, 2)

    @classmethod
    def fromstr(cls, statics):
        location = statics[1].get_text(strip=True)
        cases = statics[2].get_text(strip=True).replace(',', '')
        if cases == '':
            cases = 0
        else:
            cases = int(cases)

        deaths = statics[4].get_text(strip=True).replace(',', '')
        if deaths == '':
            deaths = 0
        else:
            deaths = int(deaths)

        return cls(location, cases, deaths)

    def introduction(self):
        return f'{self.location}: {self.cases} ca nhiễm - {self.deaths} ca tử vong - {self.percent} %'

    def file(self):
        csv_writer_world.writerow([self.location, self.cases, self.deaths, self.percent])


def create_names():
    names = []
    letters = 'qwertyuiopasdfghjllzxcvbnm'
    while True:
        if len(names) == 230:
            break
        a = random.choice(letters) + random.choice(letters) + random.choice(letters)  + random.choice(letters)
        while a not in names:
            names.append(a)

    return names


for b, c in zip(create_names(), statics):
    b = Covid.fromstr(c)
    b.file()

csv_file_world.close()

# for i in statics:
#     for a in i:
#         print(a.text)

# i = int('10000'.replace(',', ''))
# print(i)