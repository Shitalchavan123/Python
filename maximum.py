def maximum(no1,no2):
    if(no1>no2):
        return no1;
    else:
        return no2

def main():
    print("Enter First Number")
    value1=input()

    print("Enter Second Number")
    value2=input()

    Ans = maximum(int(value1),int(value2))

    print("Largest Number=",Ans)



if __name__ =="__main__":
      main()