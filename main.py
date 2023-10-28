import http.client
from time import strftime
from datetime import datetime
from bs4 import BeautifulSoup

def main():
    write_to_file()


def get_curr_status():
    # Request data from https://rent.pe.ntu.edu.tw
    connection = http.client.HTTPSConnection('rent.pe.ntu.edu.tw')
    connection.request("GET", "/")
    response = connection.getresponse()
    r = response.read().decode()

    # parse page
    soup = BeautifulSoup(r, 'html5lib')
    gym = soup.select_one('div.CMFlowPeople > div > div.CMCList > div:nth-child(1) > div.IC > div:nth-child(1) > span').text
    swim = soup.select_one('div.CMFlowPeople > div > div.CMCList > div:nth-child(2) > div.IC > div:nth-child(1) > span').text
    now = datetime.now().strftime("%Y-%m-%d\t%a\t%H:%M")
    return f"{now}\t{gym}\t{swim}\n"


def write_to_file():
    with open("docs/counts.tsv", "a") as f:
        data = get_curr_status()
        f.write(data)


if __name__ == "__main__":
    main()
