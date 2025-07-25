class Person:
    def __init__(self,name):
        self.name=name
    def setName(self,name):
        self.name=name
    def getName(self):
        return self.name
person=Person("abc")
person.setName("bob")
person.getName