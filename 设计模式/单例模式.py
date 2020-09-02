# date: 21/07/20
# author: Crise


class Singleton(object):
    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(Singleton, "_Singleton__instance"):
            Singleton.__instance = object.__new__(cls)

        return Singleton.__instance


if __name__ == "__main__":
    a = Singleton()
    b = Singleton()
    print(a)
    print(b)
    print(a == b)
