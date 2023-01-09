def display(no):
    cnt=0
    if cnt<no :
        print("Hello")
        cnt=cnt+1
        display(no)

def main():
    display(4)


if __name__== "__main__":
    main()