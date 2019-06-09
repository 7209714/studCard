from Date import Date
from student import Student

def main():
    name=input()
    month=int(input())
    day=int(input())
    year=int(input())
 #   d1=Date()
    
    s1=Student("John", Date(6, 1, 1999), 90) 
    s2=Student("Marry", Date(10, 8, 1997), 80)

    s1.setName(name)
    s2.setDate(month,day,year)

    s1.toString()
    s2.toString()
main()