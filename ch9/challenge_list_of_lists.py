universities = [
    ["California Institute of Technology", 2175, 37704],
    ["Harvard", 19627, 39849],
    ["Massachusetts Institute of Technology", 10566, 40732],
    ["Princeton", 7802, 37000],
    ["Rice", 5879, 35551],
    ["Stanford", 19535, 40569],
    ["Yale", 11701, 40500],
]


def mean(listx):
    listtotal = 0
    for student in listx:
        listtotal = listtotal + student
    return listtotal / len(listx)


def median(listy):
    listy.sort()
    center = int((len(listy)+1)/2)
    return listy[center-1]


def enrollment_stats(data):
    count_list = list()
    tuition_list = list()
    for i in range(len(data)):
        count_list.append(data[i][1])
        tuition_list.append(data[i][2])
    return count_list, tuition_list


students_tuition = enrollment_stats(universities)
totalstudents = 0
totaltuition = 0

# print(students_tuition)
for i in students_tuition[0]:
    totalstudents = totalstudents + i
for x in students_tuition[1]:
    totaltuition = totaltuition + x

print("*****" * 5)
print(f"Total students: \t  {totalstudents}")
print(f"Total tuition: \t\t$ {int(totaltuition)}")
print(f"\nStudent mean: \t\t  {int(mean(students_tuition[0]))}")
print(f"Student median: \t  {median(students_tuition[0])}")
print(f"\nTuition mean: \t\t$ {int(mean(students_tuition[1]))}")
print(f"Tuition median: \t$ {median(students_tuition[1])}")
print("*****" * 5)

