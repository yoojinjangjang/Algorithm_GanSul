from functools import cmp_to_key


def comparator(o1, o2):
    if o1[1] > o2[1]:
        return 1
    elif o1[1] == o2[1]:
        if o1[2] < o2[2]:
            return 1
        elif o1[2] == o2[2]:
            if o1[3] > o2[3]:
                return 1
            elif o1[3] == o2[3]:
                if o1[0] < o2[0]:
                    return 1
    return -1


n = int(input())
students = []
for i in range(n):
    name, korean, math, english = input().split()
    students.append([name, int(korean), int(math), int(english)])

students.sort(key=cmp_to_key(comparator), reverse=True)
for i in students:
    print(i[0])