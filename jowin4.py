#WAP to change the roll no. of a student.

class student:
    def __init__(self, name, roll_no, age):
        self.name = name
        self.__roll_no = roll_no
        self.__age = age

    def show(self):
        print('Student Details: ', self.name, self.__roll_no)

    def get_roll_no(self):
        return self.__roll_no

    def set_roll_no(self, number):
        if number > 50:
            print('Invalid roll no. Please set correct roll number')
        else:
            self.__roll_no = number
    
s1 = student('Jowin', 10, 15)
s1.show()
s1.set_roll_no(120)

s1.set_roll_no(25)
s1.show

