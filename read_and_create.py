import random
import xlrd
import time

# URL_FULL = "https://hyd-srv.oz-tms.com/bingoqr/api/addHydrantLog/I/05XXXXXXXX/T/6/V/0/S/0"
URL_BASIC = "https://hyd-srv.oz-tms.com/bingoqr/api/addHydrantLog/I/"


class Hydrant:
    def __init__(self, hydrant_phones, triggers, status, liter_range, bar_range):
        """this __init__ function takes the the arguments and make a url for sending as alert to hydrant system.
        The alert number is choosen randomaly by the function, and so the liter/bar value if needed"""
        self.hydrant_phones = hydrant_phones
        self.triggers = [num.strip() for num in triggers.split(",")]
        self.status = [num.strip() for num in status.split(",")]
        self.liter_range = [int(num) for num in liter_range.split(",")]
        self.bar_range = [int(num) for num in bar_range.split(",")]

        self.current_hydrant_phone = random.choice(hydrant_phones)
        self.current_trigger = random.choice(self.triggers)
        self.current_status = random.choice(self.status)
        self.current_liter = random.randrange(
            self.liter_range[0], self.liter_range[1])
        self.current_bar = random.randrange(
            self.bar_range[0], self.bar_range[1])
        self.value = 0

        if self.current_trigger in ["1", "2", "7"]:
            self.current_status = "0"
            if self.current_trigger in ["1", "2"]:
                self.value = self.current_liter
            else:
                self.value = self.current_bar
        else:
            self.current_status = "1"

        self.full_url = f"{URL_BASIC}{self.current_hydrant_phone}/T/{self.current_trigger}/V/{self.value}/S/{self.current_status}"

    def __str__(self):
        return self.full_url

    def event_continuation(self):
        try:
            if self.current_status == "0":
                # time.sleep(3)

                if self.current_trigger in ["1", "2"]:
                    self.value = random.randrange(
                        self.liter_range[0], self.liter_range[1])
                else:
                    self.value = random.randrange(
                        self.bar_range[0], self.bar_range[1])
                self.full_url = f"ZZZZ{URL_BASIC}{self.current_hydrant_phone}/T/{self.current_trigger}/V/{self.value}/S/{self.current_status}"
                return(self.full_url)
        except AttributeError:
            print("ZZZZZZZZZ")

    def end_event(self):
        pass


def reading_files():
    """this function read a file which contain variables (triggers, status, liter and bar ranges) and decompose it to
    seprated values for the next stage - Hydrant.__init__ """
    with open(r"C:\Users\USER\.vscode\Inbar's Projects\LearningPython\Hydrants\lists.txt", "r") as file:
        reading = file.readlines()
        for line in reading:
            split = line.strip().split(":")
            if split[0] == "triggers":
                global triggers
                triggers = split[1]
            elif split[0] == "status":
                global status
                status = split[1]
            elif split[0] == "liters_range":
                global liter_range
                liter_range = split[1]
            elif split[0] == "bars_range":
                global bar_range
                bar_range = split[1]

    file = r"C:\Users\USER\.vscode\Inbar's Projects\LearningPython\Hydrants\hydrants_phones.xls"
    wb = xlrd.open_workbook(file)
    sheet = wb.sheet_by_index(0)
    sheet.cell_value(0, 0)
    global hydrant_phones
    hydrant_phones = [sheet.cell_value(i, 0) for i in range(sheet.nrows)]


def welcome():
    print("Welcom to Hydrants' Keepie Simulator System\n\n")
    time = int(input("For How Long Time - in Minutes, Do You Want to Simulate?\n"))
    event = int(input("How Many Warnings (התרעה) Do You Want to Simulate?\n"))


def create_events(num=int, time=int):
    for i in range(num):
        i = Hydrant(hydrant_phones, triggers, status, liter_range, bar_range)
        print(i)


reading_files()
create_events(4, 1)
