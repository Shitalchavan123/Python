
def sub(no1,no2):
    ans=0
    ans=no1-no2
    return ans

def Decorated_Function(Function_name):
    def Inner(A,B):
        if(A<B):
            A,B=B,A
        return Function_name(A,B)
    return Inner

def main():
    value1= int(input("Enter first number"))
    value2= int(input("Enter second number"))

    New_Function= Decorated_Function(sub)
    print(New_Function(value1,value2))

if __name__== "__main__":
        main()


