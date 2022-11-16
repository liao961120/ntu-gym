import json
import http.client
from time import strftime
from datetime import datetime

def main():
    write_to_file()


def get_curr_status():
    # Request data from https://ntusportscenter.ntu.edu.tw/counter.txt
    connection = http.client.HTTPSConnection('ntusportscenter.ntu.edu.tw')
    connection.request("GET", "/counter.txt")
    response = connection.getresponse()
    COUNT = json.loads(response.read().decode())
    gym, swim = COUNT['CounterData'][0]['innerCount'].split(";")
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    return f"{now}\t{gym}\t{swim}\n"


def write_to_file():
    with open("docs/counts.tsv", "a") as f:
        data = get_curr_status()
        f.write(data)


if __name__ == "__main__":
    main()