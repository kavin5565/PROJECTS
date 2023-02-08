import requests
from bs4 import BeautifulSoup
def ExtractData(url):
    response = requests.get(url = url).content
    soup = BeautifulSoup(response,'lxml')

    table = soup.find("table",{"cellspacing":0})
    tdd   = table.find("td")
    trr   = table.find_all("tr")

    table1 = soup.find("table",{"width":1004})
    spann  = table1.find("span")
    mapp   = table1.find("map")
    divv   = table1.find("div")


    print(mapp)


    table2 = soup.find("a",{"class":"Menu"})



ExtractData(url="https://etenders.gov.in/eprocure/app")


with open("report.csv","w") as csv_file:
    csv_write = csv.writer(csv_file)
    csv_write.writerow(table1)

