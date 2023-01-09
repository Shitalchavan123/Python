import time

def displayeven(no):
    for i in range(1,no,1):
        if(i%2==0):
            print("Given number is even",i)


def displayodd(no):
    for i in range(1,no,1):
        if(i%2!=0):
            print("Given number is even",i)


def main():
    print("Demonstration of serial programming")
    displayeven(2000)
    displayodd(2000)

if __name__== "__main__":
    start_time=time.process_time()
    main()
    end_time=time.process_time()
    print("Execution time is=",end_time-start_time)