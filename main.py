# inital code of the day


nums = [1, 2, 3, 4]
squares = [n * n for n in nums]
# Equivalent long form:
squares2 = []
for n in nums:
    squares2.append(n * n)



nums = range(1, 11)
evens = [n for n in nums if n % 2 == 0]



matrix = [[1,2], [3,4], [5,6]]
flat = [x for row in matrix for x in row]
# Equivalent loops:
flat2 = []
for row in matrix:
    for x in row:
        flat2.append(x)



student = {
    "name" : "ali",
    "age" : 12,
    "id" : 9898
}

for strudentkey, strudentvalue in zip(student):
    print("sdjksdjf")


for key in student:
    print(key, ":", student[key])



for k, v in zip(student.keys(), student.values()):
    print(k, ":", v)
