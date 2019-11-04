from math import log, floor

def describe3Digits(n):
    descUnits = {1: "one", 2: "two", 3: "three"}
    descTens = {2: "twenty", 3: "thirty"}
    descCents = {}
    for i in descUnits:
        descCents[i] = descUnits[i] + "hundreds"

def describeInt(n):

    descBlock = {0:"", 1:"thousand", 2:"million", 3:"billion"}


    nDigits = floor(log(n)/log(10))+1
    nBlocks = nDigits//3+1
    for i in range(nBlocks):
        b = (n//(1000**i))%1000
        if b:
            print(b, descBlock[i])
    pass

if __name__ == "__main__":
    examples = [1909303, 390, 29930, 10]
    for val in examples:
        print("Example", val)
        describeInt(val)

