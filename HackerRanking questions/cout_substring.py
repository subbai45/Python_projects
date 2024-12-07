def count_substring(string, sub_string):
    count = 0
    start = 0
    while True:
        # Find the next occurrence of the sub_string
        start = string.find(sub_string, start)
        # If no more occurrences are found, break the loop
        if start == -1:
            break
        # Increment the count and move to the next character after the current match
        count += 1
        start += 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)