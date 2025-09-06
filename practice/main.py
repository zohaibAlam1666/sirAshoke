



class student:
    def __init__(self, rollId, name, age):
        self.rollId = rollId
        self.name = name
        self.age = age

    def greet(self):

        print (f"user name is :{self.age}, {self.rollId},{self.name}")

    def test(self, name):
        return name
    
        

student12 = student (2343, "ashok",35)
student12.greet()

student45 = student (2454, "Zohaib", 25)
student45.greet()

student98 = student (34343, "alam", 35)
print(student98.test("alam"))