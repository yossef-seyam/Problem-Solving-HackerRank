if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    avg = 0
    #print(student_marks[name])
    for name in student_marks:
        if name == query_name:
            sum = float(student_marks[name][0])+float(student_marks[name][1])+float(student_marks[name][2])
            #print("Sum = ",sum)
            avg = sum/float(3)
    print("%0.2f"% avg)