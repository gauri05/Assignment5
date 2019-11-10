print ("Python recurrsion  factorial.............")
def fact(no):
    if(no == 0):
        return 1
    return no * fact(no-1)

def main():
    no = int(input("Enter number:"))
    ans=fact(no)
    print ("ans::::",ans)


if __name__ == "__main__":
    main()
