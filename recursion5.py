def display(no):
    sum=0
    if(no<=0):
        return 0
    else:
        return(no+display(no-1))

ret=display(4)

print("Addition=",ret)