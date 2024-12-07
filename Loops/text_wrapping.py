# text wrapping

import textwrap as tw

string = input("Enter the string you want to wrap: ")
width = int(input("Enter the max width length: "))

fill = tw.fill(string,width)
wrap = tw.wrap(string,5)
shorten = tw.shorten(string,26)
print("fill",fill)
print("wrap",wrap)
print("shorten",shorten)

print("="*60)

