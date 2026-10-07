class a:
    def __init__(self,a):
        self.a=a
    def __lt__(self,other):
        if (self.a<other.a):
            return("Obj 1 is smaller")
        else:
            return("Obj 1 is graterer")
    def __eq__(self,other):
        if (self.a==other.a):
            return("Equal ")
        else:
            return("Not equal ")
obj1=a(2)
obj2=a(3)
print("Passed value",obj1.a,obj2.a)
print(obj1<obj2)
obj3=a(4)
obj4=a(4)
print("Passed value",obj3.a,obj4.a)
print(obj3==obj4)