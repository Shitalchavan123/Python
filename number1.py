class numbers:
    def __init__(self):
        self.size=0
        self.arr=list()

    def accept(self):
        print("Enter how many elemenys you want ")
        self.size= int(input())

        print("Enter the elements")
        value=0
        for i in range(0,self.size):
            value=int(input())
            self.arr.append(value)

    def display(self):
        print("Elements from list are")
        for i in range(0,self.size):
            print(self.arr[i])

    def summation(self):
       sum=0
       for i in range(0,self.size):
           sum=sum+self.arr[i]
       return sum


def main():
    obj=numbers()
    obj.accept()
    obj.display()

    output=obj.summation()
    print("Summation of numbers",output)

if __name__== "__main__":
    print("Inside starter")
    main()