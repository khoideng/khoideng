from bs4 import BeautifulSoup
import requests
import random
import csv

page = requests.get("https://vi.wikipedia.org/wiki/B%E1%BA%A3n_m%E1%BA%ABu:D%E1%BB%AF_li%E1%BB%87u_%C4%91%E1%BA%A1i_d%E1%BB%8Bch_COVID-19/S%E1%BB%91_ca_nhi%E1%BB%85m_theo_t%E1%BB%89nh_th%C3%A0nh_t%E1%BA%A1i_Vi%E1%BB%87t_Nam")
soup = BeautifulSoup(page.text, 'lxml')

body = soup.find('tbody')
statics = []

for a in body.find_all('tr'):
    statics.append(a.find_all('td'))

csv_file_all = open('cms_all.csv', 'w', encoding='utf-8')
csv_writer_all = csv.writer(csv_file_all)
csv_writer_all.writerow(['Tỉnh', 'Ca nhiễm', 'Ca tử vong', 'Tỉ lệ tử vong'])


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
        location = statics[0].get_text(strip=True)
        cases = int(statics[1].get_text(strip=True).replace('.', ''))
        deaths = int(statics[5].get_text(strip=True).replace('.', ''))
        return cls(location, cases, deaths)

    def introduction(self):
        return f'{self.location}: {self.cases} ca nhiễm - {self.deaths} ca tử vong - {self.percent} %'


class Vietnam():
    def __init__(self, name):
        self.name = name
        self.provinces = []

    def add_province(self, pro):
        self.provinces.append(pro)

    def file(self):
        total_cases = 0
        total_deaths = 0
        for province in self.provinces:
            total_cases += int(province.cases)
            total_deaths += int(province.deaths)

        csv_writer_all.writerow(['Việt Nam', total_cases, total_deaths, round(total_deaths/total_cases*100, 2)])

        for province in self.provinces:
            csv_writer_all.writerow([province.location, province.cases, province.deaths, province.percent])


def create_names():
    names = []
    letters = 'qwertyuiopasdfghjllzxcvbnm'
    while True:
        if len(names) == 63:
            break
        a = random.choice(letters) + random.choice(letters) + random.choice(letters)
        while a not in names:
            names.append(a)

    return names


vietnam = Vietnam('Vietnam')
for b, c in zip(create_names(), statics[2:-1]):
    b = Covid.fromstr(c)
    vietnam.add_province(b)

vietnam.file()

