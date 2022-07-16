class ineuron:
    __students = "Data Science"

    def students(self):
        print('Print the class of student' , ineuron.__students)

i = ineuron()
i.students()
print(i._ineuron__students)
# directly not acciccible ,with class name can access