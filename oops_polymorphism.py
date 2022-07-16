class ineuron:
    def students(self):
        print("Print Students Details")

class class_type:
    def students(self):
        print("print the class type of students")

def inuron_external(a):
    a.students()

i = ineuron()
j = class_type()
inuron_external(i)
inuron_external(j)

def test(a,b):
    return  a+b
print(test(3,4))
print(test('aman','kumar'))