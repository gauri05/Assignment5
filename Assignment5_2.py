print("Arecursive program........")


def fun(val):
    #if val  <=1:
    if (val == 0):
        return 1
    #print (val,end = " ")
    fun(val - 1)
    print (val, end = " ")


def main():
    no = int(input("Enter number:"))
    fun(no)


if __name__ == "__main__":
    main()
