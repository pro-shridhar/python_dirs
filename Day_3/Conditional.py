def stu_m(marks):
    if marks > 0 and marks < 30:
        print("Fail")
    elif marks > 30 and marks < 50:
        print("3rd Division")
    elif marks > 50 and marks < 70:
        print("2nd Division")
    elif marks > 70 and marks < 100:
        if marks > 90:
            print("Excellent")
            return
        print("1st Division")
    else:
        print("Invelid marks")


list = list(map(int, input("give me marks ").split()))
# print(list)

for i in list:
    stu_m(i)
