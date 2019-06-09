from Date import Date
class Student:

    def __init__(self,name,date,score):
        self.__name = name
        self.__date=date
        date=Date
        self.__score=score
    def setName(self, name):
        self.__name = name         
    def setDate(self,m,d,y):
        self.__date.setDay(d)
        self.__date.setMonth(m)
        self.__date.setYear(y)
    def setScore(self, score):
        self.__score=score
    def getName(self):
        return self.__name
    def getDate(self):
        return self.__date
    def getScore(self):
        return self.__score
    def toString(self):
        print(self.getName(),end=" ")
        self.__date.toString()
        print(self.getScore(),"\n")

