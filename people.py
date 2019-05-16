class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Hi my name is {}".format(self.name)


class Student(Person):
    def learn(self):
        return "I get it!"



class Instructor(Person):
    def teach(self):
        return "An object is an instance of a class"

Nadia = Instructor("Nadia")
print(Nadia)
Chris = Student('Chris')
print(Chris)
print(Nadia.teach())
print(Chris.learn())
print(Chris.teach()) # this method doesn't work here beacause teach is a method for Instructor and not
                    # for student. They are sibling classes so don't inherit eachother's methods