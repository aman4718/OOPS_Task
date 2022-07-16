class ineuron:
    def student(self):
        print("Print details of all the students")
    def archives(self):
        print("print the list of all archives")
    def hall_of_fame(self):
        print("Print everyone from hall of fame")
        
class ineuron_vision(ineuron):
    def student(self):
        print("this are the filter student list")

iv = ineuron_vision()
iv.student();