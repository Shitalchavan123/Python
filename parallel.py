import os
import multiprocessing

def sqaure(no):
    print("PID of worker process is {} for the input {}".format(os.getpid(),no))
    return no*no

def main():
    print("Process Id of our application is:",os.getpid())
    Data=[1,2,3,4,]
    result=[]

    pobj= multiprocessing.Pool()

    result= pobj.map(sqaure,Data)

    print("result after square operation:",result)

if __name__=="__main__":
    main()