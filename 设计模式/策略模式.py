# date: 01/07/20
# author: Crise

from collections import defaultdict
from abc import ABC, abstractmethod


# 简单工厂模式
class Promotion(ABC):
    @abstractmethod
    def discount(self, money):
        pass


class NormalPromotion(Promotion):
    def discount(self, money):
        return money


class DisCountPromotion(Promotion):
    def __init__(self, discount):
        self._discount = discount

    def discount(self, money):
        return money * self._discount


class ReducePromotion(Promotion):
    def __init__(self, reduction):
        self._reduction = reduction

    def discount(self, money):
        return money - self._reduction


class PromotionFactory:
    promotion = dict()
    promotion["discount"] = DisCountPromotion
    promotion["reduction"] = ReducePromotion

    def createPro(self, pro=None):
        if pro in self.promotion:
            return self.promotion[pro]
        else:
            return NormalPromotion


# if __name__ == "__main__":
#     commodity = input("please enter items separated by commas: ")
#     price = input("please enter price for every item separated by commas: ")
#     number = input("please enter number for every item separated by commas: ")
#
#     commoditys = defaultdict(float)
#
#     for i in range(len(commodity.split(","))):
#         singe_price = int(price.split(",")[i]) * int(number.split(",")[i])
#         commoditys[commodity.split(",")[i]] = singe_price
#         commoditys["total"] += singe_price
#
#     if commoditys["total"] > 5000:
#         pro = PromotionFactory().createPro("discount")
#         commoditys["total"] = pro(0.8).discount(commoditys["total"])
#         print(commoditys)
#     elif 1000 < commoditys["total"] < 5000:
#         pro = PromotionFactory().createPro("reduction")
#         commoditys["total"] = pro(400).discount(commoditys["total"])
#         print(commoditys)
#     else:
#         pro = PromotionFactory().createPro()
#         commoditys["total"] = pro().discount(commoditys["total"])
#         print(commoditys)


# ------------------------------------------------------------------------------


# 策略模式
class Promotion2(ABC):
    @abstractmethod
    def discount(self, money):
        pass


class NormalPromotionSt(Promotion2):
    def discount(self, money):
        return money


class DisCountPromotionSt(Promotion2):
    def __init__(self, discount):
        self._discount = discount

    def discount(self, money):
        return money * self._discount


class ReducePromotionSt(Promotion2):
    def __init__(self, reduction):
        self._reduction = reduction

    def discount(self, money):
        return money - self._reduction


class Promotion2Factory:
    promotion = dict()
    promotion["discount"] = DisCountPromotion
    promotion["reduction"] = ReducePromotion

    def createPro(self, pro=None):
        if pro in self.promotion:
            return self.promotion[pro]
        else:
            return NormalPromotion


if __name__ == "__main__":
    commodity = input("please enter items separated by commas: ")
    price = input("please enter price for every item separated by commas: ")
    number = input("please enter number for every item separated by commas: ")

    commoditys = defaultdict(float)

    for i in range(len(commodity.split(","))):
        singe_price = int(price.split(",")[i]) * int(number.split(",")[i])
        commoditys[commodity.split(",")[i]] = singe_price
        commoditys["total"] += singe_price

    if commoditys["total"] > 5000:
        pro = PromotionFactory().createPro("discount")
        commoditys["total"] = pro(0.8).discount(commoditys["total"])
        print(commoditys)
    elif 1000 < commoditys["total"] < 5000:
        pro = PromotionFactory().createPro("reduction")
        commoditys["total"] = pro(400).discount(commoditys["total"])
        print(commoditys)
    else:
        pro = PromotionFactory().createPro()
        commoditys["total"] = pro().discount(commoditys["total"])
        print(commoditys)
