class ineuron:
    def __init__(self):
        self.students1 = "Data Science"

    def students(self):
        print(self.students1)

i = ineuron()
i.students()
i.students1 = "Data Analyst"
i.students()

class ineuron1:
    def __init__(self):
        self.__students1 = "Data Science"

    def students(self):
        print(self.__students1)
    def student_change(self,new_value):
        self.__students1 = new_value

i1 = ineuron1()
i1.students()
i1.__students1 = "Big Data"
i1.students()
i1.student_change("Aman")
i1.students()



# class
# object
# constructor
# inheritance
# private
# public
# protected
# abstraction
# encaptulations
# polymorpsim
# package
# modules
# method overrridding
#
# For all the concepts that we have discussed in our class point by point you have to write
# atleast 10 examples
# implement logging and exception handling have to use
# you have to make sure that use ineuron studnets , class , class type , number of courses
# , affiliates , blog, internship , jobs as a reference example
#sql workbench link windows - https://dev.mysql.com/downloads/windows/installer/8.0.html
#different system - https://dev.mysql.com/downloads/workbench