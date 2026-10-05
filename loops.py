
# for x in "Tomal khan":
#     print(x)

# for x in [2, 3, 5, 6]:
#     print(x)

# for x in ["a", "b", "c"]:
#     print(x)

# for x in range(2, 10, 2):
# # print(x)


names = ["Arman, Badhsa"]

for name in names:
    if name.startswith:
        print("fount")
        break


def add(a, b):
    return a + b


# print(add(2, 3))

def division(a, b=5):
    return a / b


print(division(22))
def incrament(*user):
    result = 0
    for number in user:
        result = result + number
    print(result)
incrament(1, 2, 3, 4)


def save_user(**user):
    print(user["id"])


save_user(id=1, name="admin")

# while loop

count = 1

while count <= 5:
    print(count)
    count += 1


for i in range(1, 11):
    if i == 5:
        continue
    print(i)
