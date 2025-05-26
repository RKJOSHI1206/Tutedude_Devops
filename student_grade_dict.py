stu_info = {}
for x in range(3):
    name = input("Enter student name : ")
    grade = input("Enter grade : ")
    print ("+++++++++++++++")
    stu_info.update({name: grade})
print(stu_info)
print("++++++ Updating the student grade +++++++ ")
name=input("Please enter Name :")
grade=input("New grade: ")
stu_info[name] = grade

print(stu_info)

