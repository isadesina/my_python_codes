def docstr_demo():
    """
    this funtion is to demonstrate how docstings work
    :return: This function returns nothing
    """
    pass


def greater(a, b):
    """
    this function takes 2 numbers and returns the greater number
    parameter: int, float

    :return: return the greater number
    """
    if a > b:
        return a
    else:
        return b


def greaater_3(a, b, c):
    rslt_1 = greater(a, b)
    rslt_2 = greater(rslt_1, c)
    return rslt_2


def printGrade(score):
    if score < 0 or score > 100:
        print("invalid entry")
        return None
    elif score > 90:
        print("You scored an A")
    elif 90 >= score > 70:
        print("you scored a B")
    elif 70 >= score > 60:
        print("you scored a C")
    elif 60 >= score > 45:
        print("you scored a D")
    else:
        print("you scored an F")


print("this is to demo function control")
name = "olumide"
if name.count("e") >= 1:
    printGrade(110)


# default variable
def RectangleArea(L=1, B=2):
    samp_var = 14
    return L * B


# global and local variables
globalVar = 1


def func():
    LocalVar = 2
    print(globalVar)  # accesed inside the function
    print(LocalVar)
    print("This is the way global var is accesed within the funciton")
    return LocalVar


def main():
    docstr_demo()
    greater()
    greaater_3()
    RectangleArea()
    globalVar = 1
    func()