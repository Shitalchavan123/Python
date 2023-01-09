import threading

def thread1(no):
    print("Inside thread1")
    for i in range(0,no):

        print(i)

def thread2(no):
    print("Inside thread2")
    for i in range(0,no):
        no=no-1
        print(no)

def main():
    number=50
    t1=threading.Thread(target=thread1,args=(number,))
    t2=threading.Thread(target=thread2,args=(number,))

    t1.start()
    t1.join()

    t2.start()
    t2.join()

if __name__== "__main__":
    main()