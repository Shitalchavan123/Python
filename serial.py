def sqaure(no):
    return no*no



def main():
    Data=[1,2,3,4,]
    result=[]

    for value in Data:
        result.append(sqaure(value))

    print("result after square operation:",result)

if __name__=="__main__":
    main()