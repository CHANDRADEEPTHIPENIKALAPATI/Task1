class Demo:
    def show(self,a=None,b=None,c=None):
        if a and b and c:
            print(a,b,c)
        elif a and b:
            print(a,b)
        elif b and c:
            print(b,c)
        else:
            print("None")
a=Demo()
a.show()
a.show(a:1,b:2,c:3)
a.show(a:1,b:2)
a.show(1)