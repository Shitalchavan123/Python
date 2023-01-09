print("Application to Demonstrates Industrial Programming")
def Addition(value1,value2):
    ans=value1+value2
    return ans
def main():
    print("Enter First Number:")
    no1=int(input())

    print("Enter second Number:")
    no2=int(input())

    sum=Addition(no1,no2)

    print("Addition=",sum)

if __name__ == "__main__":
    main()