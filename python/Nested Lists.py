if __name__ == '__main__':

    students = []
    for _ in range(int(input())):
        temp = []
        name = input()
        score = float(input())
        temp.append(name)
        temp.append(score)
        students.append(temp)
        # [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
    lowest = students[0]
    for student in students:
        if student[1] < lowest[1]:
            lowest = student

    students.remove(lowest)
    second = students[0]
    for student in students:
        if student[1] < second[1]:
            second = student
    students.remove(second)
    third = students[0]
    for student in students:
        if student[1] < third[1]:
            third = student
    students.remove(third)
    res = [second[0],third[0]]
    if second[1]==third[1]:
        res.sort()
        print('\n'.join(res))

    else:
        print(second[0])
        #print(third[0])


