#positional arguments/keyword arguments
def add(no1,no2):
    print("Value of no1",no1)
    print("Value of no2", no2)
    return no1+no2

def sub1(no1,no2):
    print("Value of no1",no1)
    print("Value of no2", no2)
    return no1-no2


def main():
    Ans=0
    Ans=add(10,21)
    print("Addition:",Ans)

    Ans = add(no2=10, no1=11)
    print("Addition:", Ans)

    Ans = sub1(no2=10, no1=11)
    print("Substraction:", Ans)

    Ans = sub1(no1=10, no2=11)
    print("Substraction:", Ans)

if __name__ == "__main__":
    main()