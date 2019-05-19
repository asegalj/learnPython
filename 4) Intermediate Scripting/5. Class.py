class MyClass:
    def __init__(self):
        self.str1 = "abc"
    def func(self):
        return self.str1

a = MyClass()
print(a.func())

b = MyClass()
b.str1 = "abcd"
print(b.func())