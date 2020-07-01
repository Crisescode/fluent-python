# date: 01/07/20
# author: Crise

from collections import defaultdict
from abc import ABC, abstractmethod


class Cashier:
    def __init__(self):
        self.commoditys = defaultdict(float)

    def convert_str(self, string):
        if "." in string:
            return float(string)
        else:
            return int(string)

    def counter(self, commodity, price, number):
        single_price = self.convert_str(price) * self.convert_str(number)
        self.commoditys[commodity] = single_price
        self.commoditys["total"] += single_price
        return self.commoditys


if __name__ == "__main__":
    commodity = input("please enter items separated by commas: ")
    price = input("please enter price for every item separated by commas: ")
    number = input("please enter number for every item separated by commas: ")

    print(commodity.split(','))
    print(price.split(','))
    print(number.split(','))

    cashier = Cashier()

    for i in range(len(commodity.split(","))):
        commodity_display = cashier.counter(
            commodity.split(',')[i], price.split(",")[i], number.split(",")[i]
        )

    print(commodity_display)


# ------------------------------------------------------------------------------


# 简单工厂模式
class Cashier2:
    def __init__(self):
        self.commoditys = defaultdict(float)

    def convert_str(self, string):
        if "." in string:
            return float(string)
        else:
            return int(string)

    def counter(self, commodity, price, number):
        single_price = self.convert_str(price) * self.convert_str(number)
        self.commoditys[commodity] = single_price
        self.commoditys["total"] += single_price
        return self.commoditys


class Promotion(ABC):
    @abstractmethod
    def discount(self, order):
        pass


class NormalPromotion(Promotion):
    def discount(self, money):
        return money


class DisPromotion(Promotion):
    def discount(self, money, discount):
        return money * discount


class ReducePromotion(Promotion):
    def discount(self, order):
        pass


class PromotionFactory:
    pass


if __name__ == "__main__":
    commodity = input("please enter items separated by commas: ")
    price = input("please enter price for every item separated by commas: ")
    number = input("please enter number for every item separated by commas: ")

