from functools import reduce

checkeven=lambda no:(no%2 == 0)


doubles=lambda no:(no*2)


sum=lambda a,b: a+b


def reducex(helper_function,Data):
    Ans=0
    for no in Data:
        Ans=helper_function(Ans,no)
        return Ans

def filterx(helper_function,Data):
    result=[]
    for no in Data:
        if(helper_function(no)==True):
            result.append(no)
            return result

def mapx(helper_function,Data):
    result=[]
    for no in Data:
        value=helper_function(no)
        result.append(value)
        return result



def main():
    print("Enter the number of elements you want to enter:")
    isize=int(input())

    Data_Input=[]
    print("Please enter the data")
    for icnt in range(0,isize,1):
        value=int(input())
        Data_Input.append(value)

        print("Data are:",Data_Input)

        Data_filter=filterx(checkeven,Data_Input)

        print("Data after filter:",Data_filter)

        Data_map=mapx(doubles,Data_filter)

        print("Data after map:",Data_map)

        output=reducex(sum,Data_map)

        print("Data after reduce:",output)


if __name__ == "__main__":
    main()