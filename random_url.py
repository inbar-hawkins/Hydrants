import random
import xlrd


def get_trigers():
    """open text file with trigers list, status list, liters range and bars range and retrieve trigers list"""
    with open("C:\\Users\\USER\\.vscode\\Inbar's Projects\\LearningPython\\Hydrants\\lists.txt", "r") as fl:
        triger_list = fl.readlines()
    return triger_list[0].strip().split(":")[1].split(',')


def get_status():
    """open text file with trigers list, status list, liters range and bars range and retrieve status list"""
    with open("C:\\Users\\USER\\.vscode\\Inbar's Projects\\LearningPython\\Hydrants\\lists.txt", "r") as fl:
        status_list = fl.readlines()
    return status_list[1].strip().split(":")[1].split(",")


def get_liters_range():
    """open text file with trigers list, status list, liters range and bars range and retrieve liters range"""
    with open("C:\\Users\\USER\\.vscode\\Inbar's Projects\\LearningPython\\Hydrants\\lists.txt", "r") as fl:
        liters_range = fl.readlines()
    return liters_range[2].strip().split(":")[1]


def get_bars_range():
    """open text file with trigers list, status list, liters range and bars range and retrieve bars range"""
    with open("C:\\Users\\USER\\.vscode\\Inbar's Projects\\LearningPython\\Hydrants\\lists.txt", "r") as fl:
        bars_range = fl.readlines()
    return bars_range[3].strip().split(":")[1]


def get_phone():
    """this function get an excel file - only xls file, with hydrants phone numbers in one column,and return it in list"""
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
# bars = round(random.uniform(int(start_bar), int(end_bar)), 2)  #for presuure as a float num
phone = random.choice(PHONES)
