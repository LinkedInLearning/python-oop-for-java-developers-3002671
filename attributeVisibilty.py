class A():
    def __init__(self):
        self.__priv = "I am private"
        self._prot = "I am protected"
        self.pub = "I am public"

x = A()
print(x.pub)
print(x._prot)
print(x.__priv)

