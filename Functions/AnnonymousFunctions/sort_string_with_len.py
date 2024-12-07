# sort the strings according to their len and store them in dict
# strings = ["apple", "bat", "cat", "elephant", "dog", "ant", "zebra", "rat"]
# {
#     3: ['bat', 'cat', 'dog', 'ant', 'rat'],
#     5: ['apple'],
#     7: ['zebra'],
#     8: ['elephant']
# }

final_data = {}
string = ["apple", "bat", "cat", "elephant", "dog", "ant", "zebra", "rat"]
# string = input("Enter the string by giving space: ").split()

# main program

for i in string:
    length = len(i)
    if length not in final_data:
        final_data[length] = []
    final_data[length].append(i)

print(final_data)