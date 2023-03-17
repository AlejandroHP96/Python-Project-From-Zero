import time
from goodbye import Goodbye
from grettings import Grettings


class App:
    def __init__(self):
        self.__getGrettings()

    def __getGrettings(self):
        print(Grettings().getGrettings())
        time.sleep(2)
        print(Goodbye().getGoodbyes())
