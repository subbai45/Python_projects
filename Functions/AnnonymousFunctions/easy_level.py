# to find the square of the given number by using anonymous functions(lambda functions)
# to find the sum of two number by using anonymous functions(lambda functions)
# to find whether number if even or odd by using anonymous functions(lambda functions)
# to find the maximum number from two numbers by using anonymous functions(lambda functions)
# to find the length of the given string by using anonymous functions(lambda functions)

# Beginner level

n = int(input("Enter the number: "))
a = float(input("Enter first value to add: "))
b = float(input("Enter second value to add: "))
sen = input("Enter anything: ")

#Anonymous Functions
square = lambda n: n**2
sum_op = lambda a,b: a+b
even_or_odd = lambda a: 'Even' if a%2==0 else 'Odd'
max_num = lambda a,b: a if a>b else b
len_sen = lambda sen: len(sen)

# main program
# function calls and retrieving results in sep variable object
square_res=square(n)
sum_res=sum_op(a,b)
even_or_odd_res=even_or_odd(n)
max_res=max_num(a,b)
len_sen_res=len_sen(sen)

#printing the ouputs

print(f"square of {n} is {square_res}")
print(f"sum of {a} + {b} = { sum_res}")
print(f"{n} is {even_or_odd_res}")
print(f"Max of two numbers {a} and {b} is {max_res}")
print(f"length of the given sentence -> {sen} is {len_sen_res}")