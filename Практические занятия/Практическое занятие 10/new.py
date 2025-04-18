def gost(people, a):
    people = people.split(" ")
    if len(people) == 0:
        a = "никого"
    elif len(people) == 1:
        a = people[0]
    elif len(people) == 2:
        a = people[0]+people[1]
    elif len(people) == 3:
        a = people[0]+people[1]+people[2]
    return a
a ={}
people = input()
print(", ".join(gost(people, a)))