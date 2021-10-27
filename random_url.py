import random
import xlrd
# import urllib.request

# URL_FULL = "https://hyd-srv.oz-tms.com/bingoqr/api/addHydrantLog/I/05XXXXXXXX/T/6/V/0/S/0"
# URL_BASIC = "https://hyd-srv.oz-tms.com/bingoqr/api/addHydrantLog/I/"


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

#  this function get an exel file - only xls file, with hydrants phone numbers in one column,and return it in list


def get_phone():
    # exel file path
    file = (r"C:\Users\USER\.vscode\Inbar's Projects\LearningPython\Hydrants\hydrants_phones.xls")
    wb = xlrd.open_workbook(file)
    sheet = wb.sheet_by_index(0)
    sheet.cell_value(0, 0)

    return [sheet.cell_value(i, 0) for i in range(sheet.nrows)]


TRIGERS = get_trigers()
STATUS = get_status()
LITERS_RANGE = get_liters_range()
BARS_RANGE = get_bars_range()
PHONES = get_phone()

start_liter = LITERS_RANGE.split(",")[0]
end_liter = LITERS_RANGE.split(",")[1]
start_bar = BARS_RANGE.split(",")[0]
end_bar = BARS_RANGE.split(",")[1]

triger = random.choice(TRIGERS)
status = random.choice(STATUS)
liters = random.randrange(int(start_liter), int(end_liter))
bars = random.randrange(int(start_bar), int(end_bar))
phone = random.choice(PHONES)


# def create_initial_url():
#     if triger == "1" or triger == "2":
#         value = liters
#         status = 0
#     elif triger == "7":
#         value = bars
#         status = 0
#     else:
#         value = 0
#         status = 1
#     url = {f"{URL_BASIC}{phone}/T/{triger}/V/{value}/S/{status}"}
#     return url


# create_initial_url()


# # this funcrion get url, and send it to the website of hydrants which send it the the DB
# def send_url(url):
#     response = urllib.request.urlopen(url)  # reading url http code
#     html = response.read()
#     # print(type(html))
#     print(html)
