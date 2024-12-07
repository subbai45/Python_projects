#StudentMarksReportEx1.py
#accepting and Validating Student Number
while(True):
    sno=input("Enter Student Number:")
    if(sno.isdigit()):
        if(int(sno) in range(100,201)):
            break
        print("\t\t{} is Invalid student Number--try again".format(sno))
    else:
        print("\t\tDon't enter alnums and str symbols for student Number--try again".format(sno))

#accepting Name and Validate
while(True):
    name=input("Enter Student Name:")
    if (len(name) == 0):
        print("\t\t{} Don't Enter Space for  student Name--try again".format(name))
    else:
        res=True
        for word in name.split():
            if(not word.isalpha()):
                res=False
                break

        if(res):
            break
        else:
            print("\t\t{} is Invalid student Name--try again".format(name))
#accepting C Lang Marks and Validate
while(True):
    cm=input("Enter Marks in C Lang:")
    if (cm.isdigit()):
        cmarks=int(cm)
        if(cmarks in range(0,101)):
            break
        print("\t\t{} is Invalid Marks--try again".format(cmarks))
    else:
        print("\t\t{} Don't Enter strs,alnums and space for Marks in C--try again".format(cm))
#accepting C++ Lang Marks and Validate
while(True):
    cppm = input("Enter Marks in C++ Lang:")
    if (cppm.isdigit()):
        cppmarks = int(cppm)
        if (cppmarks in range(0, 101)):
            break
        print("\t\t{} is Invalid Marks--try again".format(cppmarks))
    else:
        print("\t\t{} Don't Enter strs, alnums, symbols for Marks in CPP--try again".format(cppm))
#accepting Python Lang Marks and Validate
while(True):
    pym = input("Enter Marks in Python Lang:")
    if (pym.isdigit()):
        pymarks = int(pym)
        if (pymarks in range(0, 101)):
            break
        print("\t\t{} is Invalid Marks--try again".format(pymarks))
    else:
        print("\t\t{} Don't Enter strs, alnums, symbols for Marks in CPP--try again".format(pym))
#Calculate Total Marks and Percentage of Marks
totmarks=cmarks+cppmarks+pymarks
percentage=(totmarks/300)*100
#Decide the Grade
# i)  Give Grade=FAIL Provided Student Secured Less than 40 in any of three subjects.
if(cmarks<40) or(cppmarks<40) or (pymarks<40):
    grade="FAIL"
else:
    #i) Given Grade = DISTINCTION provided totmarks ranges between (250,300)
    if(totmarks in range(250,301)):
        grade="DISTINCTION"
    elif(200<=totmarks<=249):
        grade="FIRST"
    elif(totmarks>=150) and (totmarks<=199):
        grade="SECOND"
    elif(totmarks in range(120,150)):
        grade="THIRD"
#Display Student Marks Report
print("*"*50)
print("\t\tS T U D E N T  M A R K S  R E P O R T")
print("*"*50)
print("\t\tStudent Number:{}".format(sno))
print("\t\tStudent Name:{}".format(name))
print("\t\tStudent C Marks:{}".format(cm))
print("\t\tStudent C++ Marks:{}".format(cppm))
print("\t\tStudent PYTHON Marks:{}".format(pymarks))
print("-"*50)
print("\t\tStudent Total Marks:{}".format(totmarks))
print("\t\tStudent Percentage of Marks:{}".format(round(percentage,2)))
print("\t\tStudent Result:{}".format(grade))
print("*"*50)
