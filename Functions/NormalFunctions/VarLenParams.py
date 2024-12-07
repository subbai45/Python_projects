#Program for Demonstrating the NEED of Variable Length Args
#This Program will not execute as it is bcoz PVM is doing Interpretation process and It Remembers only Latest Function Defintion but not all Function definitions with Same Name.
#VarArgsEx1.py
def dispvals(a,b,c,d,e): # Function Def-1
	print(a,b,c,d,e)
def dispvals(a,b,c,d): # Function Def-2
	print(a,b,c,d)
def dispvals(a,b,c): # Function Def-3
	print(a,b,c)
def dispvals(a,b): # Function Def-4
	print(a,b)
def dispvals(a): # Function Def-5
	print(a)
def dispvals(): # Function Def-6
	print("empty")

#Main Program
dispvals(10,20,30,40,50) # Function call-1 with Pos Args-----5
dispvals(10,20,30,40)   # Function call-2 with Pos Args-----4
dispvals(10,20,30)   # Function call-3 with Pos Args-----3
dispvals(10,20)   # Function call-4 with Pos Args-----2
dispvals(10)   # Function call-5 with Pos Args-----1
dispvals()   # Function call-6 with Pos Args-----0