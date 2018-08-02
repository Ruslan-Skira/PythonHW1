import datetime
age = int(input("enter the age please"))
name = str(input("fill up the name please"))
quantity = int(input("how many times I need to copy lines"))
now = datetime.datetime.now().year
def hundredYearsOld(age, name):
    if age < 100:
        ned = str(100 - age + now)
        answer = str(ned + name)
    elif age == 100:

        answer = 1
    else:
        answer = 1

    return answer

user1 = hundredYearsOld(age, name)
print(user1)
copying = user1 * quantity
print(copying)
