print("Arecursive program+ Summation of digit.......")

ans=0
def fun(val):
    global ans
    if val==0:
        return 1
    digit=val%10
    #print (digit)
    ans=ans+digit
    n=val//10
    fun(n)
    return ans



def main():
    no = int(input("Enter number:"))
    ans1=fun(no)
    print(ans1)


if __name__ == "__main__":
    main()
