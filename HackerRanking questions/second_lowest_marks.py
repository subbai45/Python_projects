# to print the alphabetical names of equally got marks
lst=[]
score=[]
for _ in range(int(input())):
    names=input()
    marks=float(input())
    lst.append([names,marks]),score.append(marks)

sorted_marks=list(set(score))
#sorted_=sorted(sorted_marks)
sorted_marks.sort()
sec_max=sorted_marks[1]
print("sorted amrks are: ",sorted_marks)
print(sec_max)
print(lst,'\n',score)
sorted_name=[i[0] for i in lst if i[1]==sec_max]
sorted_name=sorted(sorted_name)
for name in sorted_name:
    print(name)