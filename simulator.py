from random_url import triger, phone, liters, bars, BARS_RANGE, LITERS_RANGE, STATUS, PHONES, TRIGERS
import urllib.request
import random


# URL_FULL = "https://hyd-srv.oz-tms.com/bingoqr/api/addHydrantLog/I/05XXXXXXXX/T/6/V/0/S/0"
URL_BASIC = "https://hyd-srv.oz-tms.com/bingoqr/api/addHydrantLog/I/"
# URL_LRNGTH = 77  # len(URL_FULL)


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


# url = create_initial_url()
# print(url)


def create_url_with_value_from_range(range, url):
    """get tange of values and sliced url  and return new url with random value from the range"""
    start_range = range.split(",")[0]
    end_range = range.split(",")[1]
    new_value = random.randrange(int(start_range), int(end_range))
    status = random.choice(STATUS)
    new_url = f"{url}{new_value}/S/{status}"

    return new_url


def create_next_url(url):
    """take first url and generate the next possible url in cases of triger 1,2,7 or None in other cases"""
    status = url[-1:]
    # value = url[72:-4]
    temp_url = url[:72]
    if status == "0":
        if triger == "7":
            return(create_url_with_value_from_range(
                BARS_RANGE, temp_url))
        elif triger == "1" or triger == "2":
            return(create_url_with_value_from_range(
                LITERS_RANGE, temp_url))


count = 0
while count != 20:
    url = create_initial_url()
    phone = random.choice(PHONES)
    triger = random.choice(TRIGERS)
    count += 1
    if url != None:
        status = url[-1:]
    print(url)
    while status != "1" and url != None:
        url = create_next_url(url)
        print(url)


# print(create_next_url(url))


def send_url(url):
    """this funcrion get url, and send it to the website of hydrants which send it the the DB"""
    response = urllib.request.urlopen(url)  # reading url http code
    html = response.read()
    # print(type(html))
    print(html)
