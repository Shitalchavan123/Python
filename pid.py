import os

def main():
    print("pid of current process is:",os.getpid())
    print("pid of parent process is:", os.getppid())

if __name__=="__main__":
    main()
