class Student:
    licznik=0
    def __init__(self):
        Student.licznik +=1
        self.imie="Tomek"
        self.nazwisko="Kowalski"
        self.__student_nrIndeksu=15555
        self.kierunek="Informatyka"
        
    def __str__(self):
        return"Imie:%s, nazwisko:%s, kierunek:%s"%(self.imie,self.nazwisko,self.kierunek)

    def porownanie (self,other):
        if self.imie < other.imie:
            return False
        else:
            return True
        
    def getLicznik(self): 
        print("wartosc licznika:%d"%(Student.licznik))

class StudentInformatyki(Student):
    def __init__(self):
        super(StudentInformatyki,self).__init__()
        self.imie="Jacek"
        self.nazwisko="Błachowski"
        self.__student_nrIndeksu=13333
        self.kierunek="ISS"
        
    def __str__(self):
        return"Imie:%s, nazwisko:%s, kierunek:%s"%(self.imie,self.nazwisko,self.kierunek)

    def porownanie (self,other):
        if self.imie < other.imie:
            return False
        else:
            return True
        
    
        

def testy():
    pass
if __name__ == "__main__":
    testy()
    p=Student()
    wypisz=str(p)
    print(wypisz)
    p1=Student()
    p1.imie="Jan"
    p.porownanie(p1)
    p3=Student()
    p.getLicznik()
    print(p1.imie)
    b=StudentInformatyki()
    wypiszb=str(b)
    print(wypiszb)
    # print(p.__student_nrIndeksu)