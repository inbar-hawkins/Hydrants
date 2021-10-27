from random_url import triger, phone, liters, bars
import urllib.request


URL_FULL = "https://hyd-srv.oz-tms.com/bingoqr/api/addHydrantLog/I/05XXXXXXXX/T/6/V/0/S/0"
URL_BASIC = "https://hyd-srv.oz-tms.com/bingoqr/api/addHydrantLog/I/"


def create_initial_url():
    if triger == "1" or triger == "2":
        value = liters
        status = 0
    elif triger == "7":
        value = bars
        status = 0
    else:
        value = 0
        status = 1
    url = {f"{URL_BASIC}{phone}/T/{triger}/V/{value}/S/{status}"}
    return url


create_initial_url()


# this funcrion get url, and send it to the website of hydrants which send it the the DB
def send_url(url):
    response = urllib.request.urlopen(url)  # reading url http code
    html = response.read()
    # print(type(html))
    print(html)
