def mutate_string(string, position, character):
    mutate = list(string)
    mutate.insert(position, character)
    mutate.pop(position + 1)

    return "".join(mutate)


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)