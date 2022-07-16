class person :
    def __init__(self , name ,surname , yob):
        self._name1 = name
        self.__surname1 = surname
        self.yob1 = yob

sudh = person("sudhanshu" , "kumar" , 1990)
print(sudh._name1)
print(sudh._person__surname1)




class person :

    _name = "sudh"
    __surname = "kumar"
    yob = 1990

    def _age(self , current_year ):
        return current_year - self.yob
    def __age1(self , current_year ):
        return current_year - self.yob

obj = person()
print(obj._age(2022))
print(obj._person__age1(2022))

class employee(person) :
    _name = "sudhanshu"
    __surname = "singh"
    yob = 1991

obj1 = employee()
print(obj1._age(2022))
print(obj1._person__age1(2022))
print(obj1)
print(obj1.yob)
print(obj1._name)
print(obj1._employee__surname)


from utils.utill1 import person2

obj = person2("sudhansu " , "kumar" , 345345)
print(obj.yob1)

class person1 :
    def __init__(self , name ,surname , yob):
        self._name1 = name
        self.__surname1 = surname
        self.yob1 = yob

sudh = person1("sudhanshu" , "kumar" , 1990)
print(sudh._name1)
print(sudh._person1__surname1)

class person2:
    def __init__(self , name ,surname , yob):
        self._name1 = name
        self.__surname1 = surname
        self.yob1 = yob

sudh = person2("sudhanshu" , "kumar" , 1990)
print(sudh._name1)
print(sudh._person2__surname1)

import test1
print(test1)
obj3 = test1.person1("sudhanshu" , "kumar" , 1994)
print(obj3.yob1)
print(obj3._name1)
print(obj3._person1__surname1)


class person :

    _name = "sudh"
    __surname = "kumar"
    yob = 1990

    def _age(self , current_year ):
        return current_year - self.yob
    def __age1(self , current_year ):
        return current_year - self.yob

obj = person()
print(obj._age(2022))
print(obj._person__age1(2022))

class employee(person) :
    _name = "sudhanshu"
    __surname = "singh"
    yob = 1991

obj1 = employee()
print(obj1._age(2022))
print(obj1._person__age1(2022))
print(obj1)
print(obj1.yob)
print(obj1._name)
print(obj1._employee__surname)

# https://github.com/drsunithaev/OOP_Ex/blob/main/DataStructures_Qn.py
# https://github.com/atharv4git/Ineuron/tree/main/tasks/task4
# https://github.com/BokkisamRohit/task6_02-07-2022/blob/main/stringTasks.py
# https://github.com/BokkisamRohit/task6_02-07-2022/blob/main/listTasks.py
# https://github.com/udayavel/FSDS/blob/main/ds_class.py
# https://github.com/piyush-123/Tasks/blob/main/Task_02Jul2022.py
# https://github.com/piyush-123/Tasks/blob/main/Task_02Jul2022.py
# https://github.com/Arunava-Biswas/Ineuron-FSDS/blob/main/Live%20Classes/Class%20work/task/test.py
#
# https://github.com/anilpadiyar/Assignment/blob/main/oops1_Task.py
# https://github.com/AnkurYadav00/challenges/blob/main/List_s.py
# https://github.com/AnkurYadav00/challenges/blob/main/Dict_s.py
# https://github.com/AnkurYadav00/challenges/blob/main/String_s.py
# https://github.com/AnkurYadav00/challenges/blob/main/Tuple_s.py
#
