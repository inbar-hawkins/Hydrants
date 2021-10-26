import random
from urllib.parse import urlparse

URL_FULL = "https://hyd-srv.oz-tms.com/bingoqr/api/addHydrantLog/I/05XXXXXXXX/T/6/V/0/S/0"
URL_BASIC = "https://hyd-srv.oz-tms.com/bingoqr/api/addHydrantLog/I/"


def get_trigers():
    with open("C:\\Users\\USER\\.vscode\\Inbar's Projects\\LearningPython\\Hydrants\\lists.txt", "r") as fl:
        triger_list = fl.readlines()
    return triger_list[0].strip().split(":")[1].split(',')


def get_status():
    with open("C:\\Users\\USER\\.vscode\\Inbar's Projects\\LearningPython\\Hydrants\\lists.txt", "r") as fl:
        status_list = fl.readlines()
    return status_list[1].strip().split(":")[1].split(",")


def get_liters_range():
    with open("C:\\Users\\USER\\.vscode\\Inbar's Projects\\LearningPython\\Hydrants\\lists.txt", "r") as fl:
        liters_range = fl.readlines()
    return liters_range[2].strip().split(":")[1]


def get_bars_range():
    with open("C:\\Users\\USER\\.vscode\\Inbar's Projects\\LearningPython\\Hydrants\\lists.txt", "r") as fl:
        bars_range = fl.readlines()
    return bars_range[3].strip().split(":")[1]


def get_phone():
    return "0526663334"


# TRIGERS = get_trigers().split(":")[1].split(',')
TRIGERS = get_trigers()
STATUS = get_status()
LITERS_RANGE = get_liters_range()
BARS_RANGE = get_bars_range()

print(STATUS)
print(TRIGERS)
print(LITERS_RANGE)
print(BARS_RANGE)

start_liter = LITERS_RANGE.split(",")[0]
end_liter = LITERS_RANGE.split(",")[1]
start_bar = BARS_RANGE.split(",")[0]
end_bar = BARS_RANGE.split(",")[1]

triger = random.choice(TRIGERS)
status = random.choice(STATUS)
liters = random.randrange(int(start_liter), int(end_liter))
bars = random.randrange(int(start_bar), int(end_bar))
phone = get_phone()

url = {f"{URL_BASIC}{phone}/T/{triger}/V/{liters}/S/{status}"}
print(url)

print(f"triger is {triger}")
print(f"status is {status}")
print(f"liters are {liters}")
print(f"bars are {bars}")


# def get_phone_number():
# HYDRANTS_PHONES = ["0544555444", "0544564654", "0545554545", "0526663334"]

#
