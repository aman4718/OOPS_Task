class car :
    def __init__(self,body,engin , tyre):
        self.body = body
        self.engin = engin
        self.tyre = tyre

    def milage(self):
        print("milage of this car");
c = car('sold' , 'v6' , 'radial')

class tata(car):
    pass

t = tata("solid" , "v8" , "radial8")
print(t)
print(t.milage())