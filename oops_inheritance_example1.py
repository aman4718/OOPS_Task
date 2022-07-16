import logging
logging.basicConfig(filename="inheritance_ex1.log",level=logging.INFO,format='%(levelname)s %(asctime)s %(name)s %(message)s')
class ineuron:
    def salary(self,num_of_days,Day_count):
        try:
            self.num_of_days = num_of_days
            self.Day_count = Day_count
            logging.info('We are into function')
            salary = num_of_days * Day_count
            logging.info('Salary is :- %s', salary)
        except AttributeError:
            logging.info('Something Went Wrong In Salary Calculation Try Again with Valid Input')

class employee(ineuron):
    pass

i = employee();
i.salary(20,5)