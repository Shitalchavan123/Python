#function which accpects nothing and returns nothing
def Demo1():
    print("Inside Demo1");

#function which accpects one parameter and returns nothing
def Demo2(no):
    print("Inside Demo2:",no)

#function which accpects one parameter and returns one parameter
def Demo3(no):
    print("Inside Demo3:",no);
    return no+2
#function which accpects two parameter and returns one parameter
def Demo4(no1,no2):
    print("Inside Demo4")
    Add=no1+no2
    return Add
#function which accpects two parameter and returns two parameter
def Demo5(no1,no2):
    print("Inside Demo5")
    Add=no1+no2
    Sub=no1-no2
    return Add,Sub


def main():
    Demo1()
    Demo2("Hello")
    Ans=Demo3(10)
    print("Return value Demo3:",Ans)
    Ans=Demo4(20,50)
    print("Addition:",Ans)
    Ans1,Ans2=Demo5(90,60)
    print("Addition=",Ans1)
    print("Sub=", Ans2)

if __name__ == "__main__":
    main()