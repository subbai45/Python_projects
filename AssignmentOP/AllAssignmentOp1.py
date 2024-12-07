#program to read sno,sname,marks in a multiline assignment

sno,sname,marks=int(input("Enter the sno.: ")),input("Enter the sname: "),float(input("Enter the marks: "))
print("="*40)
print("Student's Number is {}".format(sno))
print("Student's Name is {}".format(sname))
print("Student's marks are %0.2f" %marks)
print("="*40)