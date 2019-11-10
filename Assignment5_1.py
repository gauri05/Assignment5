print("Arecursive program........")


def fun(val):
    #if val  <=1:
    if (val == 0):
        return 1
    print ("*",end = " ")
    return fun(val - 1)


def main():
    no = int(input("Enter number:"))
    fun(no)


if __name__ == "__main__":
    main()
