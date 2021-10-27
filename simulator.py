from random_url import triger, phone, liters, bars, BARS_RANGE, LITERS_RANGE
import urllib.request
import random


#URL_FULL = "https://hyd-srv.oz-tms.com/bingoqr/api/addHydrantLog/I/05XXXXXXXX/T/6/V/0/S/0"
URL_BASIC = "https://hyd-srv.oz-tms.com/bingoqr/api/addHydrantLog/I/"


def create_initial_url():
    """create the first random url"""
    if triger == "1" or triger == "2":
        value = liters
        status = 0
    elif triger == "7":
        value = bars
        status = 0
    else:
        value = 0
        status = 1
    url = f"{URL_BASIC}{phone}/T/{triger}/V/{value}/S/{status}"
    return url


url = create_initial_url()
print(url)


def create_next_url(url):
    """take first url and generate the next possible url based on the logic in the specifications"""
    status = url[-1:]
    #value = url[72:-4]
    temp_url = url[:72]
    new_url = url
    if status == "0":
        if triger == "7":
            start_bar = BARS_RANGE.split(",")[0]
            end_bar = BARS_RANGE.split(",")[1]
            new_value = random.randrange(int(start_bar), int(end_bar))
            new_url = f"{temp_url}{new_value}/S/{status}"
        elif triger == "1" or triger == "2":
            start_liter = LITERS_RANGE.split(",")[0]
            end_liter = LITERS_RANGE.split(",")[1]
            new_value = random.randrange(int(start_liter), int(end_liter))
            new_url = f"{temp_url}{new_value}/S/{status}"
        else:
            pass
    else:
        pass
    return new_url


print(create_next_url(url))


# this funcrion get url, and send it to the website of hydrants which send it the the DB
def send_url(url):
    response = urllib.request.urlopen(url)  # reading url http code
    html = response.read()
    # print(type(html))
    print(html)
