import time
import multiprocessing

def displayeven(no):
    for i in range(1,no,1):
        if(i%2==0):
            print("Given number is even",i)


def displayodd(no):
    for i in range(1,no,1):
        if(i%2!=0):
            print("Given number is even",i)


def main():
    print("Demonstration of parallel programming using multiple processes")
    number=2000

    p1 = multiprocessing.process(target = displayeven, args = (number,))
    p2 = multiprocessing.process(target = displayodd, args = (number,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("End of main")

if __name__== "__main__":
    start_time=time.process_time()
    main()
    end_time=time.process_time()
    print("Execution time is=",end_time-start_time)