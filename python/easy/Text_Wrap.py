import textwrap


def wrap(string, max_width):
    length = len(string) #26
    last = 0
    while length % max_width != 0:
        length -= 1
        last += 1
    total =""
    for i in range(len(string)):
            if i % max_width == 0 and i != 0:
                total += string[i-max_width:i]
                total +="\n"
    total += string[-last:]
    return total


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)