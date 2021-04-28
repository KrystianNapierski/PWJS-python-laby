import math as m

class Punkty2D:
    def __init__(self):
         self.x=5
         self.x1=3
         self.y=3
         self.y1=5
        

    def Drukuj(self):
        print("x=", self.x, "y=", self.y)

    def Zeruj(self):
         self.x = 0
         self.y = 0
            

class Punkty3D(Punkty2D):
    def __init__(self):
        self.z=11
        Punkty2D.__init__(self)

    def Zeruj(self):
        self.x = 0
        self.y = 0
        self.z = 0
           
    def Drukuj(self):
        print("x=", self.x, "y=", self.y,"z=",self.z)

class Odcinek():
    def __init__(self):
        self.ab=0
        
    def Liczenie(self):
        a = Punkty2D()
        self.ab = m.sqrt(pow(a.x-a.x1, 2)+pow(a.y-a.y1, 2))
        print(self.ab)
            

def main():
    a = Punkty2D()
    print(a.x, a.y)
    a.Zeruj()
    print(a.x, a.y)
    a.x=13
    a.Drukuj()
    print("---------------")
    b= Punkty3D()
    print(b.x,b.y,b.z)
    b.Zeruj()
    print(b.x, b.y, b.z)
    b.x=11
    b.z=551
    b.Drukuj()
    print("---------------")
    c = Odcinek()
    c.Liczenie()


def testy():
    pass
if __name__ == "__main__":
    testy()
main()