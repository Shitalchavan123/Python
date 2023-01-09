import threading
size=0


def evenlist(arr):
    for i in range(0,size,1):
        if(i%2==0):
            print("Even number:",i)

def oddlist(arr):
    for i in range(0,size,1):
        if(i%2!=0):
            print("Odd number:",i)


def main():
    print("Assignment 7")
    arr=list()
    print("Enter the size of elements")
    size=int(input())
    print("Enter the values")
    for i in range(0,size):
        no=int(input())
        arr.append(no)
    print(arr)

    p1= threading.Thread(target = evenlist, args = (arr,))
    p2= threading.Thread(target = oddlist, args = (arr,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Exit  from main")


if __name__== "__main__":
    main()