print("Application to Demonstrates Industrial Programming")

import marvellousmodule
def main():
        print("value of __name__from main is:", __name__)
        print("Enter first Number:")
        no1=int(input())

        print("Enter second Number:")
        no2=int(input())

        sum=marvellousmodule.Addition(no1,no2)

        print("Addition=",sum)

if __name__ == "__main__":
    main()