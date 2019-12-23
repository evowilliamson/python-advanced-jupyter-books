import importlib

class Advisor(object):
    def advice1(self, **kwargs):
        print(kwargs)

    def advice2(self, **kwargs):
        print("2")

    def advice(self, **kwargs):
        my_function = getattr(self, "advice1")
        my_function(**kwargs)

a = Advisor()
a.advice(b=100, c=200)