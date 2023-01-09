def fact(no):

    if(no<=0):
        return 1
    else:
        return(no*fact(no-1))

ret=fact(4)

print("Addition=",ret)