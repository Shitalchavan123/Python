def main():
    arr=list()

    print("Enetr how many elements you want to store?")
    size=int(input())

    print("Enter the Values")
    for i in range(0,size,1):
        no=int(input())
        arr.append(no)  #arr.insert(i,no)
        print(arr)



if __name__== "__main__":
     main()