# # inital code of the day


# nums = [1, 2, 3, 4]
# squares = [n * n for n in nums]
# # Equivalent long form:
# squares2 = []
# for n in nums:
#     squares2.append(n * n)



# nums = range(1, 11)
# evens = [n for n in nums if n % 2 == 0]



# matrix = [[1,2], [3,4], [5,6]]
# flat = [x for row in matrix for x in row]
# # Equivalent loops:
# flat2 = []
# for row in matrix:
#     for x in row:
#         flat2.append(x)



# student = {
#     "name" : "ali",
#     "age" : 12,
#     "id" : 9898
# }

# for strudentkey, strudentvalue in zip(student):
#     print("sdjksdjf")


# for key in student:
#     print(key, ":", student[key])



# for k, v in zip(student.keys(), student.values()):
#     print(k, ":", v)




studen = {
    "name": "ali",
    "id" : 1278,
    "greet" : lambda name : print(f"wellcome back {name}")
}


for x,y in zip(studen.keys(), studen.values()):
    if x != "greet" and y == 1278:
        print(x,y)


class student: 

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.somting = "ksdjfkljsd"

    def greet(self):
        print(f"the name of the student is {self.name} the age is {self.age}")



s1 = student("ali",14)
s1.greet()
s2 = student("ksdjfkls0", 3434)
s2.greet()


