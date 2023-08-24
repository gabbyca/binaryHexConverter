def toBinary(raw):
    result = ""
    dig = raw
    while dig > 0:
        if (dig % 2 != 0):
            result += str(1)
        else:
            result += str(0)
        dig  = (dig // 2)
    if len(result) < 8:
        while len(result) < 8:
            result += str(0)
    result = (reverse(result))

    tempList = []
    for char in result:
        tempList.append(int(char))
    for i in range(len(tempList)):
        tempList[i] = 1-tempList[i]
    for i in range(len(tempList)-1, -1, -1):
        if (tempList[i] == 1):
            tempList[i] = 0
        else:
            tempList[i] = 1
            return tempList







def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str;


dict = {
    10: "A",
    11: "B",
    12: "C",
    13: "D",
    14: "E",
    15: "F"
}
def hexadecimal(norm):
    result = ""
    dig = norm
    while dig > 0:
        if (dig % 16 != 0):
            if dig % 16 > 9:
                value = dict[(dig % 16)]
                result += str(value)
            else:
                result += str(dig % 16)
        else:
            result += str(0)
        dig = (dig // 16)
    return (reverse(result))

input = int(input("Enter a number: "))
if (input >= 0) & (input <= 100000):
    if (input >= 0) & (input <= 127):
        print(toBinary(input))
    else:
        print(hexadecimal(input))
