
class Arithmatic:

    def __init__(self,A,B):
        print("Inside init method")
        self.no1=A
        self.no2=B
    def addition(self):
        Ans=self.no1+self.no2
        return Ans
        print("Addition="+Ans)

    def sub(self):
        Ans=self.no1-self.no2
        return Ans
        print("substraction=" + Ans)

def main():
    print("Inside main method")

    obj=Arithmatic(20,11)
    output=obj.addition()
    print("Adition=",output)

    output=obj.sub()
    print("Substraction",output)


if __name__== "__main__":
    print("Inside starter")
    main()
