numOfLoops = int(input("Enter num of commands: "))

def add(a,b):
    return a+b

for i in range(0, numOfLoops):
    temp = input()
    tempToList = temp.split()
    if tempToList[0] == "ADD":
        print(float(tempToList[1])+float(tempToList[2]))
    elif tempToList[0] == "SUB":
        print(float(tempToList[1]) - float(tempToList[2]))