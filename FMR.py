def checkeven(no):
    return(no%2==0)

def increment(no):
    return no+2

def filterx(Arr,Function_Name):
    result=[]
    for no in Arr:
        if(Function_Name(no)):
            result.append(no)
        return result

def mapx(Arr,Function_Name):
    result=[]
    for no in Arr:
        if(Function_Name(no)):
            result.append(value)
        return result

def reducex(Arr,Function_name):
    sum=0
    for no in Arr:
        sum=sum+no
        return sum


def main():
    Data=[2,5,2,6]
    print("Original Data",Data)

    Data_Filter=list(filterx(Data,checkeven))

    print("Data after filter:",Data_Filter)

    Data_Map = list(mapx(Data_Filter,increment))

    print("Data after map:", Data_Map)

if __name__=="__main__":
    main()