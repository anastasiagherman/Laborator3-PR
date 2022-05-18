from Andys import Andys
import sys

def displayOptions():
    print("\n1: Test getPage")
    print("2: Test loginCookies")
    print("3: Test headRequest")
    print("4: Test optionsRequest")
    print("5: Download images")
    print("6: Exit")
    y = int(input("Enter the option := "))
    return y

def chooseOption(x):
    global option
    if x == 1:
        andys.getPage()
        option = displayOptions()
        chooseOption(option)
    elif x == 2:
        andys.getPageCookies()
        option = displayOptions()
        chooseOption(option)
    elif x == 3:
        andys.headRequest()
        option = displayOptions()
        chooseOption(option)
    elif x == 4:
        andys.optionsRequest()
        option = displayOptions()
        chooseOption(option)
    elif x == 5:
        andys.downloadImages()
        option = displayOptions()
        chooseOption(option)
    elif x == 6:
        sys.exit()

option = None

if __name__ == "__main__":

    andys = Andys("testingemailacount@gmail.com", "testingAccount01")
    option = displayOptions()
    chooseOption(option)
