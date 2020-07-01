# date: 01/07/20
# author: Crise


# 初学者写法
class Operation:
    def __init__(self):
        pass

    def convert_str(self, string):
        if "." not in string:
            return int(string)
        else:
            return float(string)

    def op(self, strA, strB, strOp):
        if strOp == "+":
            return self.convert_str(strA) + self.convert_str(strB)
        elif strOp == "-":
            return self.convert_str(strA) - self.convert_str(strB)
        elif strOp == "*":
            return self.convert_str(strA) * self.convert_str(strB)
        elif strOp == "/":
            try:
                return self.convert_str(strA) / self.convert_str(strB)
            except ZeroDivisionError:
                raise Exception("除数不能为0")
        else:
            print("不支持这个运算！")


# if __name__ == "__main__":
#     opr = Operation()
#     print(opr.op("3", "1.5", "/"))


# -----------------------------------------------------------------------------


# 简单工厂模式
class Operation2:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def GetResult(self):
        pass

    def covert_str(self, string):
        if "." not in string:
            return int(string)
        else:
            return float(string)


class OperationAdd(Operation2):
    def GetResult(self):
        return self.covert_str(self.num1) + self.covert_str(self.num2)


class OperationSub(Operation2):
    def GetResult(self):
        return self.covert_str(self.num1) - self.covert_str(self.num2)


class OperationMul(Operation2):
    def GetResult(self):
        return self.covert_str(self.num1) * self.covert_str(self.num2)


class OperationDiv(Operation2):
    def GetResult(self):
        try:
            return self.covert_str(self.num1) / self.covert_str(self.num2)
        except ZeroDivisionError:
            raise Exception("除数不能为0.")


class OperationUndef(Operation2):
    def GetResult(self):
        raise NotImplementedError("不支持的运算符！")


class OperationFactory:
    operation = dict()
    operation["+"] = OperationAdd
    operation["-"] = OperationSub
    operation["*"] = OperationMul
    operation["/"] = OperationDiv

    def createOp(self, ch, num1, num2):
        if ch in self.operation:
            op = self.operation[ch](num1, num2)
        else:
            op = OperationUndef(num1, num2)

        return op


if __name__ == "__main__":
    op = input("op: ")
    num1 = input("num1: ")
    num2 = input("num2: ")

    factory = OperationFactory()
    op = factory.createOp(op, num1, num2)

    print(op.GetResult())
