class Grandparent:
    def __init__(self, name):
        self.name = name

    def introduce_grandparent(self):
        print(f"I am the Grandparent, my name is ram {self.name}.")

class Parent(Grandparent):
    def __init__(self, name, job):
        super().__init__(name)
        self.job = job

    def introduce_parent(self):
        print(f"I am the Parent, my name is  sham {self.name} and I am a {self.job}.")

class Child(Parent):
    def __init__(self, name, job, hobby):
        super().__init__(name, job)
        self.hobby = hobby

    def introduce_child(self):
        print(f"I am the Child, my name is {self.name}, my job is {self.job}, and my hobby is {self.hobby}.")
my_child = Child("", "trader", "reading")
my_child.introduce_grandparent()
my_child.introduce_parent()
my_child.introduce_child()