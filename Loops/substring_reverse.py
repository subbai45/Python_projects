# to implement the sub_stirng of the given input string and reverse the substring and display the string

sen=input("Enter the line of text: ")
if(len(sen)<=0):
    print("EMPTY string, please enter something")
var=sen.split()
for i in range(len(var)): #range(0,len(var))
    rev=(var[i][::-1])
    print(rev,end=" ")


